import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QComboBox, QLabel, QAction
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Paint')
        self.setStyleSheet("background-color: #c8d9cb;")
        self.color = '#000000'

        self.menubar = QMenuBar(self)
        self.menubar.addMenu('Файл')
        self.menubar.addMenu('Главная')
        self.menubar.addMenu('Вид')
        self.menubar.setStyleSheet("background-color: white;")

        self.toolbar = QToolBar(self)
        self.toolbar.move(0, 25)

        self.lb = QLabel(self)
        self.lb.resize(330, 43)
        self.lb.move(377, 25)
        self.lb.setStyleSheet("background-color: white;")

        self.paint_lbl = QLabel(self)
        self.paint_lbl.resize(650, 400)
        self.paint_lbl.move(20, 80)
        self.paint_lbl.setStyleSheet("background-color: white; border-style: solid;"
                                     " border-width: 2px; border-color: black;")

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

        self.lbl = QLabel()
        self.lbl.setFixedSize(30, 30)
        self.lbl.setStyleSheet("background-color: black; border-style: solid; border-width: 2px; border-color: black;")
        self.toolbar.addWidget(self.lbl)

        a = self.toolbar.addAction(QIcon('venv/color.ico'), 'Select color')
        a.triggered.connect(self.click1)

        self.toolbar.setStyleSheet("background-color: white;")

    def click1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl.setStyleSheet(
                f"background-color: {color.name()}; border-style: solid; border-width: 2px; border-color: black;")
            self.color = color.name()
            print(self.color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())