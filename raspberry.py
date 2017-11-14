from PyQt5 import QtGui

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep

con = ((65, 155, 249),(105, 57, 57),(185, 57, 65))
first = None
second = None

def setRGB(first,r,g,b):
    R = r
    G = g
    B = b
    palette = first.palette()
    role = first.backgroundRole()
    color = QColor()
    palette.setColor(role, color.fromRgb(B, G, R))
    first.setPalette(palette)
def setkalori(first,kal):
    kalori = kal
    first = 30

def setType():
    caefein = 20
    suger = 40
    water = 50

class MyLabel(QLabel):
    def __init__(self, text=None,width=0,height=0):
        super(self.__class__, self).__init__()
        self.text = text
        self.width=width
        self.height=height
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white)
        painter.translate( self.height,self.width)
        painter.rotate(90)
        if self.text:
            painter.drawText(0, 0, self.text)
        painter.end()


class First(QWidget):
    def __init__(self, parent=None,drink_type="none",kalori=0,_color = 0):
        super().__init__(parent)

        self.label1 = MyLabel("INGREDIENT",48,30)
        self.label1.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = MyLabel(drink_type,57,27)
        self.label2.setStyleSheet("font-size: 40px;font-weight: 300;line-height: 0.62;text-align: center;color: rgb(255, 255, 255);")

        self.label3 = MyLabel(str(kalori)+"kcal",50,20)
        self.label3.setStyleSheet("font-size: 10px;font-weight: 500;text-align: center;color: rgb(255, 255, 255);")

        pixmap = QPixmap('raspberry-icon.png')
        transform = QTransform().rotate(90)
        pixmap = pixmap.transformed(transform)
        self.icon = QLabel()

        self.icon.setPixmap(pixmap)

        hBoxLayout = QHBoxLayout()


        hBoxLayout.addWidget(self.label3)

        hBoxLayout.addWidget(self.label2)

        hBoxLayout.addWidget(self.label1)

        hBoxLayout.addWidget(self.icon)
        palette = self.palette()
        role = self.backgroundRole()
        color = QColor()
        B=con[_color][2]
        R=con[_color][0]
        G=con[_color][1]
        palette.setColor(role, color.fromRgb(B, G, R))
        self.setPalette(palette)

        self.setLayout(hBoxLayout)
        self.showFullScreen()
        self.keyPressEvent = self.newkey

    def newkey(self, event):
        key = event.key()

        if key == Qt.Key_2:
            global second
            second = Second(water=486,cafein=0,sugar=0,_color = 0)
            self.hide()
        if key == Qt.Key_4:
            second = Second(water=327, cafein=0, sugar=0,_color = 0)
            self.hide()
        if key == Qt.Key_6:
            second = Second(water=416, cafein=166.4, sugar=0,_color=1)
            self.hide()
        if key == Qt.Key_8:
            second = Second(water=546, cafein=43.6, sugar=57646,_color = 2)
            self.hide()
class Second(QWidget):
    def __init__(self, parent=None,water=0,cafein=0,sugar=0,_color=0):
        super().__init__(parent)

        self.label1 = MyLabel("water",48,30)
        self.label1.setStyleSheet("font-size: 15px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = MyLabel(str(water)+"mL",57,30)
        self.label2.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label3 = MyLabel("caffein", 48, 30)
        self.label3.setStyleSheet("font-size: 15px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label4 = MyLabel(str(cafein)+"mg", 57, 30)
        self.label4.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label5 = MyLabel("sugar", 48, 30)
        self.label5.setStyleSheet("font-size: 15px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label6 = MyLabel(str(sugar)+"mg", 57, 30)
        self.label6.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        hBoxLayout = QHBoxLayout()


        hBoxLayout.addWidget(self.label6)

        hBoxLayout.addWidget(self.label5)

        hBoxLayout.addWidget(self.label4)

        hBoxLayout.addWidget(self.label3)

        hBoxLayout.addWidget(self.label2)

        hBoxLayout.addWidget(self.label1)


        palette = self.palette()
        role = self.backgroundRole()
        color = QColor()
        B = con[_color][2]
        R = con[_color][0]
        G = con[_color][1]
        palette.setColor(role, color.fromRgb(B, G, R))
        self.setPalette(palette)

        self.setLayout(hBoxLayout)
        self.showFullScreen()

        self.keyPressEvent = self.newkey


    def newkey(self, event):
        key = event.key()
        if key == Qt.Key_1:
            first = First(drink_type="water",kalori=0,_color = 0)
            self.hide()
        elif key == Qt.Key_3:
            first = First(drink_type="water",kalori=0,_color = 0)
            self.hide()
        elif key == Qt.Key_5:
            first = First(drink_type="coffee",kalori=2,_color = 1)
            self.hide()
        elif key == Qt.Key_7:
            first = First(drink_type="coke", kalori=205, _color =2)
            self.hide()

def buttonClicked(self):
    pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    first = First(drink_type="water",kalori=0)


    sys.exit(app.exec_())
