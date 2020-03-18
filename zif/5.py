import sqlite3
import sys, random
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QApplication, QPushButton, QLayoutItem
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QInputDialog, QColorDialog, QGridLayout, QWidgetItem
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QPolygon, QPixmap, QImage, QPalette, QIcon, QFont, QCursor
from PyQt5.QtCore import Qt, QPoint, QSize, QRect


class Window_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("Sapper")
        self.setWindowIcon(QIcon("bomb.jpg"))

        self.oImage = QImage("color.jpg")
        self.sImage = self.oImage.scaled(QSize(400, 500))
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.sImage))
        self.setPalette(self.palette)

        self.image_bomb = QPixmap("bomb_21.jpg")
        self.bomb_1.setPixmap(self.image_bomb)
        self.bomb_2.setPixmap(self.image_bomb)

        self.btn_List.setIcon(QIcon("cup.jpg"))
        self.btn_List.setStyleSheet("QPushButton {"
                                    "background-color: #AD41E5; "
                                    "border: none;"
                                    "}")
        self.btn_List.setIconSize(QSize(100, 100))
        self.btn_List.clicked.connect(self.spisok_popitok)

        self.name.setStyleSheet("QLabel {"
                                "color: #FFFB14"
                                "}")

        self.btn_easy.setStyleSheet("QPushButton {"
                                    "background-color: #FFAB23; "
                                    "border: 2px solid #000000; "
                                    " border-radius: 30px"
                                    "} "
                                    "QPushButton:hover {"
                                    "color: white;"
                                    "}")
        self.btn_easy.clicked.connect(self.easy)

        self.btn_normal.setStyleSheet("QPushButton {"
                                      "background-color: #FFAB23; "
                                      "border: 2px solid #000000; "
                                      "border-radius: 30px;"
                                      "} "
                                      "QPushButton:hover {"
                                      "color: white;"
                                      "}")
        self.btn_normal.clicked.connect(self.normal)

        self.btn_hard.setStyleSheet("QPushButton {"
                                    "background-color: #FFAB23; "
                                    "border: 2px solid #000000; "
                                    "border-radius: 30px;"
                                    "} "
                                    "QPushButton:hover {"
                                    "color: white;"
                                    "}")
        self.btn_hard.clicked.connect(self.hard)

        self.show()

    def spisok_popitok(self):
        self.hide()

        self.trys = Window_trys()
        self.trys.show()

    def easy(self):
        self.b = 10
        self.n = 10
        self.spis = [(i, j) for j in range(self.n) for i in range(self.n)]

        self.hide()

        self.game()

    def normal(self):
        self.b = 40
        self.n = 15
        self.spis = [(i, j) for j in range(self.n) for i in range(self.n)]

        self.hide()

        self.game()

    def hard(self):
        self.b = 100
        self.n = 20
        self.spis = [(i, j) for j in range(self.n) for i in range(self.n)]

        self.hide()

        self.game()

    def game(self):
        self.window_game = Window_game(self.b, self.n, self.spis)
        self.window_game.show()


