from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint
from pprint import pprint
from algoritmos import get_puntos, puntos_mas_cercanos

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        self.ui.actionMostrar.triggered.connect(self.mostrar_puntos)
        self.ui.actionMas_Cercanos.triggered.connect(self.puntos_mas_cercanos)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.puntos = []

    @Slot()
    def puntos_mas_cercanos(self):
        cercanos = puntos_mas_cercanos(self.puntos)
        pprint(cercanos)
        for punto1, punto2 in cercanos:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            # self.scene.addEllipse(x1, y1, 6, 6)
            # self.scene.addEllipse(x2, y2, 6, 6)
            self.scene.addLine(x1+3, y1+3, x2+3, y2+3)

    @Slot()
    def mostrar_puntos(self):
        self.puntos = get_puntos(10)
        pprint(self.puntos)
        for punto in self.puntos:
            x = punto[0]
            y = punto[1]
            self.scene.addEllipse(x, y, 6, 6)

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        print('dibujar')

        pen = QPen()
        pen.setWidth(2)

        for i in range(0, 100):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origen = randint(0, 500)
            y_origen = randint(0, 500)
            x_destin = randint(0, 500)
            y_destin = randint(0, 500)

            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
            self.scene.addEllipse(x_destin, y_destin, 6, 6, pen)
            self.scene.addLine(x_origen+3, y_origen+3, x_destin+3, y_destin+3, pen)


    @Slot()
    def limpiar(self):
        print('limpiar')
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())