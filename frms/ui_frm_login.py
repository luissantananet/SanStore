# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(296, 193)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(296, 193))
        MainWindow.setMaximumSize(QSize(296, 193))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnlogin = QPushButton(self.centralwidget)
        self.btnlogin.setObjectName(u"btnlogin")
        self.btnlogin.setGeometry(QRect(120, 140, 75, 31))
        self.btnlogin.setFont(font)
        self.btnexit = QPushButton(self.centralwidget)
        self.btnexit.setObjectName(u"btnexit")
        self.btnexit.setGeometry(QRect(200, 140, 75, 31))
        self.btnexit.setFont(font)
        self.lineuser = QLineEdit(self.centralwidget)
        self.lineuser.setObjectName(u"lineuser")
        self.lineuser.setGeometry(QRect(30, 30, 241, 31))
        self.lineuser.setFont(font)
        self.linekey = QLineEdit(self.centralwidget)
        self.linekey.setObjectName(u"linekey")
        self.linekey.setGeometry(QRect(30, 90, 241, 31))
        self.linekey.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineuser, self.linekey)
        QWidget.setTabOrder(self.linekey, self.btnlogin)
        QWidget.setTabOrder(self.btnlogin, self.btnexit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btnlogin.setText(QCoreApplication.translate("MainWindow", u"Logar", None))
        self.btnexit.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
    # retranslateUi

