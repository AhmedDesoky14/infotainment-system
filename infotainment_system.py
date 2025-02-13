# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QThread, Signal, QTimer
from home_tab import home_tab
from drive_assist_tab import drive_assist_tab
from settings_tab import settings_tab
from gps_tab import gps_tab
from radio_tab import radio_tab
from media_player_tab import media_player_tab
import screens
import time

class infotainment_system:
    def __init__(self):
        #initialize QWindow, QWidgets and setup UI
        screens.main_screen = screens.infotainment_screen()
        screens.auth_screen = screens.authentication_screen()
        screens.logo_loading_screen = screens.logo_screen()
        screens.delete_confirm_box = screens.delete_box()
        #initailize classes of tabs and screens
        self.home = home_tab()
        self.drive_assist = drive_assist_tab()
        self.gps = gps_tab()
        self.radio = radio_tab()
        self.media = media_player_tab()
        self.settings = settings_tab()
        self.__init_sequence()  #start init sequence

    def __init_sequence(self):
        #call init functions
        self.__reset_all()
        self.__load_users()
        self.__set_visual_mode()
        self.__loading_screen()
        self.__authenticate()
        self.__start_main()

    #function to reset and clear every text, label and list
    def __reset_all(self):
        #reset date and time and temperature
        screens.main_screen_ui.date_label.setText("")
        screens.main_screen_ui.time_label.setText("")
        screens.main_screen_ui.temperature_value.setText("")

        self.home.set_speed(0) #set speed 0
        self.home.set_speed_limit(0) #set speed limit 0
        self.home.set_battery(100,False) #set battery to 100 and not charging
        self.home.reset_left_turn() #reset left turn
        self.home.reset_right_turn() #reset right turn
        self.home.reset_waiting() #reset waiting
        self.home.reset_collision_warning() #reset collision warning
        #reset warnings
        self.home.reset_warning(1)
        self.home.reset_warning(2)
        self.home.reset_warning(3)

        #reset driver assist tab
        self.drive_assist.reset_brakes()
        self.drive_assist.reset_backward_direction()
        self.drive_assist.reset_left_direction()
        self.drive_assist.reset_right_direction()
        self.drive_assist.reset_forward_direction()
        self.drive_assist.reset_usercamera()

        #clear users list
        screens.main_screen_ui.users_list.clear()

    #function to load all users to show into the users list
    def __load_users(self):
        """ Reads a text file and adds each line to QListWidget users list """
        with open(screens.users_list_file_path, "r", encoding="utf-8") as file:
            line = file.readlines()  # Read all lines
            screens.main_screen_ui.users_list.addItems(line)  # Add to user list in the settings window

    #function to set the visual mode at start
    def __set_visual_mode(self):
        with open(screens.visual_mode_file_path, "r") as file:
            value = file.read().strip()  # Remove extra spaces or newlines
        if (value == "0"): #Dark Mode
            settings_tab.bright_mode = False
            #set all screens in dark mode
            screens.main_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
            screens.auth_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
            screens.logo_loading_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
            screens.delete_confirm_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
            #set visual mode button as dark mode and not checked
            screens.main_screen_ui.visual_mode_button.setChecked(False)
            screens.main_screen_ui.visual_mode_button.setText("Dark Mode")
        else:   #Bright compile
            settings_tab.bright_mode = True
            #set all screens in bright mode
            screens.main_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 234, 253, 1), stop:1 rgba(188, 204, 220, 1));")
            screens.auth_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 234, 253, 1), stop:1 rgba(188, 204, 220, 1));")
            screens.logo_loading_screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 234, 253, 1), stop:1 rgba(188, 204, 220, 1));")
            screens.delete_confirm_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 234, 253, 1), stop:1 rgba(188, 204, 220, 1));")
            #set visual mode button as bright mode and not checked
            screens.main_screen_ui.visual_mode_button.setChecked(True)
            screens.main_screen_ui.visual_mode_button.setText("Bright Mode")

    def __loading_screen(self):
        self.loading_thread = Loading_thread()
        self.loading_thread.progress_updated.connect(screens.logo_screen_ui.progressBar.setValue)
        self.loading_thread.loading_complete.connect(self.__on_loading_complete)
        #show all screens but logo loading on top
        screens.main_screen.showFullScreen()
        screens.auth_screen.showFullScreen()
        screens.logo_loading_screen.showFullScreen()
        #open all tabs then get back to first tab
        screens.main_screen_ui.screen_tabs.setCurrentIndex(1)
        screens.main_screen_ui.screen_tabs.setCurrentIndex(2)
        screens.main_screen_ui.screen_tabs.setCurrentIndex(3)
        screens.main_screen_ui.screen_tabs.setCurrentIndex(4)
        screens.main_screen_ui.screen_tabs.setCurrentIndex(5)
        screens.main_screen_ui.screen_tabs.setCurrentIndex(0)
        self.loading_thread.start()    #start the thread

    #Slot function called when loading the application is complete
    def __on_loading_complete(self):
        screens.logo_screen_ui.loading_label.setStyleSheet("color: rgb(46, 194, 126);")
        screens.logo_screen_ui.loading_label.setText("Welcome!")
        QTimer.singleShot(1000, screens.logo_loading_screen.close)  # 1s delay before closing

    #login authentication function
    def __authenticate(self):
        #left to be implemented for face recognition integration
        #do authentication
        screens.auth_screen.close()

    def __start_main(self):
        """====================================================================================================
            Main function, after initailzation every thing happens starting from here
        ===================================================================================================="""



#QThread child class to run specific task which is simulate loading
class Loading_thread(QThread):
    progress_updated = Signal(int)  # Signal to update progress
    loading_complete = Signal()
    def run(self):
        for i in range(101):  # 0 to 100
            time.sleep(0.025)  # (sleep for 25ms) to simulate loading
            self.progress_updated.emit(i)  # Emit progress
        self.loading_complete.emit()  # Emit "loading_complete" signal when finished






