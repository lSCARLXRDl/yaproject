import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QComboBox, QLabel
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

        self.ag = QtWidgets.QActionGroup(self)
        self.ag.addAction(self.toolbar.addAction(icons.icon(icons.File), 'myFile'))
        self.ag.addAction(self.toolbar.addAction(icons.icon(icons.Folder), 'myFolder'))
        self.toolbar.addSeparator()
        self.ag.addAction(self.toolbar.addAction(icons.icon(icons.Trashcan), 'myTrash'))
        self.ag.setExclusive(1)

    def printAndSetCheck(action):
        action.setCheckable(1)
        action.setChecked(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())