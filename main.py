import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QComboBox, QLabel, QSlider
from PyQt5.QtWidgets import QColorDialog, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPainter, QPen, QBrush, QFont, QKeyEvent, QTransform, QClipboard
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QPainter, QColor, QGuiApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Paint')
        self.setStyleSheet("background-color: #c8d9cb;")
        self.can_resize = False
        self.can_save = False

        self.background = Qt.white

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(self.background)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.LastPoint = QPoint()
        self.act = 1

        self.mewo = QLabel(self)
        self.mewo.resize(700, 70)
        self.mewo.move(0, 0)
        self.mewo.setStyleSheet("background-color: white;")

        self.menubar = QMenuBar(self)
        self.menu_file = self.menubar.addMenu('Файл')
        self.menu_file.addAction('Открыть').triggered.connect(self.open_file)
        self.menu_file.addAction('Создать новый').triggered.connect(self.create_new)
        self.menu_file.addAction('Сохранить').triggered.connect(self.save)
        self.menu_view = self.menubar.addAction('Тема')
        self.menu_view.triggered.connect(self.view_f)
        self.menubar.setStyleSheet("background-color: white;")

        self.toolbar = QToolBar(self)
        self.toolbar.move(0, 20)

        self.lb1 = QLabel(self)
        self.lb1.resize(40, 440)
        self.lb1.move(0, 70)
        self.lb1.setStyleSheet("background-color: #c8d9cb;")

        self.lb2 = QLabel(self)
        self.lb2.resize(700, 20)
        self.lb2.move(0, 70)
        self.lb2.setStyleSheet("background-color: #c8d9cb;")

        self.lb3 = QLabel(self)
        self.lb3.resize(40, 440)
        self.lb3.move(660, 70)
        self.lb3.setStyleSheet("background-color: #c8d9cb;")

        self.lb4 = QLabel(self)
        self.lb4.resize(700, 20)
        self.lb4.move(0, 480)
        self.lb4.setStyleSheet("background-color: #c8d9cb;")

        paste = self.toolbar.addAction(QIcon('data/paste.ico'), 'Paste')
        paste.triggered.connect(self.paste)
        rot1 = self.toolbar.addAction(QIcon('data/rotate_right.ico'), 'Rotate')
        rot1.triggered.connect(self.rotate1)
        rot2 = self.toolbar.addAction(QIcon('data/rotate_left.ico'), 'Rotate')
        rot2.triggered.connect(self.rotate2)
        self.toolbar.addSeparator()
        pen = self.toolbar.addAction(QIcon('data/pen.ico'), 'Pen')
        pen.triggered.connect(self.click_act1)
        eraser = self.toolbar.addAction(QIcon('data/eraser.ico'), 'Eraser')
        eraser.triggered.connect(self.click_act2)
        self.toolbar.addAction(QIcon('data/fill.ico'), 'Fill')
        text = self.toolbar.addAction(QIcon('data/text.ico'), 'Text')
        text.triggered.connect(self.click_act3)
        self.toolbar.addSeparator()

        self.lbl = QLabel()
        self.lbl.setFixedSize(30, 30)
        self.lbl.setStyleSheet("background-color: black; border-style: solid; border-width: 2px; border-color: black;")
        self.toolbar.addWidget(self.lbl)

        a = self.toolbar.addAction(QIcon('data/color.ico'), 'Select color')
        a.triggered.connect(self.click1)

        self.toolbar.setStyleSheet("background-color: white;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and 660 > event.x() > 40 and 480 > event.y() > 90:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing and 660 > event.x() > 40 and 480 > event.y() > 90:
            if self.act == 1:
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawLine(self.lastPoint, event.pos())
                self.lastPoint = event.pos()
                self.update()
            elif self.act == 2:
                painter = QPainter(self.image)
                painter.setPen(QPen(Qt.white, 15, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawLine(self.lastPoint, event.pos())
                self.lastPoint = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def click_act1(self):
        self.act = 1

    def click_act2(self):
        self.act = 2

    def click_act3(self):
        self.act = 3

    def paste(self):
        clipboard = QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()
        self.image = mimeData.imageData()
        self.update()

    def rotate1(self):
        my_transform = QTransform()
        my_transform.rotate(90)
        self.image = self.image.transformed(my_transform)
        self.update()

    def rotate2(self):
        my_transform = QTransform()
        my_transform.rotate(-90)
        self.image = self.image.transformed(my_transform)
        self.update()

    def click1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl.setStyleSheet(
                f"background-color: {color.name()}; border-style: solid; border-width: 2px; border-color: black;")
            self.brushColor = color.toRgb()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.image.load(fname)

    def create_new(self):
        self.act = 1
        self.brushColor = Qt.black
        self.lbl.setStyleSheet(
            f"background-color: black; border-style: solid; border-width: 2px; border-color: black;")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(self.background)
        self.update()

    def save_file(self):
        if self.can_save:
            filename = QFileDialog.getSaveFileName(self, 'Save file', '', '*.png;;*.jpg')
            if len(filename[0]) != 0:
                self.pixmap.save(filename[0], filename[1][2:])

    def view_f(self):
        self.id = QInputDialog(self)
        color, ok_pressed = self.id.getItem(
            self, "Смена темы", "Выберите тему",
            ("Классический", "Красный", "Жёлтый"), 0, False)
        if color == "Классический":
            self.setStyleSheet("background-color: #c8d9cb;")
            self.lb1.setStyleSheet("background-color: #c8d9cb;")
            self.lb2.setStyleSheet("background-color: #c8d9cb;")
            self.lb3.setStyleSheet("background-color: #c8d9cb;")
            self.lb4.setStyleSheet("background-color: #c8d9cb;")
        elif color == "Красный":
            self.setStyleSheet("background-color: red;")
            self.lb1.setStyleSheet("background-color: red;")
            self.lb2.setStyleSheet("background-color: red;")
            self.lb3.setStyleSheet("background-color: red;")
            self.lb4.setStyleSheet("background-color: red;")
        elif color == "Жёлтый":
            self.setStyleSheet("background-color: #f6ff42;")
            self.lb1.setStyleSheet("background-color: #f6ff42;")
            self.lb2.setStyleSheet("background-color: #f6ff42;")
            self.lb3.setStyleSheet("background-color: #f6ff42;")
            self.lb4.setStyleSheet("background-color: #f6ff42;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())