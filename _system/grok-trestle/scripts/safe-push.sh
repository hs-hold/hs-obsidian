#!/usr/bin/env bash
# Safe commit + push for the shared vault. Usage:
#   safe-push.sh "<bot name>" "<commit message>"
# - takes a box-wide lock (several bots share one clone)
# - git pull --rebase --autostash
# - stages everything, refuses to commit if the secrets scan finds anything (exit 3)
# - commits as "<bot name>", pushes, retries pull --rebase + push up to 3 times
# Never prints the token (auth comes from the configured git credential helper).
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="${VAULT:-$(cd "$HERE/../../.." && pwd)}"
BOT="${1:-Grok Bot}"; MSG="${2:-vault update}"
LOCK="/tmp/hs-obsidian-vault.lock"
exec 9>"$LOCK"
flock -w 120 9 || { echo "PUSH: FAIL could not get vault lock in 120s (another bot is writing). Retry."; exit 4; }
cd "$VAULT" || exit 1
git pull --rebase --autostash -q || { echo "PUSH: FAIL pull --rebase hit a conflict. Run: git -C \"$VAULT\" status"; exit 5; }
git add -A
if git diff --cached --quiet; then echo "PUSH: OK nothing to commit"; 
  [ "$(git rev-list --count @{u}..HEAD 2>/dev/null || echo 0)" = "0" ] && exit 0; fi
if ! python3 "$HERE/secrets-scan.py" --staged; then
  git reset -q
  echo "PUSH: BLOCKED secrets found in staged files - nothing committed. Remove the value (or move it to _private/, which is git-ignored) and retry."
  exit 3
fi
if ! git diff --cached --quiet; then
  git -c user.name="$BOT" -c user.email="bot@hs-holdings.local" commit -q -m "[$BOT] $MSG" || exit 1
fi
for i in 1 2 3; do
  if git push -q origin HEAD:main 2>/tmp/hs-vault-push.err; then
    echo "PUSH: OK $(git rev-parse --short HEAD) [$BOT] $MSG"; exit 0; fi
  sed -E 's#https://[^@ ]+@#https://***@#g' /tmp/hs-vault-push.err | tail -3
  git pull --rebase --autostash -q || { echo "PUSH: FAIL rebase conflict on retry $i"; exit 5; }
done
echo "PUSH: FAIL after 3 attempts"; exit 6
