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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Authentcation_Window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(987, 574)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.authentication_camera_label = QLabel(Form)
        self.authentication_camera_label.setObjectName(u"authentication_camera_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authentication_camera_label.sizePolicy().hasHeightForWidth())
        self.authentication_camera_label.setSizePolicy(sizePolicy)
        self.authentication_camera_label.setMinimumSize(QSize(550, 260))
        self.authentication_camera_label.setMaximumSize(QSize(16777215, 16777215))
        self.authentication_camera_label.setBaseSize(QSize(550, 300))
        self.authentication_camera_label.setScaledContents(True)
        self.authentication_camera_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.authentication_camera_label)

        self.instructions_label = QLabel(Form)
        self.instructions_label.setObjectName(u"instructions_label")
        self.instructions_label.setMinimumSize(QSize(0, 35))
        self.instructions_label.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.instructions_label.setFont(font)
        self.instructions_label.setStyleSheet(u"QLabel\n"
"{\n"
"	color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"	border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"color: rgb(36, 31, 49);\n"
"\n"
"}\n"
"")
        self.instructions_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.instructions_label)

        self.result_label = QLabel(Form)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(0, 35))
        self.result_label.setMaximumSize(QSize(16777215, 35))
        self.result_label.setFont(font)
        self.result_label.setStyleSheet(u"QLabel\n"
"{\n"
"	color:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"	border:2px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4) ;\n"
"color: rgb(143, 240, 164);\n"
"}\n"
"")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.authentication_camera_label.setText("")
        self.instructions_label.setText(QCoreApplication.translate("Form", u"Please, turn your head left!", None))
        self.result_label.setText(QCoreApplication.translate("Form", u"User is addedd successfully", None))
    # retranslateUi

