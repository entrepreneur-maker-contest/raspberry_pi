from PyQt5 import QtGui

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
percentage = 50
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
        size = self.size()

        # Colored rectangles
        qp.setBrush(QColor(self.r, self.g, self.b))
        qp.drawRect(0, 0, self.width, self.height)


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(0,0,480,320)
        self.m = PaintWidget(self,r=253,g=197,b=85,width=self.width(),height=self.height())
        self.m.move(0,0)
        self.m.resize(self.width(),self.height())
        self.label1 = QLabel("INGREDIENT", self)
        self.label1.move(70, 204.5)
        self.label1.setStyleSheet("font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")
        self.label1.resize(180,18)

        self.label2 = QLabel("BEER", self)
        self.label2.move(77, 248.5)
        self.label2.resize(180,30)
        self.label2.setStyleSheet("font-size: 40px;font-weight: 300;line-height: 0.62;text-align: center;color: rgb(255, 255, 255);")

        self.icon = QLabel(self)
        pixmap = QPixmap('raspberry-icon.png')
        self.icon.setPixmap(pixmap)

        # Optional, resize window to image size
        self.icon.resize(pixmap.width(), pixmap.height())
        self.icon.move(88,57.5)

        self.showFullScreen()

def buttonClicked(self):
    pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
