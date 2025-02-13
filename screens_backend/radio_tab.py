# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPainterPath, QRegion
from PySide6.QtCore import QUrl, QRect
import screens

class radio_tab:
    def __init__(self):
        self.ui = screens.main_screen_ui
        # Locate Radio tab in infotainment UI
        self.radio_tab_widget = self.ui.screen_tabs.findChild(QWidget, "radio_tab")
        # Create WebEngineView inside the Radio tab
        self.web_view = QWebEngineView(self.radio_tab_widget)
        self.web_view.setGeometry(0, 0, self.radio_tab_widget.width(), self.radio_tab_widget.height())
        # Ensure the radio tab uses a layout
        self.radio_tab_widget.setLayout(QVBoxLayout())
        # Remove margins and spacing to allow full expansion
        self.radio_tab_widget.layout().setContentsMargins(0, 0, 0, 0)
        self.radio_tab_widget.layout().setSpacing(0)
        # Apply the correct size policy
        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Add web view to layout
        self.radio_tab_widget.layout().addWidget(self.web_view)
        # Forcefully round the corners using masking, using resizeEvent didn't work, so I connected
        # the page loading signal to the "self.apply_rounded_mask" slot to apply the mask
        #self.radio_tab_widget.resizeEvent = self.apply_rounded_mask
        self.web_view.loadFinished.connect(self.apply_rounded_mask)
        #load radio url
        self.load_radio()

    # Apply a rounded mask to the Radio tab to force rounded edges
    def apply_rounded_mask(self,event = None):
        """Applies a rounded mask to the widget dynamically on resize."""
        if not self.radio_tab_widget.isVisible():
            return  # Avoid applying mask when it's not shown

        radius = 20  # Adjust corner radius
        width = self.radio_tab_widget.width()
        height = self.radio_tab_widget.height()

        if width > 0 and height > 0:
            path = QPainterPath()
            path.addRoundedRect(QRect(0, 0, width, height), radius, radius)
            region = QRegion(path.toFillPolygon().toPolygon())
            self.radio_tab_widget.setMask(region)

    #Load a Radio URL
    def load_radio(self):
        radio_url = "https://radio.garden/listen/quran-fm-98-2-idhaet-alqran-alkrym/GQxvGBNK"
        self.web_view.setUrl(QUrl(radio_url))
        self.web_view.show()



