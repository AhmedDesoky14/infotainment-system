# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_confirm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class DeleteBox(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QSize(800, 600))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 109, 130, 1), stop:1 rgba(39, 55, 77, 1));")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.confirm_label = QLabel(Form)
        self.confirm_label.setObjectName(u"confirm_label")
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.confirm_label.setFont(font)
        self.confirm_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.confirm_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_delete_button = QPushButton(Form)
        self.yes_delete_button.setObjectName(u"yes_delete_button")
        self.yes_delete_button.setMinimumSize(QSize(384, 150))
        self.yes_delete_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")

        self.horizontalLayout.addWidget(self.yes_delete_button)

        self.no_delete_button = QPushButton(Form)
        self.no_delete_button.setObjectName(u"no_delete_button")
        self.no_delete_button.setMinimumSize(QSize(384, 150))
        self.no_delete_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;  /* Makes the button rounded */\n"
"    padding: 10px;\n"
"border: 2px solid #241f31;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #E9EFF4;\n"
"}")

        self.horizontalLayout.addWidget(self.no_delete_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.confirm_label.setText(QCoreApplication.translate("Form", u"Are you sure you want\n"
"to delete this user?", None))
        self.yes_delete_button.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.no_delete_button.setText(QCoreApplication.translate("Form", u"No", None))
    # retranslateUi

