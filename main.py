import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QComboBox, QLabel, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Paint')

        self.menubar = QMenuBar(self)
        self.menubar.addMenu('Файл')
        self.menubar.addMenu('Главная')
        self.menubar.addMenu('Вид')

        self.toolbar = QToolBar(self)
        self.toolbar.move(0, 30)
        icons = QtWidgets.QFileIconProvider()

        self.cb = QComboBox(self)
        self.cb.setFixedSize(50, 30)
        self.cb.addItems(['', '', ''])
        self.cb.setItemIcon(0, QIcon('venv/rotate.ico'))
        self.cb.setItemIcon(1, QIcon('venv/rotate_right.ico'))
        self.cb.setItemIcon(2, QIcon('venv/rotate_left.ico'))

        self.toolbar.addAction(QIcon('venv/paste.ico'), 'Paste')
        self.toolbar.addAction(QIcon('venv/select.ico'), 'Select')
        self.toolbar.addWidget(self.cb)
        self.toolbar.addSeparator()
        self.toolbar.addAction(QIcon('venv/pen.ico'), 'Pen')
        self.toolbar.addAction(QIcon('venv/eraser.ico'), 'Eraser')
        self.toolbar.addAction(QIcon('venv/fill.ico'), 'Fill')
        self.toolbar.addAction(QIcon('venv/text.ico'), 'Text')
        self.toolbar.addSeparator()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())