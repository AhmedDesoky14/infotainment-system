# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infotainment_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

import os, sys
# Get absolute path to UI/resources
resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "UI_Python", "resources"))
# Add to Python's module search path
sys.path.append(resources_path)
# Now import the resources
import rc_images
import rc_popups
import rc_icons

class Main_Screen_UI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 853)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setBaseSize(QSize(800, 600))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(100, 100))
        self.logo.setMaximumSize(QSize(200, 200))
        self.logo.setSizeIncrement(QSize(0, 0))
        self.logo.setBaseSize(QSize(100, 100))
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap(u":/logo/images/Peugeot-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMinimumSize(QSize(500, 25))
        self.date_label.setMaximumSize(QSize(16777215, 16777215))
        self.date_label.setBaseSize(QSize(470, 50))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);")
        self.date_label.setFrameShape(QFrame.NoFrame)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.date_label)

        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setMinimumSize(QSize(500, 25))
        self.time_label.setMaximumSize(QSize(16777215, 16777215))
        self.time_label.setBaseSize(QSize(470, 50))
        self.time_label.setFont(font)
        self.time_label.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);\n"
"")
        self.time_label.setFrameShape(QFrame.NoFrame)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.time_label)

        self.home_speed_2 = QLabel(self.centralwidget)
        self.home_speed_2.setObjectName(u"home_speed_2")
        sizePolicy.setHeightForWidth(self.home_speed_2.sizePolicy().hasHeightForWidth())
        self.home_speed_2.setSizePolicy(sizePolicy)
        self.home_speed_2.setMinimumSize(QSize(500, 50))
        self.home_speed_2.setMaximumSize(QSize(16777215, 16777215))
        self.home_speed_2.setBaseSize(QSize(180, 60))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        self.home_speed_2.setFont(font1)
        self.home_speed_2.setStyleSheet(u"/*border: 4px solid #3674B5;\n"
"border-radius: 10px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"/*color: rgb(36, 31, 49);*/\n"
"color: rgb(229, 165, 10);")
        self.home_speed_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.home_speed_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.temperature_icon = QLabel(self.centralwidget)
        self.temperature_icon.setObjectName(u"temperature_icon")
        sizePolicy.setHeightForWidth(self.temperature_icon.sizePolicy().hasHeightForWidth())
        self.temperature_icon.setSizePolicy(sizePolicy)
        self.temperature_icon.setMinimumSize(QSize(50, 50))
        self.temperature_icon.setMaximumSize(QSize(100, 100))
        self.temperature_icon.setBaseSize(QSize(50, 50))
        self.temperature_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.temperature_icon.setPixmap(QPixmap(u":/temperature/icons/temperature/temperature.png"))
        self.temperature_icon.setScaledContents(True)
        self.temperature_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.temperature_icon)

        self.temperature_value = QLabel(self.centralwidget)
        self.temperature_value.setObjectName(u"temperature_value")
        sizePolicy.setHeightForWidth(self.temperature_value.sizePolicy().hasHeightForWidth())
        self.temperature_value.setSizePolicy(sizePolicy)
        self.temperature_value.setMinimumSize(QSize(70, 50))
        self.temperature_value.setMaximumSize(QSize(16777215, 16777215))
        self.temperature_value.setBaseSize(QSize(100, 50))
        self.temperature_value.setFont(font)
        self.temperature_value.setStyleSheet(u"background: transparent;\n"
"color: rgb(154, 153, 150);")
        self.temperature_value.setScaledContents(False)
        self.temperature_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.temperature_value)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.battery_icon = QLabel(self.centralwidget)
        self.battery_icon.setObjectName(u"battery_icon")
        sizePolicy.setHeightForWidth(self.battery_icon.sizePolicy().hasHeightForWidth())
        self.battery_icon.setSizePolicy(sizePolicy)
        self.battery_icon.setMinimumSize(QSize(50, 50))
        self.battery_icon.setMaximumSize(QSize(100, 100))
        self.battery_icon.setBaseSize(QSize(50, 50))
        self.battery_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.battery_icon.setPixmap(QPixmap(u":/battery/icons/battery/100%.png"))
        self.battery_icon.setScaledContents(True)
        self.battery_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.battery_icon)

        self.battery_value = QLabel(self.centralwidget)
        self.battery_value.setObjectName(u"battery_value")
        sizePolicy.setHeightForWidth(self.battery_value.sizePolicy().hasHeightForWidth())
        self.battery_value.setSizePolicy(sizePolicy)
        self.battery_value.setMinimumSize(QSize(70, 50))
        self.battery_value.setMaximumSize(QSize(16777215, 16777215))
        self.battery_value.setBaseSize(QSize(100, 50))
        self.battery_value.setFont(font)
        self.battery_value.setStyleSheet(u"background: transparent;\n"
"color: rgb(154, 153, 150);")
        self.battery_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.battery_value)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(3, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.screen_tabs = QTabWidget(self.centralwidget)
        self.screen_tabs.setObjectName(u"screen_tabs")
        self.screen_tabs.setMinimumSize(QSize(780, 475))
        self.screen_tabs.setMaximumSize(QSize(16777215, 16777215))
        self.screen_tabs.setStyleSheet(u"QTabWidget {\n"
"    border: none;  /* Remove border around the tab widget */\n"
"}\n"
"QTabBar {\n"
"    alignment: center;  /* This will center the tabs horizontally */\n"
"}\n"
"QTabBar::tab {\n"
"    padding: 10px;\n"
"    border-radius: 10px;  /* For rounded corners */\n"
"    margin-right: 5px;  /* Space between tabs */\n"
"    height: 35px; /* Adjust height */\n"
"    background: transparent;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #6C95B4;  /* Highlight the selected tab */\n"
"}")
        self.screen_tabs.setTabPosition(QTabWidget.South)
        self.screen_tabs.setTabShape(QTabWidget.Rounded)
        self.screen_tabs.setIconSize(QSize(128, 55))
        self.screen_tabs.setElideMode(Qt.ElideNone)
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_tab.sizePolicy().hasHeightForWidth())
        self.home_tab.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.home_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.warning_icon1 = QLabel(self.home_tab)
        self.warning_icon1.setObjectName(u"warning_icon1")
        sizePolicy.setHeightForWidth(self.warning_icon1.sizePolicy().hasHeightForWidth())
        self.warning_icon1.setSizePolicy(sizePolicy)
        self.warning_icon1.setMinimumSize(QSize(75, 75))
        self.warning_icon1.setMaximumSize(QSize(16777215, 16777215))
        self.warning_icon1.setBaseSize(QSize(75, 75))
        self.warning_icon1.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.warning_icon1.setScaledContents(True)
        self.warning_icon1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.warning_icon1)

        self.warning_icon2 = QLabel(self.home_tab)
        self.warning_icon2.setObjectName(u"warning_icon2")
        sizePolicy.setHeightForWidth(self.warning_icon2.sizePolicy().hasHeightForWidth())
        self.warning_icon2.setSizePolicy(sizePolicy)
        self.warning_icon2.setMinimumSize(QSize(75, 75))
        self.warning_icon2.setMaximumSize(QSize(16777215, 16777215))
        self.warning_icon2.setBaseSize(QSize(75, 75))
        self.warning_icon2.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.warning_icon2.setScaledContents(True)
        self.warning_icon2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.warning_icon2)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.warning_icon3 = QLabel(self.home_tab)
        self.warning_icon3.setObjectName(u"warning_icon3")
        sizePolicy.setHeightForWidth(self.warning_icon3.sizePolicy().hasHeightForWidth())
        self.warning_icon3.setSizePolicy(sizePolicy)
        self.warning_icon3.setMinimumSize(QSize(75, 75))
        self.warning_icon3.setMaximumSize(QSize(16777215, 16777215))
        self.warning_icon3.setBaseSize(QSize(75, 75))
        self.warning_icon3.setFont(font)
        self.warning_icon3.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;")
        self.warning_icon3.setScaledContents(True)
        self.warning_icon3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.warning_icon3)

        self.warning_icon4 = QLabel(self.home_tab)
        self.warning_icon4.setObjectName(u"warning_icon4")
        sizePolicy.setHeightForWidth(self.warning_icon4.sizePolicy().hasHeightForWidth())
        self.warning_icon4.setSizePolicy(sizePolicy)
        self.warning_icon4.setMinimumSize(QSize(75, 75))
        self.warning_icon4.setMaximumSize(QSize(16777215, 16777215))
        self.warning_icon4.setBaseSize(QSize(75, 75))
        self.warning_icon4.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.warning_icon4.setScaledContents(True)
        self.warning_icon4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.warning_icon4)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.speed_limit = QLabel(self.home_tab)
        self.speed_limit.setObjectName(u"speed_limit")
        sizePolicy.setHeightForWidth(self.speed_limit.sizePolicy().hasHeightForWidth())
        self.speed_limit.setSizePolicy(sizePolicy)
        self.speed_limit.setMinimumSize(QSize(75, 75))
        self.speed_limit.setMaximumSize(QSize(16777215, 16777215))
        self.speed_limit.setBaseSize(QSize(75, 75))
        self.speed_limit.setFont(font)
        self.speed_limit.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"color: rgb(165, 29, 45);\n"
