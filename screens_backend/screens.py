# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QMainWindow, QWidget)
from ui_infotainment_screen import Main_Screen_UI
from ui_loadig_logo import Logo_Window
from ui_adduser_authentication import Authentcation_Window
from ui_delete_confirm import DeleteBox

visual_mode_file_path = "UI_Python/bright_dark.txt"
users_list_file_path = "./credentials/users_list.txt"

main_screen_ui = None #Main screen UI
authentication_screen_ui = None #Authentication screen UI
logo_screen_ui = None #Logo screen UI
delete_box_ui = None #Delete User Confirm Box

main_screen = None #Main QWindow
auth_screen = None #QWidget responsible for authentication
logo_loading_screen = None #Loading Logo QWidget
delete_confirm_box = None #Delete confirm box QWidget
"""==================================================
    Screens classes
==================================================="""

class infotainment_screen(QMainWindow): #inherit from QMainWindow class
    def __init__(self):
        super().__init__() #call "QMainWindow" constructor explicitly
        global main_screen_ui
        main_screen_ui = Main_Screen_UI()
        main_screen_ui.setupUi(self)

class authentication_screen(QWidget): #inherit from QWidget class
    def __init__(self):
        super().__init__() #call "QWidget" constructor explicitly
        global authentication_screen_ui
        authentication_screen_ui = Authentcation_Window()
        authentication_screen_ui.setupUi(self)

class logo_screen(QWidget): #inherit from QWidget class
    def __init__(self):
        super().__init__() #call "QWidget" constructor explicitly
        global logo_screen_ui
        logo_screen_ui = Logo_Window()
        logo_screen_ui.setupUi(self)

class delete_box(QWidget):
    def __init__(self):
        super().__init__() #call "QWidget" constructor explicitly
        global delete_box_ui
        delete_box_ui = DeleteBox()
        delete_box_ui.setupUi(self)
        #connect push buttons
        delete_box_ui.yes_delete_button.clicked.connect(self.on_yes)
        delete_box_ui.no_delete_button.clicked.connect(self.on_no)

    #slot function when yes is clicked
    def on_yes(self):
            selected_item = main_screen_ui.users_list.currentRow()
            main_screen_ui.users_list.takeItem(selected_item)
            delete_confirm_box.close()

    #slot function when no is clicked
    def on_no(self):
            delete_confirm_box.close() #do nothing
