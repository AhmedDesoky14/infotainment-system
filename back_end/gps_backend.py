import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QSizePolicy, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from infotainment_screen_ui import Ui_MainWindow

class GPSapp:
    def __init__(self, main_ui):
        self.ui = main_ui 

        # Locate GPS tab in infotainment UI
        self.gps_tab = self.ui.screen_tabs.findChild(QWidget, "gps_tab")
        
        # Create WebEngineView inside the GPS tab
        self.web_view = QWebEngineView(self.gps_tab)
        self.web_view.setGeometry(0, 0, self.gps_tab.width(), self.gps_tab.height())
        
        # Ensure the GPS tab uses a layout
        self.gps_tab.setLayout(QVBoxLayout())

        # Remove margins and spacing to allow full expansion
        self.gps_tab.layout().setContentsMargins(0, 0, 0, 0)
        self.gps_tab.layout().setSpacing(0)

        # Apply the correct size policy
        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add web view to layout
        self.gps_tab.layout().addWidget(self.web_view)
            
        self.load_google_maps()

    def load_google_maps(self):
        google_maps_url = "https://www.google.com/maps"
        self.web_view.setUrl(QUrl(google_maps_url))
        self.web_view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = GPSapp(Ui_MainWindow())  # Pass the main infotainment UI
    main_window.show()
    sys.exit(app.exec())