"")
        self.speed_limit.setScaledContents(True)
        self.speed_limit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.speed_limit)

        self.speed_limit_warning = QLabel(self.home_tab)
        self.speed_limit_warning.setObjectName(u"speed_limit_warning")
        sizePolicy.setHeightForWidth(self.speed_limit_warning.sizePolicy().hasHeightForWidth())
        self.speed_limit_warning.setSizePolicy(sizePolicy)
        self.speed_limit_warning.setMinimumSize(QSize(75, 75))
        self.speed_limit_warning.setMaximumSize(QSize(16777215, 16777215))
        self.speed_limit_warning.setBaseSize(QSize(75, 75))
        self.speed_limit_warning.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.speed_limit_warning.setScaledContents(True)
        self.speed_limit_warning.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.speed_limit_warning)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.turn_left = QLabel(self.home_tab)
        self.turn_left.setObjectName(u"turn_left")
        sizePolicy.setHeightForWidth(self.turn_left.sizePolicy().hasHeightForWidth())
        self.turn_left.setSizePolicy(sizePolicy)
        self.turn_left.setMinimumSize(QSize(75, 75))
        self.turn_left.setMaximumSize(QSize(16777215, 16777215))
        self.turn_left.setBaseSize(QSize(75, 75))
        self.turn_left.setFont(font)
        self.turn_left.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.turn_left.setScaledContents(True)
        self.turn_left.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.turn_left)

        self.turn_right = QLabel(self.home_tab)
        self.turn_right.setObjectName(u"turn_right")
        sizePolicy.setHeightForWidth(self.turn_right.sizePolicy().hasHeightForWidth())
        self.turn_right.setSizePolicy(sizePolicy)
        self.turn_right.setMinimumSize(QSize(75, 75))
        self.turn_right.setMaximumSize(QSize(16777215, 16777215))
        self.turn_right.setBaseSize(QSize(75, 75))
        self.turn_right.setStyleSheet(u"border: 1px solid #3d3846;\n"
"border-radius: 15px;  /* Makes the boarder rounded */\n"
"background: transparent;\n"
"")
        self.turn_right.setScaledContents(True)
        self.turn_right.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.turn_right)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.speedlimit_button = QPushButton(self.home_tab)
        self.speedlimit_button.setObjectName(u"speedlimit_button")
        sizePolicy.setHeightForWidth(self.speedlimit_button.sizePolicy().hasHeightForWidth())
        self.speedlimit_button.setSizePolicy(sizePolicy)
        self.speedlimit_button.setMinimumSize(QSize(180, 70))
        self.speedlimit_button.setMaximumSize(QSize(16777215, 16777215))
        self.speedlimit_button.setBaseSize(QSize(180, 70))
        font2 = QFont()
        font2.setPointSize(11)
        self.speedlimit_button.setFont(font2)
        self.speedlimit_button.setFocusPolicy(Qt.NoFocus)
        self.speedlimit_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #F8FAFC;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/speed_icons/icons/speed/speed_set.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.speedlimit_button.setIcon(icon)
        self.speedlimit_button.setIconSize(QSize(32, 32))
        self.speedlimit_button.setCheckable(True)
        self.speedlimit_button.setAutoExclusive(False)
        self.speedlimit_button.setAutoDefault(False)
        self.speedlimit_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.speedlimit_button)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.front_camera_view = QLabel(self.home_tab)
        self.front_camera_view.setObjectName(u"front_camera_view")
        sizePolicy.setHeightForWidth(self.front_camera_view.sizePolicy().hasHeightForWidth())
        self.front_camera_view.setSizePolicy(sizePolicy)
        self.front_camera_view.setMinimumSize(QSize(570, 400))
        self.front_camera_view.setMaximumSize(QSize(16777215, 16777215))
        self.front_camera_view.setSizeIncrement(QSize(-7937, 0))
        self.front_camera_view.setBaseSize(QSize(570, 410))
        self.front_camera_view.setFrameShape(QFrame.Panel)
        self.front_camera_view.setFrameShadow(QFrame.Plain)
        self.front_camera_view.setLineWidth(2)
        self.front_camera_view.setTextFormat(Qt.RichText)
        self.front_camera_view.setScaledContents(True)
        self.front_camera_view.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.front_camera_view)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/tabs_icons/icons/tabs_icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.home_tab, icon1, "")
        self.gps_tab = QWidget()
        self.gps_tab.setObjectName(u"gps_tab")
        sizePolicy1.setHeightForWidth(self.gps_tab.sizePolicy().hasHeightForWidth())
        self.gps_tab.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.gps_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gps_web_engine_view = QWidget(self.gps_tab)
        self.gps_web_engine_view.setObjectName(u"gps_web_engine_view")
        sizePolicy1.setHeightForWidth(self.gps_web_engine_view.sizePolicy().hasHeightForWidth())
        self.gps_web_engine_view.setSizePolicy(sizePolicy1)
        self.gps_web_engine_view.setStyleSheet(u"border-radius: 20px;")

        self.gridLayout_2.addWidget(self.gps_web_engine_view, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/tabs_icons/icons/tabs_icons/gps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.gps_tab, icon2, "")
        self.media_tab = QWidget()
        self.media_tab.setObjectName(u"media_tab")
        self.gridLayout_5 = QGridLayout(self.media_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.media_player = QWidget(self.media_tab)
        self.media_player.setObjectName(u"media_player")
        self.gridLayout_9 = QGridLayout(self.media_player)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.audioselect_list = QListWidget(self.media_player)
        self.audioselect_list.setObjectName(u"audioselect_list")
        sizePolicy.setHeightForWidth(self.audioselect_list.sizePolicy().hasHeightForWidth())
        self.audioselect_list.setSizePolicy(sizePolicy)
        self.audioselect_list.setMinimumSize(QSize(350, 140))
        self.audioselect_list.setBaseSize(QSize(350, 180))
        font3 = QFont()
        font3.setPointSize(14)
        self.audioselect_list.setFont(font3)
        self.audioselect_list.setStyleSheet(u"QListView\n"
"{\n"
"    border : none;\n"
"    background-color: #343434;\n"
"    color: white;\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"    outline: 0;\n"
"        border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:!active\n"
"{\n"
"    background-color: #308dc6;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.audioselect_list)

        self.song_cover = QLabel(self.media_player)
        self.song_cover.setObjectName(u"song_cover")
        self.song_cover.setMinimumSize(QSize(350, 140))
        self.song_cover.setBaseSize(QSize(350, 180))
        self.song_cover.setPixmap(QPixmap(u":/song_cover/images/default_cover.jpeg"))
        self.song_cover.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.song_cover)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.filename = QLabel(self.media_player)
        self.filename.setObjectName(u"filename")
        self.filename.setMinimumSize(QSize(450, 25))
        self.filename.setMaximumSize(QSize(16777215, 30))
        self.filename.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.filename.setFont(font4)
        self.filename.setStyleSheet(u"QLabel\n"
"{\n"
"	color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"	border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"\n"
"}\n"
"")
        self.filename.setFrameShape(QFrame.Panel)
        self.filename.setLineWidth(2)
        self.filename.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.filename)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 4)
        self.horizontalLayout_15.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.audio_file_progress_slidebar = QSlider(self.media_player)
        self.audio_file_progress_slidebar.setObjectName(u"audio_file_progress_slidebar")
        self.audio_file_progress_slidebar.setStyleSheet(u"QSlider::groove:horizontal  {\n"
"	border: 1px solid #999999; \n"
"	height: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal  {\n"
"	background: #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover  {\n"
"	background: #308dc6; \n"
"	border-color: #308dc6;\n"
"}\n"
"\n"
"")
        self.audio_file_progress_slidebar.setMinimum(1)
        self.audio_file_progress_slidebar.setMaximum(100)
        self.audio_file_progress_slidebar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.audio_file_progress_slidebar)

        self.horizontalLayout_16.setStretch(0, 10)

        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_current_duration = QLabel(self.media_player)
        self.label_current_duration.setObjectName(u"label_current_duration")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_current_duration.setFont(font5)
        self.label_current_duration.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);\n"