class Window_game(QWidget):
    def __init__(self, b, n, spis):
        super().__init__()

        self.b = b
        self.n = n
        self.flag_onoff = -1
        self.s = 0
        self.h = 0
        self.f = 0
        self.lose = 0
        self.spisok = spis
        self.sp_min = [(self.x, self.y)]
        self.pict = 1

        self.siz = QSize()
        self.siz.setHeight(50)
        self.siz.setWidth(50)

        self.font = QFont()
        self.font.setFamily("Ms Shell Dlg 2")
        self.font.setPointSize(15)

        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)

        uic.loadUi("game.ui", self)

        self.glav_chast()

    def glav_chast(self):
        self.setWindowTitle("Sapper")
        self.setWindowIcon(QIcon("bomb.jpg"))

        self.oImage = QImage("color.jpg")
        self.sImage = self.oImage.scaled(QSize(400, 500))
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.sImage))
        self.setPalette(self.palette)

        self.btn_with_flag = Knopka()
        self.btn_with_flag.setCursor(QtCore.Qt.OpenHandCursor)
        self.btn_with_flag.setIcon(QIcon("flag_pom.jpg"))
        self.btn_with_flag.setIconSize(QSize(40, 40))
        self.btn_with_flag.setStyleSheet("QPushButton {"
                                         "background: #FFAB23; "
                                         "color: #FFAB23;"
                                         "}")
        self.btn_with_flag.clicked.connect(self.btn_push)

        self.btn_simple = Knopka()
        self.btn_simple.setCursor(QtCore.Qt.OpenHandCursor)
        self.btn_simple.setStyleSheet("QPushButton {"
                                      "background: #FFAB23; "
                                      "color: #FFAB23;"
                                      "}")
        self.btn_simple.clicked.connect(self.btn_push)

        self.label_kol_bombs.setText(str(self.b))

        self.label_flag_kol.setText(str(self.f))

        self.image_bomb = QPixmap("bomb_22.jpg")
        self.label_im_bomb.setPixmap(self.image_bomb)

        self.image_im_flag = QPixmap("flag_kol_2.jpg")
        self.label_im_flag.setPixmap(self.image_im_flag)

        self.image_clock = QPixmap("clock_3.png")
        self.label_clock.setPixmap(self.image_clock)

        self.btn_flag.setIcon(QIcon("flag_off_2.jpg"))
        self.btn_flag.setStyleSheet("QPushButton {"
                                    "background-color: #AD41E5; "
                                    "border: none;"
                                    "}"
                                    )
        self.btn_flag.setIconSize(QSize(100, 100))
        self.btn_flag.clicked.connect(self.onoff)

        self.label_hod.setText("Ход: " + str(self.h))

        self.come_to_menu.setStyleSheet("QPushButton {"
                                        "background: blue;"
                                        "color: black;"
                                        "border: 2px solid #000000;"
                                        "}"
                                        "QPushButton:hover {"
                                        "color: white;"
                                        "}")

        for i in range(self.n):
            for j in range(self.n):
                kn = Knopka(i, j)
                kn.setCursor(QtCore.Qt.OpenHandCursor)
                kn.setStyleSheet("QPushButton {"
                                 "background: #FFAB23; "
                                 "color: #FFAB23;"
                                 "width: 40;"
                                 "height: 40;"
                                 "}")
                kn.setMaximumSize(self.siz)
                kn.clicked.connect(self.btn_push)
                self.grid.addWidget(kn, i, j)

        self.grid.setSpacing(10)
        self.grid.setHorizontalSpacing(10)

        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

        self.come_to_menu.clicked.connect(self.comeback)

    def onoff(self):
        self.flag_onoff *= -1
        if self.flag_onoff == 1:
            self.btn_flag.setIcon(QIcon("flag_on_2.jpg"))
        else:
            self.btn_flag.setIcon(QIcon("flag_off_2.jpg"))

    def hod(self):
        self.h += 1
        self.label_hod.setText("Ход: " + str(self.h))

    def btn_push(self):
        btn = self.sender()
        if self.lose == 0:
            if self.flag_onoff == 1 and btn.name != "пусто":
                if btn.pict == 1:
                    btn.pict = 2
                    kn = Knopka(btn.x, btn.y, btn.pict, btn.name + "_флаг")
                    kn.setCursor(QtCore.Qt.OpenHandCursor)
                    kn.setIcon(QIcon("flag_pom.jpg"))
                    kn.setIconSize(QSize(40, 40))
                    kn.setStyleSheet("QPushButton {"
                                     "background: #FFAB23; "
                                     "color: #FFAB23;"
                                     "width: 40;"
                                     "height: 40;"
                                     "}")
                    kn.setMaximumSize(self.siz)
                    kn.clicked.connect(self.btn_push)
                    self.grid.removeWidget(btn)
                    self.grid.addWidget(kn, btn.x, btn.y)
                    self.f += 1
                    self.label_flag_kol.setText(str(self.f))
                else:
                    btn.pict = 1
                    if "мина" in btn.name:
                        name = "мина"
                    else:
                        name = "неизвестно"

                    kn = Knopka(btn.x, btn.y, btn.pict, name)
                    kn.setCursor(QtCore.Qt.OpenHandCursor)
                    kn.setStyleSheet("QPushButton {"
                                     "background: #FFAB23; "
                                     "color: #FFAB23;"
                                     "width: 40;"
                                     "height: 40;"
                                     "}")
                    kn.setMaximumSize(self.siz)
                    kn.clicked.connect(self.btn_push)
                    self.grid.removeWidget(btn)
                    self.grid.addWidget(kn, btn.x, btn.y)
                    self.f -= 1
                    self.label_flag_kol.setText(str(self.f))
            elif btn.pict == 1:
                if self.h == 0:
                    self.rasstanovka_bomb()
                    self.around(btn.x, btn.y)
                    self.hod()
                    if self.proverka_na_win():
                        self.hide()
                        self.restart(1)
                else:
                    self.hod()
                    if btn.name == "мина":
                        self.lose = 1
                        btn.setIcon(QIcon("bomb_2.jpg"))
                        if self.n == 10:
                            btn.setIconSize(QSize(90, 50))
                        elif self.n == 15:
                            btn.setIconSize(QSize(65, 35))
                        else:
                            btn.setIconSize(QSize(45, 25))
                    else:
                        self.around(btn.x, btn.y)
                    if self.proverka_na_win():
                        self.hide()
                        self.restart(1)

    def restart(self, k):
        self.window_restart = Window_restart(self.n, self.b, self.spisok, self.time, k)
        self.window_restart.show()

    def ryadom(self, x, y):
        t = 0
        if x + 1 < self.n:
            item = self.grid.itemAtPosition(x + 1, y)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if x - 1 >= 0:
            item = self.grid.itemAtPosition(x - 1, y)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if y + 1 < self.n:
            item = self.grid.itemAtPosition(x, y + 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if y - 1 >= 0:
            item = self.grid.itemAtPosition(x, y - 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if x + 1 < self.n and y + 1 < self.n:
            item = self.grid.itemAtPosition(x + 1, y + 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if x - 1 >= 0 and y - 1 >= 0:
            item = self.grid.itemAtPosition(x - 1, y - 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if x + 1 < self.n and y - 1 >= 0:
            item = self.grid.itemAtPosition(x + 1, y - 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1
        if x - 1 >= 0 and y + 1 < self.n:
            item = self.grid.itemAtPosition(x - 1, y + 1)
            btn = item.widget()
            if "мина" in btn.name:
                t += 1

        item = self.grid.itemAtPosition(x, y)
        btn = item.widget()

        if btn.name != "пусто":
            if t == 0:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: white;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("")
                btn.setMaximumSize(self.siz)
            elif t == 1:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: blue;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("1")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 2:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: green;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("2")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 3:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: brown;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("3")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 4:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: red;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("4")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 5:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: purple;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("5")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 6:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: pink;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("6")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 7:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: orange;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("7")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
            elif t == 8:
                btn.name = "пусто"
                btn.setStyleSheet("QPushButton {"
                                  "background: white; "
                                  "color: #69FFF5;"
                                  "width: 40;"
                                  "height: 40;"
                                  "}")
                btn.setText("8")
                btn.setFont(self.font)
                btn.setMaximumSize(self.siz)
        return t

    def around(self, x, y):
        if self.ryadom(x, y) == 0:
            if x + 1 < self.n:
                item = self.grid.itemAtPosition(x + 1, y)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x + 1, y)
            if x - 1 >= 0:
                item = self.grid.itemAtPosition(x - 1, y)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x - 1, y)
            if y + 1 < self.n:
                item = self.grid.itemAtPosition(x, y + 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x, y + 1)
            if y - 1 >= 0:
                item = self.grid.itemAtPosition(x, y - 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x, y - 1)
            if x + 1 < self.n and y + 1 < self.n:
                item = self.grid.itemAtPosition(x + 1, y + 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x + 1, y + 1)
            if x - 1 >= 0 and y - 1 >= 0:
                item = self.grid.itemAtPosition(x - 1, y - 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x - 1, y - 1)
            if x + 1 < self.n and y - 1 >= 0:
                item = self.grid.itemAtPosition(x + 1, y - 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x + 1, y - 1)
            if x - 1 >= 0 and y + 1 < self.n:
                item = self.grid.itemAtPosition(x - 1, y + 1)
                btn = item.widget()
                if btn.name == "неизвестно":
                    self.around(x - 1, y + 1)

    def proverka_na_win(self):
        ans = 1
        for i in range(self.n):
            for j in range(self.n):
                item = self.grid.itemAtPosition(i, j)
                btn = item.widget()
                if "неизвестно" in btn.name:
                    ans = 0
                    break
            if ans == 0:
                break
        return ans

    def rasstanovka_bomb(self):
        while len(self.sp_min) != self.b + 1:
            k = random.choice(self.spisok)
            if k not in self.sp_min:
                item = self.grid.itemAtPosition(k[0], k[1])
                btn = item.widget()
                btn.name = "мина"
                self.sp_min.append(k)

    def game_over(self):
        time = self.time
        time_over = time.addSecs(90000000)
        while time.toString("hh:mm:ss") != time_over.toString("hh:mm:ss"):
            time = time.addSecs(1)

    def timerEvent(self):
        if self.lose == 0:
            self.time = self.time.addSecs(1)
            self.label_time.setText(self.time.toString("hh:mm:ss"))
        else:
            if self.s == 0:
                self.s = 1
                self.game_over()
                self.hide()
                self.restart(2)

    def comeback(self):
        self.hide()
        self.window_menu = Window_menu()
        self.window_menu.show()


class Knopka(QPushButton):
    def __init__(self, x=0, y=0, pict=1, name="неизвестно"):
        super().__init__()
        self.x = x
        self.y = y
        self.pict = pict
        self.name = name


class Window_trys(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("trys.ui", self)
        self.see()

    def see(self):
        con = sqlite3.connect("results.db")
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM result""").fetchall()


class Window_restart(QWidget):
    def __init__(self, n, b, spis, time, k):
        super().__init__()
        self.n = n
        self.b = b
        self.spis = spis
        self.k = k
        uic.loadUi("quastion.ui", self)
        self.label_time.setText(time.toString("hh:mm:ss"))
        self.quastion()

    def quastion(self):
        self.setWindowTitle("Sapper")
        self.setWindowIcon(QIcon("bomb.jpg"))

        self.oImage = QImage("color.jpg")
        self.sImage = self.oImage.scaled(QSize(400, 500))
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.sImage))
        self.setPalette(self.palette)

        if self.k == 1:
            self.label_2.setText("You win")
        else:
            self.label_2.setText("You lose")

        self.label.setStyleSheet("QLabel {"
                                 "background: #F40E76;"
                                 "color: white;"
                                 "}")

        self.image_clock = QPixmap("clock_2.png")
        self.label_clock.setPixmap(self.image_clock)

        self.menu.setStyleSheet("QPushButton {"
                                "background: blue;"
                                "color: black;"
                                "border: 2px solid #000000;"
                                "}"
                                "QPushButton:hover {"
                                "color: white;"
                                "}")
        self.menu.clicked.connect(self.comeback)

        self.restrt.setStyleSheet("QPushButton {"
                                  "background: #00FF00;"
                                  "color: black;"
                                  "border: 2px solid #000000;"
                                  "}"
                                  "QPushButton:hover {"
                                  "color: white;"
                                  "}")
        self.restrt.clicked.connect(self.game)

    def comeback(self):
        self.hide()
        self.window_menu = Window_menu()
        self.window_menu.show()

    def game(self):
        self.hide()
        self.window_game = Window_game(self.b, self.n, self.spis)
        self.window_game.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kal = Window_menu()
    sys.exit(app.exec())
# SQLiteStodio
