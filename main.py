from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.get_inform.clicked.connect(self.view_information)

    def view_information(self):
        con = sqlite3.connect('coffee.sqlite.db')
        cur = con.cursor()
        result = cur.execute('''SELECT * from cofes''').fetchall()
        for i in result:
            for j in range(len(i)):
                self.coffee_table.setItem(result.index(i), j, QTableWidgetItem(str(i[j])))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
