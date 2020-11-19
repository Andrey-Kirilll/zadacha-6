import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from release.new_form import AddForm
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_inform = QtWidgets.QPushButton(self.centralwidget)
        self.get_inform.setGeometry(QtCore.QRect(70, 40, 301, 71))
        self.get_inform.setStyleSheet("background-color: rgb(116, 116, 116);\n"
                                      "font: 75 16pt \"Segoe Script\";\n"
                                      "text-decoration: underline;")
        self.get_inform.setObjectName("get_inform")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setGeometry(QtCore.QRect(25, 160, 721, 321))
        self.coffee_table.setStyleSheet("font: 10pt \"Microsoft New Tai Lue\";")
        self.coffee_table.setLineWidth(1)
        self.coffee_table.setShowGrid(True)
        self.coffee_table.setGridStyle(QtCore.Qt.SolidLine)
        self.coffee_table.setRowCount(9)
        self.coffee_table.setColumnCount(7)
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.horizontalHeader().setMinimumSectionSize(39)
        self.change_db = QtWidgets.QPushButton(self.centralwidget)
        self.change_db.setGeometry(QtCore.QRect(440, 40, 271, 71))
        self.change_db.setStyleSheet("background-color: rgb(116, 116, 116);\n"
                                     "font: 75 16pt \"Segoe Script\";\n"
                                     "text-decoration: underline;")
        self.change_db.setObjectName("change_db")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))
        self.get_inform.setText(_translate("MainWindow", "Получить информацию\n"
                                                         " о кофе"))
        self.change_db.setText(_translate("MainWindow", "Внести изменения\n"
                                                        "в базу данных"))


class Coffee(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ex1 = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.get_inform.clicked.connect(self.view_information)
        self.change_db.clicked.connect(self.open_new_form)

    def view_information(self):
        con = sqlite3.connect('data/coffee.sqlite.db')
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
