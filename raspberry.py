from PyQt5 import QtGui

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep
R=185
G=57
B=65
drink_type = "None"
kalori = "0"
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
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label1 = MyLabel("INGREDIENT",48,30)
        self.label1.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = MyLabel(drink_type,57,27)
        self.label2.setStyleSheet("font-size: 40px;font-weight: 300;line-height: 0.62;text-align: center;color: rgb(255, 255, 255);")

        self.label3 = MyLabel(kalori+"kcal",50,20)
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

        self.setLayout(hBoxLayout)
        self.showFullScreen()

        palette = self.palette()
        role = self.backgroundRole()
        color = QColor()
        palette.setColor(role, color.fromRgb(B, G, R))
        self.setPalette(palette)
class Second(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label1 = MyLabel("INGREDIENT",48,30)
        self.label1.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = MyLabel("BEER",57,30)
        self.label2.setStyleSheet("font-size: 40px;font-weight: 300;line-height: 0.62;text-align: center;color: rgb(255, 255, 255);")

        hBoxLayout = QHBoxLayout()


        hBoxLayout.addWidget(self.label2)

        hBoxLayout.addWidget(self.label1)

        self.setLayout(hBoxLayout)
        self.showFullScreen()

        palette = self.palette()
        role = self.backgroundRole()
        color = QColor()
        palette.setColor(role, color.fromRgb(B, G, R))
        self.setPalette(palette)


def buttonClicked(self):
    pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    first = First()
    second = Second()
    i = 0
    first_check = False
    while True:
        if first_check:
            sleep(3)
        else:
            first_check=True
        if i%2:
            first.show()
            second.hide()
        else:
            second.show()
            first.hide()

        i = (i+1)%2

    sys.exit(app.exec_())
