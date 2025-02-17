# This Python file uses the following encoding: utf-8
import screens
from PySide6.QtCore import Slot
from b_add_user_remove_user import User_account  # Import your FaceRecognition class
import random
from PySide6 import QtWidgets
import sys
import os
from PySide6.QtCore import Signal, Slot, QObject
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
class settings_tab(QObject):
    user_added_signal = Signal()  # Define a custom signal
    def __init__(self):
        super().__init__()
        self.bright_mode = False #boolean to check whether a bright mode or dark mode
        screens.main_screen_ui.visual_mode_button.toggled.connect(self.__toggle_mode)
        screens.main_screen_ui.check_updates_button.clicked.connect(self.__on_updates_clicked)
        screens.main_screen_ui.check_updates_button.clicked.connect(self.__on_updates_clicked)
        screens.main_screen_ui.adduser_button.clicked.connect(self.__on_add_user)
        screens.main_screen_ui.deleteuser_button.clicked.connect(self.__on_delete_user)
        #screens.delete_box.response_received.connect(self.__on_delete_user)
        self.user_account = User_account(camera_index=0)
        

    #Slot function to change visual mode of the window
    def __toggle_mode(self,checked):
        if checked: #set bright mode
            self.bright_mode = True
            screens.main_screen_ui.visual_mode_button.setText("Bright Mode")
            with open(screens.visual_mode_file_path, "w") as file:
                file.write("1")
            screens.main_screen_ui.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 234, 253, 1), stop:1 rgba(188, 204, 220, 1));")
        else: #set dark mode
            self.bright_mode = False
            screens.main_screen_ui.visual_mode_button.setText("Dark Mode")
            with open(screens.visual_mode_file_path, "w") as file:
                file.write("0")
            screens.main_screen_ui.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")



    def __generate_id(self):
        return str(random.randint(10000, 99999))  # Ensures a 5-digit number

    #slot function to add new user for the vehicle system
    # @Slot()
    # def __on_add_user(self):
    #     """
    #     Slot function to add a new user to the vehicle system.
    #     """
    #     id_number = self.__generate_id()
    #     if id_number:
    #         result = self.user_account.add_user_by_photo_name(id_number)
    #         if result == 1:
    #             print(f"User '{id_number}' added successfully.")
    #             self.user_added_signal.emit()
    #         else:
    #             print(f"Failed to add user '{id_number}'.")

    @Slot()
    def __on_add_user(self):
        """
        Slot function to add a new user to the vehicle system.
        """
        id_number = self.__generate_id()
        if id_number:
            result = self.user_account.add_user_by_photo_name(id_number)
            if result == 1:
                print(f"User '{id_number}' added successfully.")
                self.user_added_signal.emit()
            else:
                print(f"Failed to add user '{id_number}'.")
                self.__show_warning()


    def __show_warning(self):
        """
        Displays a warning message with instructions for 5 seconds and then closes automatically.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("⚠ User Registration Failed")

        # Warning message with instructions
        message = (
            "<b>Failed to add user! Please ensure the following:</b><br><br>"
            "<ul>"
            "<li><b>Be alone</b> in front of the camera.</li>"
            "<li>Ensure <b>good lighting</b> and a <b>clear face</b>.</li>"
            "<li>Avoid <b>blurry</b> or <b>low-resolution</b> images.</li>"
            "<li>Remove <b>masks, hats, or anything covering your face</b>.</li>"
            "</ul>"
            "<br><b>🔄 Try again with better conditions.</b>"
        )


        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        
        # Set a larger size for better readability
        msg_box.setMinimumSize(720, 720)  

        # Close the message box after 5 seconds
        QTimer.singleShot(7000, msg_box.close)

        msg_box.exec()



    @Slot()
    def __on_delete_user(self):

        """
        Slot function to remove a user from the vehicle system.
        """
        selected_item = screens.main_screen_ui.users_list.currentItem()

        if (selected_item != -1):  # Check if an item is selected
            screens.delete_confirm_box.showFullScreen()
            selected_name = selected_item.text()
            result = self.user_account.remove_user(selected_name)
            if result == 1:
                print(f"removed user '{selected_name}'.")
            else:
                print(f"Failed to remove user '{selected_name}'.")






    

    #slot function to update
    def __on_updates_clicked(self):
        pass #left to be implemented for updates sequence

    #slot function to set temperature for the vehicle
    def __on_set_temperature(self):
        pass #left for implementation to set temperature