"\n"
"")

        self.horizontalLayout_17.addWidget(self.label_current_duration)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)

        self.label_total_time = QLabel(self.media_player)
        self.label_total_time.setObjectName(u"label_total_time")
        self.label_total_time.setFont(font5)
        self.label_total_time.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);\n"
"")

        self.horizontalLayout_17.addWidget(self.label_total_time)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.shuffle_button = QPushButton(self.media_player)
        self.shuffle_button.setObjectName(u"shuffle_button")
        sizePolicy.setHeightForWidth(self.shuffle_button.sizePolicy().hasHeightForWidth())
        self.shuffle_button.setSizePolicy(sizePolicy)
        self.shuffle_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/mediaplayer/icons/mediaplayer/shuffle_enabled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffle_button.setIcon(icon3)
        self.shuffle_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.shuffle_button)

        self.previous_button = QPushButton(self.media_player)
        self.previous_button.setObjectName(u"previous_button")
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        self.previous_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/mediaplayer/icons/mediaplayer/previous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previous_button.setIcon(icon4)
        self.previous_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.previous_button)

        self.rewind_button = QPushButton(self.media_player)
        self.rewind_button.setObjectName(u"rewind_button")
        sizePolicy.setHeightForWidth(self.rewind_button.sizePolicy().hasHeightForWidth())
        self.rewind_button.setSizePolicy(sizePolicy)
        self.rewind_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/mediaplayer/icons/mediaplayer/rewind.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rewind_button.setIcon(icon5)
        self.rewind_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.rewind_button)

        self.stop_button = QPushButton(self.media_player)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/mediaplayer/icons/mediaplayer/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon6)
        self.stop_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.stop_button)

        self.playpause_button = QPushButton(self.media_player)
        self.playpause_button.setObjectName(u"playpause_button")
        sizePolicy.setHeightForWidth(self.playpause_button.sizePolicy().hasHeightForWidth())
        self.playpause_button.setSizePolicy(sizePolicy)
        self.playpause_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/mediaplayer/icons/mediaplayer/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playpause_button.setIcon(icon7)
        self.playpause_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.playpause_button)

        self.forward_button = QPushButton(self.media_player)
        self.forward_button.setObjectName(u"forward_button")
        sizePolicy.setHeightForWidth(self.forward_button.sizePolicy().hasHeightForWidth())
        self.forward_button.setSizePolicy(sizePolicy)
        self.forward_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/mediaplayer/icons/mediaplayer/forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button.setIcon(icon8)
        self.forward_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.forward_button)

        self.next_button = QPushButton(self.media_player)
        self.next_button.setObjectName(u"next_button")
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/mediaplayer/icons/mediaplayer/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_button.setIcon(icon9)
        self.next_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.next_button)

        self.repeat_button = QPushButton(self.media_player)
        self.repeat_button.setObjectName(u"repeat_button")
        sizePolicy.setHeightForWidth(self.repeat_button.sizePolicy().hasHeightForWidth())
        self.repeat_button.setSizePolicy(sizePolicy)
        self.repeat_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/mediaplayer/icons/mediaplayer/repeat_disabled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.repeat_button.setIcon(icon10)
        self.repeat_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.repeat_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)

        self.mute_unmute_button = QPushButton(self.media_player)
        self.mute_unmute_button.setObjectName(u"mute_unmute_button")
        sizePolicy.setHeightForWidth(self.mute_unmute_button.sizePolicy().hasHeightForWidth())
        self.mute_unmute_button.setSizePolicy(sizePolicy)
        self.mute_unmute_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/mediaplayer/icons/mediaplayer/unmute.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mute_unmute_button.setIcon(icon11)
        self.mute_unmute_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_19.addWidget(self.mute_unmute_button)

        self.volume_slider = QSlider(self.media_player)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy2)
        self.volume_slider.setStyleSheet(u"QSlider::groove:horizontal  {\n"
"	border: 1px solid #999999; \n"
"	height: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal  {\n"
"	background: #2a2a2a; \n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px;\n"
"	border: 1px sloid #2a2a2a;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal  {\n"
"	background: #2a2a2a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover  {\n"
"	background: #308dc6; \n"
"	border-color: #308dc6;\n"
"}\n"
"")
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSliderPosition(50)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.volume_slider)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_19.setStretch(0, 3)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 4)
        self.horizontalLayout_19.setStretch(3, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.verticalLayout_10.setStretch(0, 6)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 1)
        self.verticalLayout_10.setStretch(4, 2)
        self.verticalLayout_10.setStretch(5, 2)

        self.gridLayout_9.addLayout(self.verticalLayout_10, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.media_player, 0, 0, 1, 1)

        icon12 = QIcon()
        icon12.addFile(u":/tabs_icons/icons/tabs_icons/media.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.media_tab, icon12, "")
        self.radio_tab = QWidget()
        self.radio_tab.setObjectName(u"radio_tab")
        sizePolicy1.setHeightForWidth(self.radio_tab.sizePolicy().hasHeightForWidth())
        self.radio_tab.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.radio_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_web_engine_view = QWidget(self.radio_tab)
        self.radio_web_engine_view.setObjectName(u"radio_web_engine_view")
        sizePolicy1.setHeightForWidth(self.radio_web_engine_view.sizePolicy().hasHeightForWidth())
        self.radio_web_engine_view.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.radio_web_engine_view, 0, 0, 1, 1)

        icon13 = QIcon()
        icon13.addFile(u":/tabs_icons/icons/tabs_icons/radio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.radio_tab, icon13, "")
        self.driving_aassist_tab = QWidget()
        self.driving_aassist_tab.setObjectName(u"driving_aassist_tab")
        sizePolicy1.setHeightForWidth(self.driving_aassist_tab.sizePolicy().hasHeightForWidth())
        self.driving_aassist_tab.setSizePolicy(sizePolicy1)
        self.gridLayout_7 = QGridLayout(self.driving_aassist_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.foreward_icon = QLabel(self.driving_aassist_tab)
        self.foreward_icon.setObjectName(u"foreward_icon")
        self.foreward_icon.setMinimumSize(QSize(60, 60))
        self.foreward_icon.setMaximumSize(QSize(16777215, 16777215))
        self.foreward_icon.setBaseSize(QSize(60, 60))
        self.foreward_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.foreward_icon.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.foreward_icon)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 10)

        self.gridLayout_6.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.usercamera_view = QLabel(self.driving_aassist_tab)
        self.usercamera_view.setObjectName(u"usercamera_view")
        sizePolicy.setHeightForWidth(self.usercamera_view.sizePolicy().hasHeightForWidth())
        self.usercamera_view.setSizePolicy(sizePolicy)
        self.usercamera_view.setMinimumSize(QSize(550, 260))
        self.usercamera_view.setMaximumSize(QSize(16777215, 16777215))
        self.usercamera_view.setBaseSize(QSize(550, 300))
        self.usercamera_view.setScaledContents(True)
        self.usercamera_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.usercamera_view)

        self.verticalLayout_5.setStretch(0, 9)

        self.gridLayout_6.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.warningx = QLabel(self.driving_aassist_tab)
        self.warningx.setObjectName(u"warningx")
        self.warningx.setMinimumSize(QSize(60, 60))
        self.warningx.setBaseSize(QSize(60, 60))
        self.warningx.setStyleSheet(u"background: transparent;\n"
"")
        self.warningx.setScaledContents(True)
        self.warningx.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.warningx, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.left_icon = QLabel(self.driving_aassist_tab)
        self.left_icon.setObjectName(u"left_icon")
        sizePolicy.setHeightForWidth(self.left_icon.sizePolicy().hasHeightForWidth())
        self.left_icon.setSizePolicy(sizePolicy)
        self.left_icon.setMinimumSize(QSize(60, 60))
        self.left_icon.setMaximumSize(QSize(16777215, 16777215))
        self.left_icon.setBaseSize(QSize(60, 60))
        self.left_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.left_icon.setScaledContents(True)
        self.left_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.left_icon)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.verticalLayout_7.setStretch(0, 10)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 10)

        self.gridLayout_6.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.backward_icon = QLabel(self.driving_aassist_tab)
        self.backward_icon.setObjectName(u"backward_icon")
        self.backward_icon.setMinimumSize(QSize(60, 60))
        self.backward_icon.setMaximumSize(QSize(16777215, 16777215))
        self.backward_icon.setBaseSize(QSize(60, 60))
        self.backward_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.backward_icon.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.backward_icon)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.horizontalLayout_8.setStretch(0, 10)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 10)

        self.gridLayout_6.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)

        self.brake_icon = QLabel(self.driving_aassist_tab)
        self.brake_icon.setObjectName(u"brake_icon")
        sizePolicy.setHeightForWidth(self.brake_icon.sizePolicy().hasHeightForWidth())
        self.brake_icon.setSizePolicy(sizePolicy)
        self.brake_icon.setMinimumSize(QSize(60, 60))
        self.brake_icon.setMaximumSize(QSize(16777215, 16777215))
        self.brake_icon.setBaseSize(QSize(60, 60))
        self.brake_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.brake_icon.setScaledContents(True)
        self.brake_icon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.brake_icon, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.right_icon = QLabel(self.driving_aassist_tab)
        self.right_icon.setObjectName(u"right_icon")
        sizePolicy.setHeightForWidth(self.right_icon.sizePolicy().hasHeightForWidth())
        self.right_icon.setSizePolicy(sizePolicy)
        self.right_icon.setMinimumSize(QSize(60, 60))
        self.right_icon.setMaximumSize(QSize(16777215, 16777215))
        self.right_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.right_icon.setScaledContents(True)
        self.right_icon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.right_icon)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.verticalLayout_6.setStretch(0, 10)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 10)

        self.gridLayout_6.addLayout(self.verticalLayout_6, 1, 2, 1, 1)

        self.speed_limit_icon = QLabel(self.driving_aassist_tab)
        self.speed_limit_icon.setObjectName(u"speed_limit_icon")
        sizePolicy.setHeightForWidth(self.speed_limit_icon.sizePolicy().hasHeightForWidth())
        self.speed_limit_icon.setSizePolicy(sizePolicy)
        self.speed_limit_icon.setMinimumSize(QSize(60, 60))
        self.speed_limit_icon.setMaximumSize(QSize(16777215, 16777215))
        self.speed_limit_icon.setBaseSize(QSize(60, 60))
        self.speed_limit_icon.setStyleSheet(u"background: transparent;\n"
"")
        self.speed_limit_icon.setScaledContents(True)
        self.speed_limit_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.speed_limit_icon, 2, 0, 1, 1)

        self.collision_warning = QLabel(self.driving_aassist_tab)
        self.collision_warning.setObjectName(u"collision_warning")
        sizePolicy.setHeightForWidth(self.collision_warning.sizePolicy().hasHeightForWidth())
        self.collision_warning.setSizePolicy(sizePolicy)
        self.collision_warning.setMinimumSize(QSize(60, 60))
        self.collision_warning.setMaximumSize(QSize(16777215, 16777215))
        self.collision_warning.setBaseSize(QSize(60, 60))
        self.collision_warning.setStyleSheet(u"background: transparent;\n"
"")
        self.collision_warning.setScaledContents(True)
        self.collision_warning.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.collision_warning, 2, 2, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 15)
        self.gridLayout_6.setRowStretch(2, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 15)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        icon14 = QIcon()
        icon14.addFile(u":/tabs_icons/icons/tabs_icons/driving_assist.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.driving_aassist_tab, icon14, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.gridLayout_8 = QGridLayout(self.settings_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.users_list = QListWidget(self.settings_tab)
        QListWidgetItem(self.users_list)
        QListWidgetItem(self.users_list)
        QListWidgetItem(self.users_list)
        QListWidgetItem(self.users_list)
        QListWidgetItem(self.users_list)
        self.users_list.setObjectName(u"users_list")
        sizePolicy.setHeightForWidth(self.users_list.sizePolicy().hasHeightForWidth())
        self.users_list.setSizePolicy(sizePolicy)
        self.users_list.setMinimumSize(QSize(377, 140))
        self.users_list.setMaximumSize(QSize(16777215, 16777215))
        self.users_list.setSizeIncrement(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(16)
        self.users_list.setFont(font6)
        self.users_list.setStyleSheet(u"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"/* Larger buttons for scrollbar */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"/* Customize the arrow size */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.users_list.setTextElideMode(Qt.ElideRight)
        self.users_list.setViewMode(QListView.ListMode)
        self.users_list.setSortingEnabled(False)

        self.horizontalLayout_10.addWidget(self.users_list)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.adduser_button = QPushButton(self.settings_tab)
        self.adduser_button.setObjectName(u"adduser_button")
        sizePolicy.setHeightForWidth(self.adduser_button.sizePolicy().hasHeightForWidth())
        self.adduser_button.setSizePolicy(sizePolicy)
        self.adduser_button.setMinimumSize(QSize(377, 55))
        self.adduser_button.setMaximumSize(QSize(16777215, 16777215))
        self.adduser_button.setFont(font3)
        self.adduser_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/settings/icons/settings/9022821_user_circle_plus_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.adduser_button.setIcon(icon15)
        self.adduser_button.setIconSize(QSize(48, 48))

        self.verticalLayout_9.addWidget(self.adduser_button)

        self.deleteuser_button = QPushButton(self.settings_tab)
        self.deleteuser_button.setObjectName(u"deleteuser_button")
        sizePolicy.setHeightForWidth(self.deleteuser_button.sizePolicy().hasHeightForWidth())
        self.deleteuser_button.setSizePolicy(sizePolicy)
        self.deleteuser_button.setMinimumSize(QSize(377, 55))
        self.deleteuser_button.setMaximumSize(QSize(16777215, 16777215))
        self.deleteuser_button.setFont(font3)
        self.deleteuser_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/settings/icons/settings/9022762_user_circle_minus_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteuser_button.setIcon(icon16)
        self.deleteuser_button.setIconSize(QSize(48, 48))

        self.verticalLayout_9.addWidget(self.deleteuser_button)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.temperature_spinbox = QSpinBox(self.settings_tab)
        self.temperature_spinbox.setObjectName(u"temperature_spinbox")
        sizePolicy.setHeightForWidth(self.temperature_spinbox.sizePolicy().hasHeightForWidth())
        self.temperature_spinbox.setSizePolicy(sizePolicy)
        self.temperature_spinbox.setMinimumSize(QSize(377, 75))
        self.temperature_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.temperature_spinbox.setFont(font6)
        self.temperature_spinbox.setStyleSheet(u"QSpinBox::up-button, QSpinBox::down-button {\n"
"    min-width: 30px;\n"
"    min-height: 30px;\n"
"}")
        self.temperature_spinbox.setAlignment(Qt.AlignCenter)
        self.temperature_spinbox.setMinimum(16)
        self.temperature_spinbox.setMaximum(40)
        self.temperature_spinbox.setValue(16)

        self.horizontalLayout_11.addWidget(self.temperature_spinbox)

        self.set_temperature_button = QPushButton(self.settings_tab)
        self.set_temperature_button.setObjectName(u"set_temperature_button")
        sizePolicy.setHeightForWidth(self.set_temperature_button.sizePolicy().hasHeightForWidth())
        self.set_temperature_button.setSizePolicy(sizePolicy)
        self.set_temperature_button.setMinimumSize(QSize(377, 75))
        self.set_temperature_button.setMaximumSize(QSize(16777215, 16777215))
        self.set_temperature_button.setFont(font3)
        self.set_temperature_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/settings/icons/settings/9022807_thermometer_simple_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.set_temperature_button.setIcon(icon17)
        self.set_temperature_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_11.addWidget(self.set_temperature_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.visual_mode_button = QPushButton(self.settings_tab)
        self.visual_mode_button.setObjectName(u"visual_mode_button")
        self.visual_mode_button.setMinimumSize(QSize(760, 50))
        self.visual_mode_button.setMaximumSize(QSize(16777215, 16777215))
        self.visual_mode_button.setFont(font6)
        self.visual_mode_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #E9EFF4;\n"
"}")
        self.visual_mode_button.setCheckable(True)

        self.verticalLayout_8.addWidget(self.visual_mode_button)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.check_updates_button = QPushButton(self.settings_tab)
        self.check_updates_button.setObjectName(u"check_updates_button")
        sizePolicy.setHeightForWidth(self.check_updates_button.sizePolicy().hasHeightForWidth())
        self.check_updates_button.setSizePolicy(sizePolicy)
        self.check_updates_button.setMinimumSize(QSize(377, 50))
        self.check_updates_button.setMaximumSize(QSize(16777215, 16777215))
        self.check_updates_button.setFont(font3)
        self.check_updates_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/settings/icons/settings/9022183_arrows_counter_clockwise_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.check_updates_button.setIcon(icon18)
        self.check_updates_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_12.addWidget(self.check_updates_button)

        self.update_button = QPushButton(self.settings_tab)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QSize(377, 50))
        self.update_button.setMaximumSize(QSize(16777215, 16777215))
        self.update_button.setFont(font3)
        self.update_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/settings/icons/settings/9022398_cloud_arrow_down_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.update_button.setIcon(icon19)
        self.update_button.setIconSize(QSize(48, 48))
        self.update_button.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.update_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.software_version_label = QLabel(self.settings_tab)
        self.software_version_label.setObjectName(u"software_version_label")
        self.software_version_label.setMinimumSize(QSize(760, 25))
        self.software_version_label.setMaximumSize(QSize(16777215, 16777215))
        self.software_version_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.software_version_label)

        self.update_progress_bar = QProgressBar(self.settings_tab)
        self.update_progress_bar.setObjectName(u"update_progress_bar")
        sizePolicy.setHeightForWidth(self.update_progress_bar.sizePolicy().hasHeightForWidth())
        self.update_progress_bar.setSizePolicy(sizePolicy)
        self.update_progress_bar.setMinimumSize(QSize(760, 25))
        self.update_progress_bar.setMaximumSize(QSize(16777215, 25))
        self.update_progress_bar.setValue(0)
        self.update_progress_bar.setAlignment(Qt.AlignCenter)
        self.update_progress_bar.setTextVisible(False)
        self.update_progress_bar.setInvertedAppearance(False)

        self.verticalLayout_8.addWidget(self.update_progress_bar)

        self.verticalLayout_8.setStretch(0, 6)
        self.verticalLayout_8.setStretch(1, 3)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_8.setStretch(3, 2)
        self.verticalLayout_8.setStretch(4, 1)
        self.verticalLayout_8.setStretch(5, 1)

        self.gridLayout_8.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        icon20 = QIcon()
        icon20.addFile(u":/tabs_icons/icons/tabs_icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_tabs.addTab(self.settings_tab, icon20, "")

        self.verticalLayout_3.addWidget(self.screen_tabs)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 7)

        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.screen_tabs.setCurrentIndex(0)
        self.speedlimit_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date: Feb 8, 2025", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time: 10:41AM", None))
        self.home_speed_2.setText(QCoreApplication.translate("MainWindow", u"125 KM/hr", None))
        self.temperature_icon.setText("")
        self.temperature_value.setText(QCoreApplication.translate("MainWindow", u"15C", None))
        self.battery_icon.setText("")
        self.battery_value.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.warning_icon1.setText("")
        self.warning_icon2.setText("")
        self.warning_icon3.setText("")
        self.warning_icon4.setText("")
        self.speed_limit.setText(QCoreApplication.translate("MainWindow", u"Limit\n"
"120", None))
        self.speed_limit_warning.setText("")
        self.turn_left.setText("")
        self.turn_right.setText("")
        self.speedlimit_button.setText(QCoreApplication.translate("MainWindow", u"  Set Speed Control", None))
        self.front_camera_view.setText("")
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.gps_tab), QCoreApplication.translate("MainWindow", u"GPS", None))
        self.song_cover.setText("")
        self.filename.setText(QCoreApplication.translate("MainWindow", u"Song Name", None))
        self.label_current_duration.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_total_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.shuffle_button.setText("")
        self.previous_button.setText("")
        self.rewind_button.setText("")
        self.stop_button.setText("")
        self.playpause_button.setText("")
        self.forward_button.setText("")
        self.next_button.setText("")
        self.repeat_button.setText("")
        self.mute_unmute_button.setText("")
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.media_tab), QCoreApplication.translate("MainWindow", u"Media", None))
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.radio_tab), QCoreApplication.translate("MainWindow", u"Radio", None))
        self.foreward_icon.setText("")
        self.usercamera_view.setText("")
        self.warningx.setText("")
        self.left_icon.setText("")
        self.backward_icon.setText("")
        self.brake_icon.setText("")
        self.right_icon.setText("")
        self.speed_limit_icon.setText("")
        self.collision_warning.setText("")
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.driving_aassist_tab), QCoreApplication.translate("MainWindow", u"Drive Assist", None))

        __sortingEnabled = self.users_list.isSortingEnabled()
        self.users_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.users_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ahmed", None));
        ___qlistwidgetitem1 = self.users_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ibrahem", None));
        ___qlistwidgetitem2 = self.users_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Karem", None));
        ___qlistwidgetitem3 = self.users_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ammar", None));
        ___qlistwidgetitem4 = self.users_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Omar", None));
        self.users_list.setSortingEnabled(__sortingEnabled)

        self.adduser_button.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.deleteuser_button.setText(QCoreApplication.translate("MainWindow", u"Delete user", None))
        self.set_temperature_button.setText(QCoreApplication.translate("MainWindow", u"Set Temperature", None))
        self.visual_mode_button.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.check_updates_button.setText(QCoreApplication.translate("MainWindow", u"Check Updates", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.software_version_label.setText(QCoreApplication.translate("MainWindow", u"Software Version: 1.0.0", None))
        self.screen_tabs.setTabText(self.screen_tabs.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

