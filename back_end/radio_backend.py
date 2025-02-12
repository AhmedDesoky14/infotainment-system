import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QSizePolicy, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from infotainment_screen_ui import Ui_MainWindow

class RadioApp(QMainWindow):
    def __init__(self, main_ui):
        super().__init__()
        self.ui = main_ui
        self.ui.setupUi(self)

        # Locate Radio tab in infotainment UI
        self.radio_tab = self.ui.screen_tabs.findChild(QWidget, "radio_tab")
        
        # Create WebEngineView inside the Radio tab
        self.web_view = QWebEngineView(self.radio_tab)
        self.web_view.setGeometry(0, 0, self.radio_tab.width(), self.radio_tab.height())
        
        # Ensure the radio tab uses a layout
        self.radio_tab.setLayout(QVBoxLayout())

        # Remove margins and spacing to allow full expansion
        self.radio_tab.layout().setContentsMargins(0, 0, 0, 0)
        self.radio_tab.layout().setSpacing(0)

        # Apply the correct size policy
        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add web view to layout
        self.radio_tab.layout().addWidget(self.web_view)
            
        self.load_radio()

    def load_radio(self):
        radio_url = "https://radio.garden/visit/cairo/vtWTDbUW"
        self.web_view.setUrl(QUrl(radio_url))
        self.web_view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RadioApp(Ui_MainWindow())  # Pass the main infotainment UI
    main_window.show()
    sys.exit(app.exec())

