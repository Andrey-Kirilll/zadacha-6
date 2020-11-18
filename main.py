from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from new_form import AddForm


class Coffee(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ex1 = None
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.get_inform.clicked.connect(self.view_information)
        self.change_db.clicked.connect(self.open_new_form)

    def view_information(self):
        con = sqlite3.connect('coffee.sqlite.db')
        cur = con.cursor()
        result = cur.execute('''SELECT * from cofes''').fetchall()
        self.coffee_table.setRowCount(len(result))
        for i in result:
            for j in range(len(i)):
                self.coffee_table.setItem(result.index(i), j, QTableWidgetItem(str(i[j])))

    def open_new_form(self):
        self.ex1 = AddForm()
        self.ex1.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
