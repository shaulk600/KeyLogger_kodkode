async function validateLogin(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const dateTime = document.getElementById('date-time').value;

    const data = {
        machine: username,  // משדרים את שם המשתמש כ"machine"
        date_time: dateTime, // תאריך ושעה
        //data: "הקלדה מוצגת כאן" // זוהי ההקלדה שלך, תוכל להוסיף אותו מתוך הנתונים שאתה מקבל
    };


//    try {
//        // קריאה לשרת באמצעות fetch
//        url = 'http://127.0.0.1:5000/api/get_target_machines_key_strokes'
//        const response = await fetch(url, {
//            method: 'GET',
//            headers: {
//                "machine" : username ,
//                "time" : date_time
//            },
//            body: JSON.stringify(data)
//        });
//
//        if (response.ok) {
//            const result = await response.json();
//            console.log("Data uploaded successfully:", result);
//            //אני מפנה אותו לחלון חדש שיפתח
//            window.location.href = 'main.html';
//            alert("הנתונים הועברו בהצלחה!");
//        } else {
//            alert("שגיאה בהעברת הנתונים.");
//        }
//    } // end try
//    catch (error) {
//        console.error("שגיאה בהתחברות:", error);
//        alert('אירעה שגיאה בהתחברות. אנא נסו שוב מאוחר יותר.');
//    } // end catch
//
//    return false;
//} // end func




// לא למחוק - מיועד לבדיקות אבטחה

    try {
        // קריאה לשרת באמצעות fetch
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
            alert("הנתונים הועברו בהצלחה!");
        } else {
            alert("שגיאה בהעברת הנתונים.");
        }
    } catch (error) {
        console.error("שגיאה בהתחברות:", error);
        alert('אירעה שגיאה בהתחברות. אנא נסו שוב מאוחר יותר.');
    }








