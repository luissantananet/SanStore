# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MenuPrincipal.sizePolicy().hasHeightForWidth())
        MenuPrincipal.setSizePolicy(sizePolicy)
        self.actionProdutos = QAction(MenuPrincipal)
        self.actionProdutos.setObjectName(u"actionProdutos")
        self.actionClientes = QAction(MenuPrincipal)
        self.actionClientes.setObjectName(u"actionClientes")
        self.actionCaixa = QAction(MenuPrincipal)
        self.actionCaixa.setObjectName(u"actionCaixa")
        self.actionEstoque = QAction(MenuPrincipal)
        self.actionEstoque.setObjectName(u"actionEstoque")
        self.actionUser = QAction(MenuPrincipal)
        self.actionUser.setObjectName(u"actionUser")
        self.actionCalculando_Markup = QAction(MenuPrincipal)
        self.actionCalculando_Markup.setObjectName(u"actionCalculando_Markup")
        self.centralwidget = QWidget(MenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MenuPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuCadastros = QMenu(self.menubar)
        self.menuCadastros.setObjectName(u"menuCadastros")
        self.menuOperacional = QMenu(self.menubar)
        self.menuOperacional.setObjectName(u"menuOperacional")
        self.menuRelatorios = QMenu(self.menubar)
        self.menuRelatorios.setObjectName(u"menuRelatorios")
        MenuPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MenuPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        MenuPrincipal.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuOperacional.menuAction())
        self.menubar.addAction(self.menuRelatorios.menuAction())
        self.menuCadastros.addAction(self.actionProdutos)
        self.menuCadastros.addAction(self.actionClientes)
        self.menuCadastros.addAction(self.actionUser)
        self.menuOperacional.addAction(self.actionCaixa)
        self.menuOperacional.addAction(self.actionEstoque)

        self.retranslateUi(MenuPrincipal)

        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"Menu Principal", None))
        self.actionProdutos.setText(QCoreApplication.translate("MenuPrincipal", u"Produtos", None))
        self.actionClientes.setText(QCoreApplication.translate("MenuPrincipal", u"Clientes", None))
        self.actionCaixa.setText(QCoreApplication.translate("MenuPrincipal", u"Caixa", None))
        self.actionEstoque.setText(QCoreApplication.translate("MenuPrincipal", u"Estoque", None))
        self.actionUser.setText(QCoreApplication.translate("MenuPrincipal", u"Usu\u00e1rio", None))
        self.actionCalculando_Markup.setText(QCoreApplication.translate("MenuPrincipal", u"Calculando Markup", None))
        self.menuCadastros.setTitle(QCoreApplication.translate("MenuPrincipal", u"Cadastros", None))
        self.menuOperacional.setTitle(QCoreApplication.translate("MenuPrincipal", u"Operacional", None))
        self.menuRelatorios.setTitle(QCoreApplication.translate("MenuPrincipal", u"Relat\u00f3rios", None))
    # retranslateUi

