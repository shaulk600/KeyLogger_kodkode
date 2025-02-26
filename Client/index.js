async function validateLogin(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const dateTime = document.getElementById('date-time').value;

    const data = {
        machine: username,
        date_time: dateTime,
        data: "הקלדה מוצגת כאן"
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/api/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            console.log("Data uploaded successfully:", result);

            // שמירת הנתונים ב-localStorage
            localStorage.setItem('machine', username);
            localStorage.setItem('date_time', dateTime);

            // מעבר לדף הראשי
            window.location.href = 'main.html';
        } else {
            alert("שגיאה בהעברת הנתונים.");
        }
    } catch (error) {
        console.error("שגיאה בהתחברות:", error);
        alert('אירעה שגיאה בהתחברות. אנא נסו שוב מאוחר יותר.');
    }

    return false;
}
