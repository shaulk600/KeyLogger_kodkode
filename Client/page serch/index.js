
// נערך בתאריך 26.02.2025
// נערך על ידי שאול קימל

// JavaScript can be used create variably in the head page
// and can be used in the page body 

// הצהרת משתנים
// Variables

let searchOn = false;
let welcomeText = " היי משתמש אורח ";

// הצהרת פונקציות
// Functions


// הצהרת משתנה - ערך הכותרת 
// Set welcome title
// מקבל את ערכו של הכותרת welcomeText בשורה הזו משתנה 
document.getElementById('welcomeTitle').textContent = welcomeText;

// הצהרת פעולת 
// on_click
// על כפתור "חזור למסך הבית"
// Button Event Listeners
document.getElementById('returnHome').addEventListener('click', function() {
    // לרשום כאן
    console.log("חזרה לדף הבית");
});

// הצהרת פעולת 
// on_click
// על כפתור "חיפוש"
document.getElementById('searchBtn').addEventListener('click', function() {
    
    // לרשום כאן
    
    console.log("ביצוע חיפוש");
    // הפיכת משתנה 
    // searchOn
    //  מכבוי לפועל(ערך אמת)
    searchOn = true;

    // הצגת תוצאות חיפוש
    // Display -הצגת תוצאות חיפוש 
    // - בעצם הצגת הטבלה בדף 
    // HTML (לא הדף הנפרד - אלא הטבלה בדף)
    // סדר הפעולות בעת הצגת הטבלה כדלקמן :

    // משתנה "אזור הטבלה המוסתרת "-להפוך אותו כשהוא מוצג
    document.getElementById('tableContainer').style.display = 'block';
    
    // העלמת ערך מה שהיה עד לפני הטבלה - חלק 2 באותו div
    document.getElementById('tablePlaceholder').style.display = 'none';
    
    // אוכלוסיית נתונים לדוגמא
    // Sample data population
    
    // שכחתי לשניה מה זה ||
    // זה OR

    // ממה שאני מבין - או שזה דומה למה שיש בטבלה או ערך דיפולטיבי יוגדר כמשתנה ה... = כל זה הצהרת משתני קבע
    const computerName = document.getElementById('computerName').value || "UNKNOWN";
    const searchDate = document.getElementById('searchDate').value || "2025-02-26";
    const searchTime = document.getElementById('searchTime').value || "12:00";
    
    //  עידכון הטבלה בדף -תוך דריסה של הערך הקודם (הערך שאמר שאין כלום בטבלה) 
    
    // Add sample result
    document.getElementById('resultsTable').innerHTML = `
        <tr>
            <td>1</td>
            <td>${computerName}</td>
            <td>${searchDate}</td>
            <td>${searchTime}</td>
            <td>פעיל</td>
        </tr>
    `;
// סיום פונקציית חיפוש
});
    

    // חומר העשרה
    // לחילופין - אם מדובר בערך שהוא תלוי במספר נתונים
    // (כמו מספר שורות - וצריך להוסיף אליהם עוד שורה -
    //  ניתן לעשות את הקוד הבא - שעושה 
    // append ולא write)
    // 
    // document.getElementById('resultsTable').insertAdjacentHTML('beforeend', `
    //     <tr>
    //         <td>1</td>
    //         <td>${computerName}</td>
    //         <td>${searchDate}</td>
    //         <td>${searchTime}</td>
    //         <td>פעיל</td>
    //     </tr>
    // `
    // );


// הצהרת פעולת 
// on_click
// על כפתור "הורדה לקובץ"
document.getElementById('downloadBtn').addEventListener('click', function() {
    // לרשום כאן
    console.log("הורדה לקובץ");
});

//הצהרת פעולת 
// on_click
// על כפתור "טעינת רשימת מחשבים"
document.getElementById('loadComputers').addEventListener('click', function() {
    // לרשום כאן
    console.log("טעינת רשימת מחשבים");

    // הצגת חלון מודלי (חלון נפרד נקרא חלון מודלי) עם רשימת מחשבים
    // Display modal with computer list
    document.getElementById('computerListModal').style.display = 'block';
});


// הצהרת פעולת 
// on_click
// על כפתור "יציאה מהמערכת"
document.getElementById('exitBtn').addEventListener('click', function() {
    // לרשום כאן
    console.log("יציאה מהמערכת");
});

// הסבר קצר לגבי הפונקציה הבאה:
// בעת פתיחת חלון מודלי יש איזשהו כפתור למעלה שמסמן
// 'X'
//  ובעת לחיצה עליו החלון נסגר
// אז זה הקוד של הכפתור - שהופך את התצוגה של הטבלה ל
// none - מוסתרת

// חלון מודולי - סגירה שלו
// Close modal when clicking X
document.querySelector('.close-btn').addEventListener('click', function() {
    document.getElementById('computerListModal').style.display = 'none';
});

// חלון מודולי - סגירה שלו - בדומה לפונקציה הקודמת
// רק שהפאנץ' פה זה אם אתה לוחץ מחוץ לחלון ולא על 
// 'X'
//  החלון יסגר

// Close modal when clicking outside
window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('computerListModal')) {
        document.getElementById('computerListModal').style.display = 'none';
        
    }
});