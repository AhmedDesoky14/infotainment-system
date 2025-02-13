# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adduser_authentication.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Authentcation_Window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(987, 592)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.auth_camera_label = QLabel(Form)
        self.auth_camera_label.setObjectName(u"auth_camera_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_camera_label.sizePolicy().hasHeightForWidth())
        self.auth_camera_label.setSizePolicy(sizePolicy)
        self.auth_camera_label.setMinimumSize(QSize(550, 260))
        self.auth_camera_label.setMaximumSize(QSize(16777215, 16777215))
        self.auth_camera_label.setBaseSize(QSize(550, 300))
        self.auth_camera_label.setScaledContents(True)
        self.auth_camera_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.auth_camera_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMinimumSize(QSize(250, 25))
        self.date_label.setMaximumSize(QSize(16777215, 16777215))
        self.date_label.setBaseSize(QSize(470, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);")
        self.date_label.setFrameShape(QFrame.NoFrame)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.date_label)

        self.time_label = QLabel(Form)
        self.time_label.setObjectName(u"time_label")
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setMinimumSize(QSize(250, 25))
        self.time_label.setMaximumSize(QSize(16777215, 16777215))
        self.time_label.setBaseSize(QSize(470, 50))
        self.time_label.setFont(font)
        self.time_label.setStyleSheet(u"background: transparent;\n"
"color: rgb(36, 31, 49);\n"
"")
        self.time_label.setFrameShape(QFrame.NoFrame)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.time_label)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.auth_button = QPushButton(Form)
        self.auth_button.setObjectName(u"auth_button")
        self.auth_button.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.auth_button.setFont(font1)
        self.auth_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")

        self.horizontalLayout.addWidget(self.auth_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.auth_text_label = QLabel(Form)
        self.auth_text_label.setObjectName(u"auth_text_label")
        self.auth_text_label.setMinimumSize(QSize(0, 35))
        self.auth_text_label.setMaximumSize(QSize(16777215, 35))
        self.auth_text_label.setFont(font1)
        self.auth_text_label.setStyleSheet(u"QLabel\n"
"{\n"
"	color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"	border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"}\n"
"")
        self.auth_text_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.auth_text_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.auth_camera_label.setText("")
        self.date_label.setText(QCoreApplication.translate("Form", u"Date: Feb 8, 2025", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"Time: 10:41AM", None))
        self.auth_button.setText(QCoreApplication.translate("Form", u"Start Authentication", None))
        self.auth_text_label.setText("")
    # retranslateUi

