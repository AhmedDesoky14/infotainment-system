import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from infotainment_screen_ui import Ui_MainWindow 
from back_end.media_player import MediaPlayerApp
from back_end.gps import GPSapp
from back_end.radio import RadioApp

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.media_player = MediaPlayerApp(self.ui)
        self.gps = GPSapp(self.ui)
        self.radio = RadioApp(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

