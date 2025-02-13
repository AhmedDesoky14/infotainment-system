# This Python file uses the following encoding: utf-8
import screens

class settings_tab:
    def __init__(self):
        self.bright_mode = False #boolean to check whether a bright mode or dark mode
        screens.main_screen_ui.visual_mode_button.toggled.connect(self.__toggle_mode)
        screens.main_screen_ui.check_updates_button.clicked.connect(self.__on_updates_clicked)
        screens.main_screen_ui.check_updates_button.clicked.connect(self.__on_updates_clicked)
        screens.main_screen_ui.adduser_button.clicked.connect(self.__on_add_user)
        screens.main_screen_ui.deleteuser_button.clicked.connect(self.__on_delete_user)

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

    #slot function to add new user for the vehicle system
    def __on_add_user(self):
        #left to be implemented for face recognition integration
        screens.auth_screen.showFullScreen()
        #do add user
        screens.auth_screen.close()

    #slot function to remove a user from the vehicle system
    def __on_delete_user(self):
        selected_item = screens.main_screen_ui.users_list.currentRow()
        if (selected_item != -1):  # Check if an item is selected
            screens.delete_confirm_box.showFullScreen()

    #slot function to update
    def __on_updates_clicked(self):
        pass #left to be implemented for updates sequence

    #slot function to set temperature for the vehicle
    def __on_set_temperature(self):
        pass #left for implementation to set temperature
