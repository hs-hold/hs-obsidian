# Grok Trestle — המדריך המלא

מדריך לכלי הזיכרון המשותף של הבוטים של H.S HOLDINGS בכספת ה-Obsidian. גרסה 1.0, 16 בנובמבר 2026.

## 1. מה זה ועל מה זה מבוסס

**Grok Trestle** הוא סט כלים שגורם לכל הבוטים שלנו (Grok Bot, Deal Analysis, מחקר שוק אטלנטה ואינדיאנפוליס, Contract Desk, Zip Intel, Content Insights, Deal Inbox ומזכירה) לעבוד עם זיכרון משותף אחד: כספת Obsidian שיושבת במאגר GitHub פרטי `hs-hold/hs-obsidian`.

הרעיון המרכזי: כל עבודה נפתחת ב**טקס פתיחה** (הבוט מושך את המידע העדכני וקורא את ההקשר), ונסגרת ב**טקס סגירה** (הבוט כותב בחזרה מה למד, מה הוחלט ומה פתוח, בודק שהכול תקין ומעלה ל-GitHub). כך הידע מצטבר מעבודה לעבודה ולא הולך לאיבוד בין שיחות ובין בוטים.

הכלי מבוסס על הפרויקט הפתוח [trestle](https://github.com/liormesh/trestle) של Lior Meshullam (רישיון MIT), שבנוי במקור ל-Claude Code. לקחנו ממנו את השיטה והתאמנו אותה לבוטים של גרוק ולעבודת הנדל"ן שלנו.

מה יש בכלי:
- 5 מיומנויות (skills) לבוטים: ראיון הקמה, פתיחת סשן, סגירת סשן, בדיקת בריאות, דוח מצב.
- 6 סקריפטים קטנים שרצים על ה-box בלי שום התקנה (python3 ו-bash בלבד).
- 6 תבניות פתקים: פרופיל, פרויקט, עסקה, איש קשר, פגישה, יומן בוט.
- פרופיל החברה `00 Profile.md` ושני פרויקטים ראשונים בתיקייה `Projects`.

## 2. מה שונה מהמקור

| נושא | trestle המקורי | Grok Trestle שלנו |
|---|---|---|
| למי | משתמש יחיד עם Claude Code במחשב שלו | 9 בוטים של גרוק שחולקים box אחד ושלושה שותפים |
| איפה הזיכרון | תיקייה מקומית + קבצי זיכרון של Claude | כספת Obsidian במאגר GitHub פרטי, מסונכרנת לכל המכשירים |
| הפעלה | פקודות `/cq`, `/73`, `/onboard` | משפט רגיל לבוט: "פתח סשן Indy", "סגור סשן" |
| שומרים (hooks) | hooks של Claude Code שחוסמים כתיבה של סודות | אין hooks לגרוק, לכן הסריקה רצה בכל commit דרך `safe-push.sh`, שמסרב להעלות אם נמצא סוד |
| סקריפטים | Node.js | python3 ו-bash בלבד, בלי התקנות |
| עבודה במקביל | לא רלוונטי | נעילה (`flock`) כדי ששני בוטים לא יכתבו לגיט באותו רגע, ו-`pull --rebase` לפני כל העלאה |
| תוכן | פיתוח תוכנה | נדל"ן: עסקאות, אנשי קשר, שווקים, קריטריונים לפליפ ו-BRRRR |
| דוח | `/visualize` כללי | דוח מצב HTML בעברית שנשמר בתוך הכספת |
| רישיון | MIT | אותו MIT, עם קרדיט מלא ב-`LICENSE-trestle-MIT.txt` |

## 3. מבנה התיקיות

```
hs-obsidian/                         (the vault = the GitHub repo)
├── 00 Profile.md                    company profile, criteria, rules, bots
├── 00 Inbox/                        quick notes not filed yet
├── Projects/                        one note per project
│   ├── Indy Trip Nov 2026.md
│   └── Deal Pipeline.md
├── Deals/                           one note per deal (address.md)
├── Contacts/                        brokers, wholesalers, contractors, lenders
├── Markets/Atlanta/ , Markets/Indianapolis/
├── Meetings/                        YYYY-MM-DD title.md
├── Notes/                           owner notes
├── Agents/<bot name>.md             append-only work log per bot
├── .gitignore                       _private/, .env, workspace files
└── _system/
    ├── reports/vault-report.html    latest status report
    └── grok-trestle/
        ├── README.md, LICENSE-trestle-MIT.txt
        ├── GUIDE-he.md/.html, GUIDE-en.md/.html
        ├── skills/<5 skills>/SKILL.md
        ├── scripts/                 python3 + bash, stdlib only
        └── templates/               profile, project, deal, contact, meeting, agent-log
```

על ה-box הכספת נמצאת בנתיב `/home/box/shared/obsidian-vault`.

## 4. הקמה חד-פעמית

### 4.1 מה כבר מוכן (לא צריך לעשות כלום)
- המאגר הפרטי `hs-hold/hs-obsidian` קיים, והבוטים מחוברים אליו עם טוקן שמוגבל רק למאגר הזה.
- הכלי, התבניות, הפרופיל והפרויקטים כבר הועלו.
- נשאר לרשום את 5 המיומנויות אצל הבוטים (Grok Bot עושה את זה) ולחבר את Obsidian אצלך.

### 4.2 טוקן למכשירים שלך
מומלץ טוקן נפרד לכל מכשיר שלך, כדי שתוכל לבטל אחד בלי לפגוע בבוטים:
1. היכנס ל-[דף יצירת הטוקן](https://github.com/settings/personal-access-tokens/new) ב-GitHub.
2. Token name: למשל `obsidian-laptop`. Expiration: לפי בחירתך (שנה זה נוח).
3. Resource owner: `hs-hold`. Repository access: **Only select repositories** ובחר רק `hs-obsidian`.
4. Permissions → Repository permissions → **Contents: Read and write**. (Metadata: Read-only מתווסף לבד.)
5. Generate token, והעתק אותו מיד. GitHub מציג אותו פעם אחת בלבד.
6. שמור אותו במנהל הסיסמאות שלך. **לא** בכספת, ולא בצ'אט.

### 4.3 חיבור Obsidian במחשב (Windows או Mac)
1. התקן Git: ב-Windows מ-[git-scm.com](https://git-scm.com/download/win) (עם Git Credential Manager, ברירת המחדל). ב-Mac הרץ בטרמינל `git --version` ואשר את ההתקנה אם תתבקש.
2. פתח טרמינל (ב-Windows: Git Bash או PowerShell) ושכפל את המאגר לתיקייה שבה תרצה את הכספת:

```bash
cd ~/Documents
git clone https://github.com/hs-hold/hs-obsidian.git
```

3. כשתתבקש: Username = שם המשתמש שלך ב-GitHub, Password = **הטוקן** (לא הסיסמה). ב-Windows ייפתח חלון של Git Credential Manager, ושם אפשר גם להתחבר דרך הדפדפן. ב-Mac כדאי קודם להריץ פקודה ששומרת את הטוקן ב-Keychain:

```bash
git config --global credential.helper osxkeychain
```

4. ב-Obsidian: **Open folder as vault** ובחר את התיקייה `hs-obsidian`.
5. Settings → **Community plugins** → **Turn on community plugins** → **Browse** → חפש **Git** (של Vinzent03) → **Install** → **Enable**.
6. Settings → Git, והגדר:
   - **Pull on startup**: מופעל.
   - **Auto pull interval (minutes)**: `5`.
   - **Auto commit-and-sync interval (minutes)**: `10`.
7. בדיקה: פתח את Command palette (Ctrl/Cmd+P) והרץ **Git: Pull**. אמור להופיע `00 Profile.md` ובו פרטי החברה.

### 4.4 חיבור Obsidian בטלפון (Android או iPhone)
> המפתח של התוסף עצמו כותב שגרסת המובייל "לא יציבה במיוחד" ועלולה לקרוס במאגר גדול. היא עובדת לכספת קטנה כמו שלנו, אבל אם יש בעיות, אפשרות חלופית היא האפליקציה GitSync (Android ו-iOS) או Working Copy (iOS, בתשלום).

1. התקן Obsidian מהחנות, וצור **כספת חדשה וריקה** בשם `hs-obsidian`. באייפון **אל** תסמן Store in iCloud.
2. Settings → Community plugins → Turn on → Browse → **Git** → Install → Enable.
3. Settings → Git → בחלק **Authentication/Identity**: Username = שם המשתמש ב-GitHub, Password/Personal access token = הטוקן של המכשיר (סעיף 4.2). אל תיגע בהגדרות Advanced.
4. Command palette → **Git: Clone an existing remote repo**.
5. הדבק את הכתובת עם `.git` בסוף ולחץ על הכפתור שמתחת לשדה:

```
https://github.com/hs-hold/hs-obsidian.git
```

6. כשתישאל על תיקייה, בחר את שורש הכספת. כשתישאל על `.obsidian`, ענה לפי מה שמוצג (בדרך כלל NO, אין צורך להוריד הגדרות). חכה להודעה **Restart Obsidian** ואתחל את האפליקציה.
7. אחר כך הגדר Pull on startup ו-Auto pull כמו במחשב.

### 4.5 רישום המיומנויות אצל הבוטים
את זה Grok Bot עושה. נתיבי 5 התיקיות לרישום:

```
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-setup-interview
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/session-open
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/session-close
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-health-check
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-report
```

## 5. שימוש יומיומי

### 5.1 פתיחת סשן
כתוב לכל בוט, למשל:
- "פתח סשן Indy"
- "פתח סשן Deal Pipeline"
- "פתח סשן" (בלי פרויקט: פרופיל, יומן הבוט ומשימות פתוחות)

הבוט ימשוך עדכונים מ-GitHub, יקרא את הפרופיל, את פתק הפרויקט, את 40 השורות האחרונות ביומן שלו, את כל המשימות הפתוחות ואת מצב הבריאות, ויחזיר לך סיכום קצר. מאחורי הקלעים זו פקודה אחת:

```bash
python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/session-open.py --agent "Deal Analysis" --project "Indy"
```

### 5.2 סגירת סשן
בסוף עבודה כתוב "סגור סשן" או "תשמור באובסידיאן". הבוט:
1. בוחר מהשיחה רק דברים מאומתים: מה נלמד (עם מקור), מה הוחלט, מה נשאר פתוח ומה בוצע.
2. מוסיף רישום מתוארך ליומן שלו `Agents/<bot>.md` ולפתק הפרויקט, תחת `## Log`.
3. מסמן משימות שבוצעו (`- [ ]` הופך ל-`- [x]`).
4. מריץ בדיקת בריאות.
5. מעלה ל-GitHub בצורה בטוחה, וזה נכנס לך ל-Obsidian תוך כמה דקות.

```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/session-close.py --agent "Deal Analysis" --project "Deal Pipeline" \
  --summary "Screened 3 Atlanta deals" \
  --learned "ARV for 123 Main St is 250k (source: URL)" \
  --decision "Pass on 123 Main St - ROI 9%" \
  --task "Get rehab quote for 45 Oak Ave"
python3 $S/vault-health.py
bash $S/safe-push.sh "Deal Analysis" "session close: Deal Pipeline"
```

### 5.3 טיפים
- אפשר לבקש גם באמצע: "תשמור את זה באובסידיאן", וזו אותה סגירת סשן.
- עסקה חדשה → הבוט יוצר `Deals/<כתובת>.md` מהתבנית. איש קשר → `Contacts/<שם>.md`. פגישה → `Meetings/YYYY-MM-DD <נושא>.md`.
- אתה עצמך יכול לכתוב פתקים ב-Obsidian כרגיל. הם יעלו אוטומטית והבוטים יראו אותם בפתיחת הסשן הבאה.
- משימה = שורה שמתחילה ב-`- [ ]`. כך כל הבוטים והדוח מזהים אותה.

## 6. המיומנויות (skills) אחת-אחת

### 6.1 vault-setup-interview — ראיון הקמה
- **מתי:** "ראיון הקמה", "עדכן פרופיל", "הוסף פרויקט", או כשפתיחת הסשן מדווחת שאין פרופיל.
- **מה:** עד 8 שאלות, אחת בכל פעם: חברה ושותפים, שווקים, קריטריונים, סגנון וכללים, בוטים, פרויקטים, עובדות ומשימות.
- **כותב:** `00 Profile.md` ו-`Projects/<שם>.md` מהתבניות. נרשם רק מה שאמרת, בלי ניחושים.
- אפשר להריץ שוב בכל זמן. בריצה חוזרת הוא שואל רק על מה שחסר או השתנה.

### 6.2 session-open — פתיחת סשן
- **מתי:** "פתח סשן <פרויקט>", או בתחילת כל משימה משמעותית.
- **מה:** pull, ואז פרופיל, פרויקט, יומן הבוט, משימות פתוחות, Inbox ובריאות, הכול בקריאה אחת וחסכונית בטוקנים.
- **לא כותב כלום.**

### 6.3 session-close — סגירת סשן
- **מתי:** "סגור סשן", "תשמור באובסידיאן", בסוף משימה, או אחרי החלטה או ממצא חשוב.
- **מה:** רישום מתוארך ליומן ולפרויקט, סימון משימות שבוצעו, בדיקת בריאות ו-commit+push בטוח.
- **כלל ברזל:** רק הוספה, לא מחיקה של תוכן של אחרים. רק עובדות מאומתות עם מקור.

### 6.4 vault-health-check — בדיקת בריאות
- **מתי:** "בדיקת בריאות לכספת", לפני כתיבה גדולה, או כשסגירה מראה WARN.
- **מה:** קישורים שבורים, פתקים בלי frontmatter או בלי `type:`, פרויקטים פעילים שלא עודכנו 14 יום, פתקי Inbox ישנים מ-7 ימים, ספירת משימות, סריקת סודות ומצב סנכרון.

### 6.5 vault-report — דוח מצב
- **מתי:** "דוח כספת", "מה המצב באובסידיאן".
- **מה:** קובץ HTML אחד בעברית, שנפתח בטלפון ובלי אינטרנט: בריאות, פתקים לפי תיקייה, פרויקטים, משימות פתוחות, פעילות כל בוט ו-15 השינויים האחרונים. הקובץ נשמר ב-`_system/reports/vault-report.html`.

## 7. בדיקת בריאות ודוח

```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/vault-health.py                 # full check
python3 $S/vault-health.py --stale-days 30 # looser staleness
python3 $S/secrets-scan.py                 # secrets only
python3 $S/vault-report.py                 # HTML report into the vault
```

| תוצאה | משמעות | מה עושים |
|---|---|---|
| `OK` | תקין | כלום |
| `INFO` | מידע (מספר משימות) | כלום |
| `WARN FRONTMATTER` | חסר בלוק `---` או `type:` | להעתיק את הראש מהתבנית המתאימה |
| `WARN LINKS` | `[[קישור]]` לפתק שלא קיים | לתקן את השם או ליצור את הפתק |
| `WARN STALE` | פרויקט פעיל שלא זז, או Inbox ישן | להחליט על הצעד הבא או לשנות `status:` |
| `WARN SYNC` | שינויים שלא הועלו | סגירת סשן או `safe-push.sh` |
| `FAIL SECRETS` | נמצא משהו שנראה כמו סיסמה או טוקן | **לא להעלות**. למחוק ולהשאיר הפניה |

קוד יציאה: 0 תקין, 1 יש WARN, 2 יש FAIL.

## 8. כללי אבטחה

1. **אף פעם** לא כותבים לכספת סיסמאות, טוקנים, מפתחות API, מספרי כרטיס או פרטי התחברות. כותבים רק איפה הם שמורים, למשל "הסיסמה אצל הבעלים במנהל הסיסמאות".
2. `safe-push.sh` סורק כל commit. אם נמצא סוד, **שום דבר לא עולה** וחוזרת הודעה `PUSH: BLOCKED`.
3. הסריקה היא רשת ביטחון ולא הגנה מושלמת (כמו שכותב גם המפתח המקורי). האחריות היא לא לכתוב סודות מלכתחילה.
4. אם סוד כבר עלה ל-GitHub, מחיקה לא מספיקה כי הוא נשאר בהיסטוריה. **חייבים לבטל אותו ולהנפיק חדש** (rotate).
5. הטוקן של הבוטים מוגבל רק למאגר `hs-obsidian`, ורק ל-Contents. לכל מכשיר שלך כדאי טוקן נפרד, כדי שאפשר יהיה לבטל אחד בלי לפגוע באחרים.
6. התיקייה `_private/` מוחרגת מגיט (`.gitignore`), כך שמה שבתוכה לא עולה לעולם. ובכל זאת, עדיף לא לשמור בה סודות.
7. המאגר חייב להישאר **Private**.
8. הטוקנים פגים בתאריך שבחרת. לפני כן צריך להנפיק חדש, אחרת הסנכרון ייעצר.

## 9. פתרון תקלות

| בעיה | פתרון |
|---|---|
| `PULL: FAIL` / `Authentication failed` | הטוקן פג או בוטל. מנפיקים חדש (סעיף 4.2): לבוטים דרך Grok Bot, ל-Obsidian בהגדרות התוסף או בחלון ההתחברות |
| `PUSH: BLOCKED secrets found` | למחוק את הערך מהקובץ שצוין ולהריץ שוב. כלום לא עלה |
| `PUSH: FAIL ... conflict` | שני גורמים ערכו את אותה שורה. הבוט מריץ `git status`, משאיר את שתי הגרסאות, `git add -A && git rebase --continue` ומעלה שוב |
| `could not get vault lock` | בוט אחר כותב כרגע. לנסות שוב בעוד דקה |
| ב-Obsidian לא רואים עדכונים | Command palette → **Git: Pull**. לוודא ש-Auto pull מוגדר |
| התנגשות (conflict) ב-Obsidian | התוסף מסמן את הקובץ. פותחים, משאירים את שתי הגרסאות, ומריצים **Git: Commit-and-sync** |
| הטלפון קורס בשכפול | לנסות שוב עם Wi-Fi וזיכרון פנוי, או לעבור ל-GitSync / Working Copy (סעיף 4.4) |
| `WARN LINKS` אחרי שינוי שם של פתק | ב-Obsidian להפעיל Settings → Files and links → **Automatically update internal links** |

בדיקה ידנית על ה-box:

```bash
git -C /home/box/shared/obsidian-vault status -sb
git -C /home/box/shared/obsidian-vault log --oneline -5
```

## 10. שאלות נפוצות

**האם צריך את Claude Code, Node.js או התקנה כלשהי?**
לא. הכול רץ על ה-box עם python3 ו-bash שכבר קיימים. אצלך צריך רק Obsidian, התוסף Git, ובמחשב גם Git.

**מה קורה אם שני בוטים סוגרים סשן באותו רגע?**
יש נעילה. השני מחכה עד 120 שניות, עושה `pull --rebase` ואז מעלה. אם מישהו אחר העלה בינתיים, יש עד 3 ניסיונות חוזרים.

**האם בוט יכול למחוק לי פתקים?**
הכללים במיומנויות הם להוסיף ולא למחוק. גם אם משהו נמחק בטעות, הוא נשאר בהיסטוריית Git וניתן לשחזור.

**איפה רואים מה כל בוט עשה?**
ב-`Agents/<שם הבוט>.md`, או בדוח המצב בטבלת "פעילות בוטים".

**איך מוסיפים פרויקט חדש?**
אומרים לבוט "הוסף פרויקט X" (ראיון הקמה), או מעתיקים את `templates/project.md` לתיקייה `Projects/`.

**איך מוסיפים בוט חדש?**
מוסיפים את שמו לרשימת הבוטים ב-`00 Profile.md` ורושמים לו את 5 המיומנויות. היומן שלו נוצר לבד בסגירת הסשן הראשונה.

**כמה זה עולה בטוקנים?**
פתיחה היא קריאה אחת וסגירה היא 1–2 קריאות. זה תוכנן לחיסכון, כמו במקור.

**אפשר לבטל?**
כן. מבטלים את רישום המיומנויות אצל הבוטים. הכספת והפתקים נשארים שלך.

## קרדיט
מבוסס על [trestle](https://github.com/liormesh/trestle) מאת Lior Meshullam, ברישיון MIT. הטקסט המלא נמצא ב-`LICENSE-trestle-MIT.txt`.
