import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon


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
        self.toolbar.move(0, 40)
        self.toolbar.addAction(QIcon('venv/clipboard.png'), 'sad')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())