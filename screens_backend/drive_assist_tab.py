# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer
from PySide6.QtGui import  QPixmap
import screens

class drive_assist_tab:
    def __init__(self):
        self.__collision_timer = QTimer()
        self.__collision_toggler = False

        pass

    #set frame to the user camera view
    def set_frame(self):
        pass    #left to be implemented for OpenCV integration

    #clear the user camera view
    def reset_usercamera(self):
        screens.main_screen_ui.usercamera_view.setPixmap(QPixmap())
        screens.main_screen_ui.usercamera_view.setStyleSheet("") # Remove all styles

    """---
        directions icons set and reset for driving assist tab
    ---"""
    def set_brakes(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/brake.png"))
    def reset_brakes(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap())
    def set_right_direction(self):
        screens.main_screen_ui.right_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_right.png"))
    def reset_right_direction(self):
        screens.main_screen_ui.right_icon.setPixmap(QPixmap())
    def set_left_direction(self):
        screens.main_screen_ui.left_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_left.png"))
    def reset_left_direction(self):
        screens.main_screen_ui.left_icon.setPixmap(QPixmap())
    def set_forward_direction(self):
        screens.main_screen_ui.foreward_icon.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/greed_forward.png"))
    def reset_forward_direction(self):
        screens.main_screen_ui.foreward_icon.setPixmap(QPixmap())
    def set_backward_direction(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap(u":/drive_assist/icons/drive_assist/green_backward.png"))
    def reset_backward_direction(self):
        screens.main_screen_ui.warningx.setPixmap(QPixmap())
