from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton
import sys
from PyQt5 import uic


class Hello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.k = 1
        uic.loadUi('test.ui', self)
        self.fill = ''
        self.initial_palette()
        self.first = '1. В этом окне будут показаны координаты \n клеток,' \
                     ' которые нужно будет закрасить. \n Считайте началом координат верхний \n ' \
                     'левый угол. Чтобы закрасить клетку, \n нажмите на нее левой кнопкой \n ' \
                     'мыши.\n 2.(6, 5), (5, 6)' \
                     '\n3. Все клетки от (4,7) до (4,11) \n' \
                     '4. (5, 11), (6, 12) \n' \
                     '5. Все клетки от (7,13) до (11, 13) \n' \
                     '6. (12, 12), (13, 11) \n' \
                     '7. Все клетки от (14, 11) до (14, 7) \n' \
                     '8. (13, 6), (12, 5) \n' \
                     '9. Все клетки от (11, 6) до (7, 6) \n'
        self.read = []
        self.sp = []
        self.cat = []
        self.b = None
        self.c = ''
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 1100, 1800, 1100)
        self.setWindowTitle('тест')
        self.color.clicked.connect(self.change_color)
        self.messanges.clicked.connect(self.start_messanging)
        self.done.clicked.connect(self.ready)
        self.buttons()
        self.initial_palette()

    def check(self, x, y):
        coords = [(6, 5), (5, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 11), (6, 12), (8, 13), (9, 13),
                  (10, 13), (11, 13), (12, 12), (13, 11), (14, 11), (14, 10), (14, 9), (14, 8), (14, 7), (13, 6),
                  (12, 5), (11, 6), (10, 6), (9, 6), (8, 6), (7, 6), (7, 13)]
        for i in coords:
            if y == i[0] and x == i[1]:
                return True
        return False

    def buttons(self):
        x = 160
        y = 80
        for i in range(1, 17):
            for j in range(1, 18):
                self.b = QToolButton(self)
                self.b.resize(51, 51)
                self.b.move(x, y)
                self.b.clicked.connect(self.change_color1)
                if self.check(i, j):
                    self.cat.append(self.b)
                self.sp.append(self.b)
                x += 50
            x = 160
            y += 50
        for i in range(len(self.sp)):
            self.sp[i].clicked.connect(self.change_color1)

    def initial_palette(self):
        self.color.setStyleSheet("QWidget { background-color: #e9cbb5}")
        self.setStyleSheet("QWidget { background-color: #ffe6d6}")
        self.messanges.setStyleSheet("QWidget { background-color: #e9cbb5 }")
        self.label_3.setStyleSheet("QWidget { background-color: #ffe6d6}")
        self.result.setStyleSheet("QWidget { background-color: #ffe6d6}")
        self.done.setStyleSheet("QWidget { background-color: #ffe6d6}")
        self.c = '#ffe6d6'

    def change_color(self):
        self.k += 1
        if self.k % 5 == 0:
            self.initial_palette()
        elif self.k % 4 == 0:
            self.color.setStyleSheet("QWidget { background-color: #c94c4c }")
            self.setStyleSheet("QWidget { background-color: #b1cbbb}")
            self.messanges.setStyleSheet("QWidget { background-color: #c94c4c }")
            self.label_3.setStyleSheet("QWidget { background-color: #eea29a }")
            self.result.setStyleSheet("QWidget { background-color: #eea29a}")
            self.done.setStyleSheet("QWidget { background-color: #c94c4c}")
            self.c = 'b1cbbb'
        elif self.k % 3 == 0:
            self.color.setStyleSheet("QWidget { background-color: #ffef96 }")
            self.setStyleSheet("QWidget { background-color: #50394c}")
            self.messanges.setStyleSheet("QWidget { background-color: #ffef96 }")
            self.label_3.setStyleSheet("QWidget { background-color: #f4e1d2 }")
            self.result.setStyleSheet("QWidget { background-color: #f4e1d2}")
            self.done.setStyleSheet("QWidget { background-color: #ffef96}")
            self.c = '#50394c'
        elif self.k % 2 == 0:
            self.color.setStyleSheet("QWidget { background-color: #20B2AA }")
            self.setStyleSheet("QWidget { background-color: #FFA07A}")
            self.messanges.setStyleSheet("QWidget { background-color: #20B2AA }")
            self.label_3.setStyleSheet("QWidget { background-color: #90EE90 }")
            self.result.setStyleSheet("QWidget { background-color: #90EE90}")
            self.done.setStyleSheet("QWidget { background-color: #20B2AA}")
            self.c = '#FFA07A'
        elif self.k % 1 == 0:
            self.color.setStyleSheet("QWidget { background-color: #FFDAB9 }")
            self.setStyleSheet("QWidget { background-color: #DDA0DD }")
            self.messanges.setStyleSheet("QWidget { background-color: #FFDAB9 }")
            self.label_3.setStyleSheet("QWidget { background-color: #B0E0E6 }")
            self.result.setStyleSheet("QWidget { background-color: #B0E0E6}")
            self.done.setStyleSheet("QWidget { background-color: #FFDAB9}")
            self.c = '#DDA0DD'

    def start_messanging(self):
        self.label_3.setText(self.first)

    def change_color1(self):
        self.sender().setStyleSheet("QWidget { background-color: #df9e10}")
        self.sender().setText('.')

    def ready(self):
        flag = False
        for i in self.sp:
            if i.text() == '.':
                if i in self.cat:
                    continue
                else:
                    flag = True
                    break
        if not flag:
            self.result.setText('хочешь верь, хочешь нет, но у тебя получился кот.')
        else:
            self.result.setText('увы, вы не правильно следовали инструкции.')


app = QApplication(sys.argv)
ex = Hello()
ex.show()
sys.exit(app.exec())
