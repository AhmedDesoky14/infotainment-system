# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtGui import  QPixmap
from enum import Enum
import screens

"""==================================================
    Warnings List Enum
==================================================="""
class WARNINGS_LIST(Enum):
    STOP = "stop.png"
    WARNING = "warning"
    TRAFFIC_LIGHTS = "traffic-lights.png"
    TWO_WAY = "two-way-street.png"
    NO_PARKING = "no-parking.png"
    PEDESTERIANS = "pedestrian-crossing.png"
    FORBIDDEN = "forbidden.png"
    UNEVEN_ROAD = "uneven.png"
    SLIPPERY = "slippery-road.png"
    UNDER_CONSTRUCTION = "road.png"


class home_tab:
    def __init__(self):
        """
            Class object variables
        """
        self.__speed_warning_toggler = False #used for flickering speed limit warning.
        self.__is_turn_waiting_on = False #used for car signals of turn left/right or waiting
        screens.main_screen_ui.speedlimit_button.toggled.connect(self.__on_speed_toggle)
        self.__date_time_timer = QTimer()
        self.__turning_timer = QTimer()
        self.__speed_limit_timer = QTimer()
        self.__collision_timer = QTimer()
        self.__speed_limit_timer.timeout.connect(self.__on_speed_limit_toggle) #connect timer timeout signal to "on_speed_limit_toggle" slot
        self.__date_time_timer.timeout.connect(self.__update_date_time)   #connect timer timeout signal to "update_date_time" slot
        self.__date_time_timer.start(1000)  # Update time every second

    #slot function, to update time and date on screen
    def __update_date_time(self):
        """Update the home page with current date and time."""
        current_date_time = QDateTime.currentDateTime()
        formatted_date = current_date_time.toString("MMM. dd, yyyy")
        screens.main_screen_ui.date_label.setText(f"Date: {formatted_date}")
        screens.main_screen_ui.time_label.setText(f"Time: {current_date_time.toString('hh:mm:ss')}")

    # set speed on screen
    def set_speed(self,speed):
        self.current_speed = speed
        screens.main_screen_ui.home_speed_2.setText(f"{speed} KM/hr")

    #slot function, to set the control variable to True if checked, False if not
    def __on_speed_toggle(self,checked): #slot function
        #if button checked, speed set point is changed and speed control is in charge
        if checked:
            self.speed_control = True
        else:
            self.speed_control = False

    #To show road's speed limit on the screen
    def set_speed_limit(self,speed_limit):
        self.speed_limit = speed_limit
        screens.main_screen_ui.speed_limit.setText(f"Limit\n{speed_limit}\nKM/hr")
        if(self.speed_limit > 0): #there's a speed limit
            self.__speed_limit_timer.start(250)
        else:
            self.__speed_limit_timer.stop()

    #Slot function, to toggle showing the speed limit icon to the driver
    def __on_speed_limit_toggle(self):
        if (self.current_speed > self.speed_limit):
            if self.__speed_warning_toggler:  #toggle the variable
                self.__speed_warning_toggler = False
                screens.main_screen_ui.speed_limit_warning.setPixmap(QPixmap())
            else:
                self.__speed_warning_toggler = True
                if(self.speed_limit > 130):
                    popup_path = ":/speed_limits/popups/speed_limits/+130.png"
                else:
                    popup_path = f":/speed_limits/popups/speed_limits/{self.speed_limit}.png"
                screens.main_screen_ui.speed_limit_warning.setPixmap(QPixmap(popup_path))

        else:
            screens.main_screen_ui.speed_limit_warning.setPixmap(QPixmap())

    #Set temperature on screen
    def set_temperature(self,temp):
        self.current_temperature = temp
        screens.main_screen_ui.temperature_value.setText(f"{temp} C")

    #Set battery and battery status on screen
    def set_battery(self,percentage,charging):
        self.current_percentage = percentage
        self.is_charging = charging
        screens.main_screen_ui.battery_value.setText(f"{percentage} %")
        if (charging):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/charging.png"))
            return  #show charging
        if (percentage == 100 and percentage > 95):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/100%.png"))
        elif (percentage < 95 and percentage >= 75):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/80%.png"))
        elif (percentage < 75 and percentage >= 55):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/60%.png"))
        elif (percentage < 55 and percentage >= 30):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/40%.png"))
        elif (percentage < 30 and percentage >= 5):
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/20%.png"))
        else: #battery is 0%
            screens.main_screen_ui.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/0%.png"))

    #start setting turnning left icon
    def set_left_turn(self):
        if(self.__is_turn_waiting_on):
            return  #do nothing, the signal running must stop
        self.__turning_timer.timeout.connect(self.__on_left)   #connect timer timeout signal to "on_left" slot
        screens.main_screen_ui.turn_left.setPixmap(QPixmap(u":/turning/icons/turning/turn_left.png"))
        self.__turning_timer.start(500)
        self.__toggler = True
        self.__is_turn_waiting_on = True

    #Slot function, after timer's timeout toggle the car signal, for turning left
    def __on_left(self):
        if(self.__toggler):
            screens.main_screen_ui.turn_left.setPixmap(QPixmap()) #set empty
            self.__toggler = False
        else:
            screens.main_screen_ui.turn_left.setPixmap(QPixmap(u":/turning/icons/turning/turn_left.png"))
            self.toggler = True

    def reset_left_turn(self):
        screens.main_screen_ui.turn_left.setPixmap(QPixmap()) #set empty
        self.__toggler = False
        self.__turning_timer.stop()

    #start setting turnning right icon
    def set_right_turn(self):
        if(self.__is_turn_waiting_on):
            return  #do nothing, the signal running must stop
        self.__turning_timer.timeout.connect(self.__on_right)   #connect timer timeout signal to "on_right" slot
        screens.main_screen_ui.turn_right.setPixmap(QPixmap(u":/turning/icons/turning/turn_right.png"))
        self.__turning_timer.start(500)
        self.__toggler = True
        self.__is_turn_waiting_on = True

    #Slot function, after timer's timeout toggle the car signal, for turning right
    def __on_right(self):
        if(self.__toggler):
            screens.main_screen_ui.turn_right.setPixmap(QPixmap()) #set empty
            self.__toggler = False
        else:
            screens.main_screen_ui.turn_right.setPixmap(QPixmap(u":/turning/icons/turning/turn_right.png"))
            self.__toggler = True

    def reset_right_turn(self):
        screens.main_screen_ui.turn_right.setPixmap(QPixmap()) #set empty
        self.__toggler = False
        self.__turning_timer.stop()

    #start setting waiting icons
    def set_waiting(self):
        if(self.__is_turn_waiting_on):
            self.reset_left_turn()  #stop left signal
            self.reset_right_turn() #stop right signal
        self.__turning_timer.timeout.connect(self.__on_waiting)   #connect timer timeout signal to "on_waiting" slot
        screens.main_screen_ui.turn_left.setPixmap(QPixmap(u":/turning/icons/turning/turn_left.png"))
        screens.main_screen_ui.turn_right.setPixmap(QPixmap(u":/turning/icons/turning/turn_right.png"))
        self.__turning_timer.start(500)
        self.__toggler = True
        self.__is_turn_waiting_on = True

    #Slot function, after timer's timeout toggle the car signal, for turning right
    def __on_waiting(self):
        if(self.__toggler):
            screens.main_screen_ui.turn_left.setPixmap(QPixmap()) #set empty
            screens.main_screen_ui.turn_right.setPixmap(QPixmap()) #set empty
            self.__toggler = False
        else:
            screens.main_screen_ui.turn_left.setPixmap(QPixmap(u":/turning/icons/turning/turn_left.png"))
            screens.main_screen_ui.turn_right.setPixmap(QPixmap(u":/turning/icons/turning/turn_right.png"))
            self.__toggler = True

    def reset_waiting(self):
        screens.main_screen_ui.turn_left.setPixmap(QPixmap()) #set empty
        screens.main_screen_ui.turn_right.setPixmap(QPixmap()) #set empty
        self.__toggler = False
        self.__turning_timer.stop()

    #Set warning or road sign icon in warning index, from index 1 to 3
    def set_warning(self,warning: WARNINGS_LIST,icon_num):
        icon_path = f":/road_signs/popups/road_signs/{warning.value}"
        match icon_num:
            case 1:
                screens.main_screen_ui.warning_icon1.setPixmap(QPixmap(icon_path))
            case 2:
                screens.main_screen_ui.warning_icon2.setPixmap(QPixmap(icon_path))
            case 3:
                screens.main_screen_ui.warning_icon3.setPixmap(QPixmap(icon_path))

    #clear icon index
    def reset_warning(self,icon_num):
        match icon_num:
            case 1:
                screens.main_screen_ui.warning_icon1.setPixmap(QPixmap())
            case 2:
                screens.main_screen_ui.warning_icon2.setPixmap(QPixmap())
            case 3:
                screens.main_screen_ui.warning_icon3.setPixmap(QPixmap())

    #set warning collision
    def set_collision_warning(self):
        self.__collision_icon_toggler = True
        self.__collision_timer.timeout.connect(self.__on_collision)
        self.__collision_timer.start(150)

    #Slot function, called when the "__collision_timer" timer is timeout
    def __on_collision(self):
        if(self.__collision_icon_toggler):
            screens.main_screen_ui.warning_icon4.setPixmap(QPixmap(u":/collision/popups/collision.png"))
            screens.main_screen_ui.collision_warning.setPixmap(QPixmap(u":/collision/popups/collision.png"))
            self.__collision_icon_toggler = False
        else:
            screens.main_screen_ui.warning_icon4.setPixmap(QPixmap())
            screens.main_screen_ui.collision_warning.setPixmap(QPixmap())
            self.__collision_icon_toggler = True

    #reset collision warning icon
    def reset_collision_warning(self):
        self.__collision_timer.stop()
        self.__collision_icon_toggler = False
        screens.main_screen_ui.warning_icon4.setPixmap(QPixmap())
        screens.main_screen_ui.collision_warning.setPixmap(QPixmap())

    #set frame to the user camera view
    def set_frame(self):
        pass    #left to be implemented for OpenCV integration

    #clear the user camera view
    def reset_frontcamera(self):
        screens.main_screen_ui.front_camera_view.setPixmap(QPixmap())
        screens.main_screen_ui.front_camera_view.setStyleSheet("") # Remove all styles
