# # This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPainterPath, QRegion
from PySide6.QtCore import QUrl, QRect
import screens

class gps_tab:
    def __init__(self):
        self.ui = screens.main_screen_ui
        # Locate GPS tab in infotainment UI
        self.gps_tab_widget = self.ui.screen_tabs.findChild(QWidget, "gps_tab")
        # Create WebEngineView inside the GPS tab
        self.web_view = QWebEngineView(self.gps_tab_widget)
        self.web_view.setGeometry(0, 0, self.gps_tab_widget.width(), self.gps_tab_widget.height())
        # Ensure the GPS tab uses a layout
        self.gps_tab_widget.setLayout(QVBoxLayout())
        # Remove margins and spacing to allow full expansion
        self.gps_tab_widget.layout().setContentsMargins(0, 0, 0, 0)
        self.gps_tab_widget.layout().setSpacing(0)
        # Apply the correct size policy
        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Add web view to layout
        self.gps_tab_widget.layout().addWidget(self.web_view)
        # Forcefully round the corners using masking
        self.gps_tab_widget.resizeEvent = self.apply_rounded_mask
        #load google maps url
        self.load_google_maps()

    # Apply a rounded mask to the GPS tab to force rounded edges
    def apply_rounded_mask(self,event = None):
        """Applies a rounded mask to the widget dynamically on resize."""
        if not self.gps_tab_widget.isVisible():
            return  # Avoid applying mask when it's not shown

        radius = 20  # Adjust corner radius
        width = self.gps_tab_widget.width()
        height = self.gps_tab_widget.height()

        if width > 0 and height > 0:
            path = QPainterPath()
            path.addRoundedRect(QRect(0, 0, width, height), radius, radius)
            region = QRegion(path.toFillPolygon().toPolygon())
            self.gps_tab_widget.setMask(region)

    #Load google maps URL
    def load_google_maps(self):
        google_maps_url = "https://www.google.com/maps"
        self.web_view.setUrl(QUrl(google_maps_url))
        self.web_view.show()

