
async function validateLogin(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        // כאן תהיה הקריאה לקובץ ה-database
        const response = await fetch('רשום את נתיב הקובץ database כאן');
        const data = await response.json();
        
        // בדיקת התאמת הפרטים
        const user = data.users.find(u => u.username === username && u.password === password);
        
        if (user) {
            // התחברות מוצלחת - מעבר לדף הראשי
            window.location.href = 'רשום את נתיב הדף main כאן';
        } else {
            // הצגת הודעת שגיאה
            document.getElementById('usernameError').style.display = 'block';
            document.getElementById('passwordError').style.display = 'block';
        }
    } catch (error) {
        console.error('שגיאה בהתחברות:', error);
        alert('אירעה שגיאה בהתחברות. אנא נסו שוב מאוחר יותר.');
    }
    
    return false;
}
