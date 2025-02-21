
// חשוב מאוד !! לעשות בדיקות אבטחה = קוד מAI

// הצהרת משתנים קבועים

// התחלת תהליך : יצרתי לשם של הכותרת משתנה שאנחנו נגדיר מה יהיה כתוב שם במקום ברוכים הבאים

const nameOfTitle = document.getElementById('name-of-title'); 
const userNameInput = document.getElementById('user-name-input');
const submitNameButton = document.getElementById('submit-name');
// 
// בעצם לוקח פונקציה שמאזין לclickעל השם ומעדכן את הכותרת - אני רוצה ליצור משתנה שיקח מהדף הקודם בעת טעינת הדף את הערך החסר וישים אותו במשתנה של הכותרת  ! סוף פיסקא הסבר על התהליך ב5 שורות הבאות למרות שנמחק את זה בהמשך ונמצא דרך יותר טובה
submitNameButton.addEventListener('click', () => {
    const userName = userNameInput.value;
    if (userName) {
        nameOfTitle.textContent = `Welcome, ${userName}`;
    }
});



let currentOpenMenu = null;

function toggleSubMenu(menuId) {
    const menu = document.getElementById(menuId);
    
    // סגירת תפריט קודם אם פתוח
    if (currentOpenMenu && currentOpenMenu !== menu) {
        currentOpenMenu.style.display = 'none';
    }

    // החלפת מצב התפריט הנוכחי
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
        currentOpenMenu = null;
    } else {
        menu.style.display = 'block';
        currentOpenMenu = menu;
    }
}

// סגירת תפריטים בלחיצה מחוץ לאזור
document.addEventListener('click', (event) => {
    if (!event.target.closest('.sidebar-main')) {
        if (currentOpenMenu) {
            currentOpenMenu.style.display = 'none';
            currentOpenMenu = null;
        }
    }
});
