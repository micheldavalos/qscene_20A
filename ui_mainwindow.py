# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionMostrar = QAction(MainWindow)
        self.actionMostrar.setObjectName(u"actionMostrar")
        self.actionMas_Cercanos = QAction(MainWindow)
        self.actionMas_Cercanos.setObjectName(u"actionMas_Cercanos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.centralwidget)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.centralwidget)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout.addWidget(self.limpiar, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuPuntos = QMenu(self.menubar)
        self.menuPuntos.setObjectName(u"menuPuntos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPuntos.menuAction())
        self.menuPuntos.addAction(self.actionMostrar)
        self.menuPuntos.addAction(self.actionMas_Cercanos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.actionMas_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Mas Cercanos", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.menuPuntos.setTitle(QCoreApplication.translate("MainWindow", u"Puntos", None))
    # retranslateUi

