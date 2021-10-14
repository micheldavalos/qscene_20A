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
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 4)

        self.limpiar = QPushButton(self.groupBox)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_2.addWidget(self.limpiar, 1, 2, 1, 2)

        self.dibujar = QPushButton(self.groupBox)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_2.addWidget(self.dibujar, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.spinBox_puntos = QSpinBox(self.groupBox_2)
        self.spinBox_puntos.setObjectName(u"spinBox_puntos")
        self.spinBox_puntos.setMinimum(2)
        self.spinBox_puntos.setMaximum(10000)

        self.horizontalLayout_2.addWidget(self.spinBox_puntos)

        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(10000)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QScene", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Puntos a generar:", None))
        self.menuPuntos.setTitle(QCoreApplication.translate("MainWindow", u"Puntos", None))
    # retranslateUi

