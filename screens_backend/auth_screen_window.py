# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtGui import  QPixmap
from enum import Enum
import screens

class TEXT_COLOR(Enum):
    RED = """QLabel
    {
            color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            color: rgb(192, 28, 40);
    }"""

    YELLOW = """QLabel
    {
            color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            color: rgb(246, 211, 45);
    }"""

    GREEN = """QLabel
    {
            color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;
            color: rgb(38, 162, 105);
    }"""

class auth_screen_window:
    def __init__(self):
        self.__date_time_timer = QTimer()
        #connect timer timeout signal to "update_date_time" slot
        self.__date_time_timer.timeout.connect(self.__update_date_time)
        self.__date_time_timer.start(1000)  # Update time every second
        screens.authentication_screen_ui.auth_button.clicked.connect(self.__on_auth_button_click)
        self.authentication_flag = False #global variable to be checked and set to False upon authentication

    #slot function, to update time and date on screen
    def __update_date_time(self):
        """Update the home page with current date and time."""
        current_date_time = QDateTime.currentDateTime()
        formatted_date = current_date_time.toString("MMM. dd, yyyy")
        screens.authentication_screen_ui.date_label.setText(f"Date: {formatted_date}")
        screens.authentication_screen_ui.time_label.setText(f"Time: {current_date_time.toString('hh:mm:ss')}")

    #slot function for clicking the authentication button, it raises the flag by 1 to allow face recognition sequence
    def __on_auth_button_click(self):
        if (authentication_flag == False):
            authentication_flag = True


    #function to set text to auth text label
    def set_auth_text(self,text,color: TEXT_COLOR):
        screens.authentication_screen_ui.auth_text_label.setText(text)
        screens.authentication_screen_ui.auth_text_label.setStyleSheet(color.value)

    #function to reset text of auth text label
    def reset_auth_text(self):
        screens.authentication_screen_ui.auth_text_label.setText()
        screens.authentication_screen_ui.auth_text_label.setStyleSheet()

    #function to set text of auth button label
    def set_auth_button_text(self,text):
        screens.authentication_screen_ui.auth_button.setText(text)

    #function to reset text of auth button label
    def reset_auth_button_text(self):
        screens.authentication_screen_ui.auth_button.setText()
