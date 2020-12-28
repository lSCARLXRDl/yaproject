import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QComboBox, QLabel, QAction, QSlider
from PyQt5.QtWidgets import QColorDialog, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPainter, QColor, QPainterPath

Color = '#000000'

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

        self.menubar = QMenuBar(self)
        self.menu_file = self.menubar.addMenu('Файл')
        self.menu_file.addAction('Открыть').triggered.connect(self.open_file)
        self.menu_file.addAction('Создать новый').triggered.connect(self.create_new)
        self.menu_file.addAction('Сохранить').triggered.connect(self.save_file)
        self.menu_view = self.menubar.addAction('Тема')
        self.menu_view.triggered.connect(self.view_f)
        self.menubar.setStyleSheet("background-color: white;")

        self.toolbar = QToolBar(self)
        self.toolbar.move(0, 20)

        self.lb = QLabel(self)
        self.lb.resize(370, 37)
        self.lb.move(330, 20)
        self.lb.setStyleSheet("background-color: white;")

        self.paint_lbl_height = 380
        self.paint_lbl = QLabel(self)
        self.paint_lbl.resize(650, self.paint_lbl_height)
        self.paint_lbl.move(20, 80)
        self.paint_lbl.setStyleSheet("background-color: white; border-style: solid;"
                                     " border-width: 2px; border-color: black;")

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.resize(300, 20)
        self.sld.move(370, 470)
        self.sld.setStyleSheet("""
                    QSlider{
                        background: #c8d9cb;
                    }
                    QSlider::groove:horizontal {  
                        height: 10px;
                        margin: 0px;
                        border-radius: 5px;
                        background: #B0AEB1;
                    }
                    QSlider::handle:horizontal {
                        background: #fff;
                        border: 1px solid #E3DEE2;
                        width: 17px;
                        margin: -5px 0; 
                        border-radius: 8px;
                    }
                    QSlider::sub-page:qlineargradient {
                        background: #3B99FC;
                        border-radius: 5px;
                    }
                """)
        self.sld.valueChanged[int].connect(self.changeValue)

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
        global Color
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl.setStyleSheet(
                f"background-color: {color.name()}; border-style: solid; border-width: 2px; border-color: black;")
            Color = color.name()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(fname)
        self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
        self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
        self.paint_lbl.setPixmap(self.pixmap)
        self.can_resize = True
        self.can_save = True

    def changeValue(self, value):
        if value > 0 and value < 10:
            if self.can_resize:
                self.paint_lbl_height = 200
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(344, 200)
        if value > 10 and value < 20:
            if self.can_resize:
                self.paint_lbl_height = 220
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(379, 220)
        elif value > 20 and value < 30:
            if self.can_resize:
                self.paint_lbl_height = 240
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(413, 240)
        elif value > 30 and value < 40:
            if self.can_resize:
                self.paint_lbl_height = 260
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(448, 260)
        elif value > 40 and value < 50:
            if self.can_resize:
                self.paint_lbl_height = 280
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(482, 280)
        elif value > 50 and value < 60:
            if self.can_resize:
                self.paint_lbl_height = 300
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(517, 300)
        elif value > 60 and value < 70:
            if self.can_resize:
                self.paint_lbl_height = 320
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(551, 320)
        elif value > 70 and value < 80:
            if self.can_resize:
                self.paint_lbl_height = 340
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(586, 340)
        elif value > 80 and value < 90:
            if self.can_resize:
                self.paint_lbl_height = 360
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(620, 360)
        elif value > 90 and value < 100:
            if self.can_resize:
                self.paint_lbl_height = 380
                self.pixmap = self.pixmap.scaledToHeight(self.paint_lbl_height)
                self.paint_lbl.resize(self.pixmap.width(), self.paint_lbl_height)
                self.paint_lbl.setPixmap(self.pixmap)
            else:
                self.paint_lbl.resize(650, 380)

    def create_new(self):
        self.paint_lbl_height = 380
        self.paint_lbl.resize(650, self.paint_lbl_height)
        self.paint_lbl.clear()
        self.can_resize = False
        self.color = '#000000'

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
            self.menubar.setStyleSheet(
                """
                QMenuBar
                {
                    background-color: #c8d9cb;
                    color: black;
                }
                QMenuBar::item
                {
                    background-color: white;
                    color: black;
                }
                QMenuBar::item::selected
                {
                    background-color: #def9ff;
                    color: black;
                }
                 """)
            self.paint_lbl.setStyleSheet("background-color: white; border-style: solid;"
                                         " border-width: 2px; border-color: black;")
            self.sld.setStyleSheet("""
                                QSlider{
                                    background: #c8d9cb;
                                }
                                QSlider::groove:horizontal {  
                                    height: 10px;
                                    margin: 0px;
                                    border-radius: 5px;
                                    background: #B0AEB1;
                                }
                                QSlider::handle:horizontal {
                                    background: #fff;
                                    border: 1px solid #E3DEE2;
                                    width: 17px;
                                    margin: -5px 0; 
                                    border-radius: 8px;
                                }
                                QSlider::sub-page:qlineargradient {
                                    background: #3B99FC;
                                    border-radius: 5px;
                                }
                            """)
        elif color == "Красный":
            self.setStyleSheet("background-color: red;")
            self.menubar.setStyleSheet(
                """
                QMenuBar
                {
                    background-color: red;
                    color: black;
                }
                QMenuBar::item
                {
                    background-color: white;
                    color: black;
                }
                QMenuBar::item::selected
                {
                    background-color: #def9ff;
                    color: black;
                }
                 """)
            self.paint_lbl.setStyleSheet("background-color: white; border-style: solid;"
                                         " border-width: 2px; border-color: black;")
            self.sld.setStyleSheet("""
                                QSlider{
                                    background: red;
                                }
                                QSlider::groove:horizontal {  
                                    height: 10px;
                                    margin: 0px;
                                    border-radius: 5px;
                                    background: #B0AEB1;
                                }
                                QSlider::handle:horizontal {
                                    background: #fff;
                                    border: 1px solid #E3DEE2;
                                    width: 17px;
                                    margin: -5px 0; 
                                    border-radius: 8px;
                                }
                                QSlider::sub-page:qlineargradient {
                                    background: #3B99FC;
                                    border-radius: 5px;
                                }
                            """)
        elif color == "Жёлтый":
            self.setStyleSheet("background-color: #f6ff42;")
            self.menubar.setStyleSheet(
                """
                QMenuBar
                {
                    background-color: #f6ff42;
                    color: black;
                }
                QMenuBar::item
                {
                    background-color: white;
                    color: black;
                }
                QMenuBar::item::selected
                {
                    background-color: #def9ff;
                    color: black;
                }
                 """)
            self.paint_lbl.setStyleSheet("background-color: white; border-style: solid;"
                                         " border-width: 2px; border-color: black;")
            self.sld.setStyleSheet("""
                                QSlider{
                                    background: #f6ff42;
                                }
                                QSlider::groove:horizontal {  
                                    height: 10px;
                                    margin: 0px;
                                    border-radius: 5px;
                                    background: #B0AEB1;
                                }
                                QSlider::handle:horizontal {
                                    background: #fff;
                                    border: 1px solid #E3DEE2;
                                    width: 17px;
                                    margin: -5px 0; 
                                    border-radius: 8px;
                                }
                                QSlider::sub-page:qlineargradient {
                                    background: #3B99FC;
                                    border-radius: 5px;
                                }
                            """)


class Label(QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent=parent)
        self.flag = False
        self._im = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.flag = True
            self.xx = e.x()
            self.yy = e.y()
            self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(Color))
            qp.drawEllipse(self.xx - 15, self.yy - 15, 30, 30)
            self.update()
            qp.end()

    def mouseMoveEvent(self, e):
        if self.flag:
            self.xx = e.x()
            self.yy = e.y()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())