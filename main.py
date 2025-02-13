# This Python file uses the following encoding: utf-8
import os, sys
# Get the absolute path of the UI_Python directory
ui_python_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "UI_Python"))
# Get the absolute path of the screens_backend directory
screens_backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "screens_backend"))
# Add to search path
sys.path.append(ui_python_path)
sys.path.append(screens_backend_path)

from PySide6.QtWidgets import QApplication
from home_tab import home_tab
from home_tab import WARNINGS_LIST
from drive_assist_tab import drive_assist_tab
from settings_tab import settings_tab
from gps_tab import gps_tab
from radio_tab import radio_tab
from media_player_tab import media_player_tab
import screens

#main class containing all instances of screens and UIs and init sequence
from infotainment_system import infotainment_system

if __name__ == "__main__":
    app = QApplication(sys.argv)

    system = infotainment_system()

    sys.exit(app.exec())



