from PyQt5 import QtGui

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
R=185
G=57
B=65
class PaintWidget(QWidget):
    def __init__(self,parent=None,r=0,g=0,b=255,width=0,height=0):
        super().__init__(parent)
        self.r = r
        self.g = g
        self.b = b
        self.width = width
        self.height = height

    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.black)

        # Colored rectangles
        qp.setBrush(QColor(self.r, self.g, self.b))
        qp.drawRect(0, 0,  self.width,self.height)

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
        painter.rotate(-90)
        if self.text:
            painter.drawText(0, 0, self.text)
        painter.end()


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label1 = MyLabel("INGREDIENT",170,30)
        self.label1.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = MyLabel("BEER",163,30)
        self.label2.setStyleSheet("font-size: 40px;font-weight: 300;line-height: 0.62;text-align: center;color: rgb(255, 255, 255);")

        pixmap = QPixmap('raspberry-icon.png')
        transform = QTransform().rotate(-90)
        pixmap = pixmap.transformed(transform)
        self.icon = QLabel()

        self.icon.setPixmap(pixmap)

        hBoxLayout = QHBoxLayout()

        hBoxLayout.addWidget(self.icon)
        hBoxLayout.addWidget(self.label1)
        hBoxLayout.addWidget(self.label2)
        self.setLayout(hBoxLayout)
        self.showFullScreen()

        palette = self.palette()
        role = self.backgroundRole()
        color = QColor()

        palette.setColor(role, color.fromRgb(R, G, B))
        self.setPalette(palette)



def buttonClicked(self):
    pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
