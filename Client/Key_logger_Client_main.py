<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>התחברות למערכת</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>Keylogger</h1>
            <h3>אנא הזינו את הפרטים הנצרכים</h3>
        </div>
        <form id="loginForm" onsubmit="return validateLogin(event)">
            <div class="form-group">
                <label for="username">שם מחשב</label>
                <input type="text" id="username" name="username" required>
                <div class="error-message" id="usernameError">שם משתמש לא תקין</div>
            </div>
            <div class="form-group">
                <label for="date-time">תאריך ושעה</label>
                <input type="datetime-local" id="date-time" name="date-time" required>
                <div class="error-message" id="dateTimeError">תאריך ושעה לא תקינים</div>
            </div>
            <button type="submit" class="login-btn">התחבר</button>
        </form>
    </div>

    <script src="index.js"></script>
</body>
</html>
