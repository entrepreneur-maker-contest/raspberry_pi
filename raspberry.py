from PyQt5 import QtGui

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
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
        self.label1.move(30, 204.5)
        self.label1.setFont(QtGui.QFont("Gothic",20,QtGui.QFont.Bold))
        self.label1.setStyleSheet("width: 180px;height: 18px;font-size: 20px;font-weight: 300;text-align: center;color: rgb(255, 255, 255);")

        self.label2 = QLabel("BEER", self)
        self.label2.move(10, 30)

        self.label3 = QLabel("", self)
        self.label3.move(10, 50)
        self.setWindowTitle("시음")


def buttonClicked(self):
    pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
