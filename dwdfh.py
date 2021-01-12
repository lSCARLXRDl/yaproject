import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolBar, QLabel
from PyQt5.QtGui import QPainter, QColor, QMouseEvent, QImage, QIcon
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Paint')
        self.setStyleSheet("background-color: #c8d9cb;")
        self.can_resize = False
        self.can_save = False

        self.lbl = QLabel(self)
        self.lbl.move(200, 200)
        self.lbl.resize(200, 200)

        self.toolbar = QToolBar(self)
        self.toolbar.move(0, 25)
        self.toolbar.addAction(QIcon('venv/paste.ico'), 'Paste')
        self.toolbar.addAction(QIcon('venv/select.ico'), 'Select')
        #self.toolbar.addWidget(self.cb)
        self.toolbar.addSeparator()
        self.toolbar.addAction(QIcon('venv/pen.ico'), 'Pen')
        self.toolbar.addAction(QIcon('venv/eraser.ico'), 'Eraser')
        self.toolbar.addAction(QIcon('venv/fill.ico'), 'Fill')
        self.toolbar.addAction(QIcon('venv/text.ico'), 'Text')
        self.toolbar.addSeparator()

        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255,255,255))
        self.image.load('C:/Users/User/AppData/Roaming/Microsoft/Windows/Network Shortcuts/tsoy.jpg')

        self.show()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.flag = True
            self.paint = QPainter(self.image)
            self.ellips(e)
    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0,0, self.image)
    def mouseMoveEvent(self, e):
        if self.flag:
            print(e.pos())
            self.ellips(e)
    def ellips(self,e):
        if e.x() > 50:
            self.paint.setBrush(QColor('black'))
            self.paint.drawEllipse(e.pos(), 10,10)
            self.update()

app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())
