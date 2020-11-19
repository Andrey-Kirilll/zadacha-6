import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.new_inf = QtWidgets.QPushButton(self.centralwidget)
        self.new_inf.setGeometry(QtCore.QRect(90, 30, 141, 61))
        self.new_inf.setStyleSheet("font: 12pt \"Myanmar Text\";\n"
                                   "color: rgb(0, 218, 0);")
        self.new_inf.setObjectName("new_inf")
        self.change_inf = QtWidgets.QPushButton(self.centralwidget)
        self.change_inf.setGeometry(QtCore.QRect(310, 30, 141, 61))
        self.change_inf.setStyleSheet("font: 14pt \"MV Boli\";\n"
                                      "color: rgb(0, 85, 255);")
        self.change_inf.setObjectName("change_inf")
        self.delete_inf = QtWidgets.QPushButton(self.centralwidget)
        self.delete_inf.setGeometry(QtCore.QRect(480, 30, 141, 61))
        self.delete_inf.setStyleSheet("color: rgb(170, 0, 0);\n"
                                      "font: 14pt \"MV Boli\";")
        self.delete_inf.setObjectName("delete_inf")
        self.cost_label = QtWidgets.QLabel(self.centralwidget)
        self.cost_label.setGeometry(QtCore.QRect(60, 360, 101, 31))
        self.cost_label.setObjectName("cost_label")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(90, 400, 61, 31))
        self.volume_label.setObjectName("volume_label")
        self.taste_label = QtWidgets.QLabel(self.centralwidget)
        self.taste_label.setGeometry(QtCore.QRect(70, 290, 91, 61))
        self.taste_label.setObjectName("taste_label")
        self.roasting_degree_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.roasting_degree_edit.setGeometry(QtCore.QRect(180, 170, 181, 41))
        self.roasting_degree_edit.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                                "color: rgb(85, 255, 255);")
        self.roasting_degree_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.roasting_degree_edit.setObjectName("roasting_degree_edit")
        self.roasting_degree_label = QtWidgets.QLabel(self.centralwidget)
        self.roasting_degree_label.setGeometry(QtCore.QRect(80, 160, 81, 50))
        self.roasting_degree_label.setObjectName("roasting_degree_label")
        self.sort_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(60, 110, 101, 31))
        self.sort_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sort_label.setTextFormat(QtCore.Qt.MarkdownText)
        self.sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_label.setObjectName("sort_label")
        self.condition_label = QtWidgets.QLabel(self.centralwidget)
        self.condition_label.setGeometry(QtCore.QRect(70, 230, 89, 50))
        self.condition_label.setObjectName("condition_label")
        self.condition_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.condition_edit.setGeometry(QtCore.QRect(180, 230, 181, 41))
        self.condition_edit.setStyleSheet("color: rgb(229, 153, 229);\n"
                                          "font: italic 12pt \"Georgia\";")
        self.condition_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.condition_edit.setObjectName("condition_edit")
        self.sort_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sort_edit.setGeometry(QtCore.QRect(180, 110, 181, 41))
        self.sort_edit.setStyleSheet("font: 14pt \"Segoe UI Historic\";\n"
                                     "color: rgb(0, 255, 0);")
        self.sort_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_edit.setObjectName("sort_edit")
        self.taste_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.taste_edit.setGeometry(QtCore.QRect(180, 290, 181, 51))
        self.taste_edit.setStyleSheet("color: rgb(229, 153, 229);\n"
                                      "font: italic 12pt \"Georgia\";")
        self.taste_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.taste_edit.setObjectName("taste_edit")
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(410, 110, 121, 31))
        self.id_edit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.id_edit.setObjectName("id_edit")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(410, 210, 181, 71))
        self.yes_button.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(85, 170, 255);\n"
                                      "color: rgb(85, 255, 0);")
        self.yes_button.setObjectName("yes_button")
        self.cost_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cost_edit.setGeometry(QtCore.QRect(180, 370, 91, 20))
        self.cost_edit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.cost_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_edit.setObjectName("cost_edit")
        self.volume_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_edit.setGeometry(QtCore.QRect(182, 400, 91, 20))
        self.volume_edit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.volume_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_edit.setObjectName("volume_edit")
        self.signal_label = QtWidgets.QLabel(self.centralwidget)
        self.signal_label.setGeometry(QtCore.QRect(410, 160, 191, 31))
        self.signal_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "text-decoration: underline;")
        self.signal_label.setText("")
        self.signal_label.setObjectName("signal_label")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(550, 110, 75, 31))
        self.ok_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(85, 255, 255);")
        self.ok_button.setObjectName("ok_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление нового сорта кофе"))
        self.new_inf.setText(_translate("MainWindow", "Добавить новую\n"
                                                      "запись"))
        self.change_inf.setText(_translate("MainWindow", "Изменить\n"
                                                         "запись"))
        self.delete_inf.setText(_translate("MainWindow", "Удалить\n"
                                                         "запись"))
        self.cost_label.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; "
                                           "font-style:italic; text-decoration: "
                                           "underline;\">Стоимость</span></p></body></html>"))
        self.volume_label.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; "
                                             "font-style:italic; text-decoration: "
                                             "underline;\">Объём</span></p><p><span style=\" font-size:12pt; "
                                             "font-weight:600; font-style:italic; text-decoration: "
                                             "underline;\">упаковки</span></p></body></html>"))
        self.taste_label.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; "
                                            "font-style:italic; text-decoration: "
                                            "underline;\">Описание</span></p><p><span style=\" font-size:12pt; "
                                            "font-weight:600; font-style:italic; text-decoration: "
                                            "underline;\">вкуса</span></p></body></html>"))
        self.roasting_degree_label.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:12pt; "
                                                      "font-weight:600; font-style:italic; text-decoration: "
                                                      "underline;\">Степень</span></p><p><span style=\" "
                                                      "font-size:12pt; font-weight:600; font-style:italic; "
                                                      "text-decoration: "
                                                      "underline;\">обжарки</span></p></body></html>"))
        self.sort_label.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; "
                                           "font-style:italic; text-decoration: underline;\">Сорт "
                                           "кофе</span></p></body></html>"))
        self.condition_label.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:12pt; "
                                                "font-weight:600; font-style:italic; text-decoration: "
                                                "underline;\">Молотый/</span></p><p><span style=\" font-size:12pt; "
                                                "font-weight:600; font-style:italic; text-decoration: underline;\">в "
                                                "зернах</span></p></body></html>"))
        self.id_edit.setPlaceholderText(_translate("MainWindow", "Введите id сорта"))
        self.yes_button.setText(_translate("MainWindow", "Подтвердить"))
        self.ok_button.setText(_translate("MainWindow", "Ok"))


class AddForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.flag = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.hide_all()
        self.new_inf.clicked.connect(self.new_inf_method)
        self.change_inf.clicked.connect(self.change_method)
        self.delete_inf.clicked.connect(self.delete_method)
        self.ok_button.clicked.connect(self.ok_method)
        self.yes_button.clicked.connect(self.result_method)

    def hide_all(self):
        self.sort_label.hide(), self.roasting_degree_label.hide(), self.condition_label.hide(),
        self.taste_label.hide(), self.cost_label.hide(), self.volume_label.hide(),
        self.sort_edit.hide(), self.roasting_degree_edit.hide(), self.condition_edit.hide(),
        self.taste_edit.hide(), self.cost_edit.hide(), self.volume_edit.hide(), self.id_edit.hide(),
        self.yes_button.hide(), self.ok_button.hide()
        self.id_edit.setText(''), self.signal_label.setText(''), self.sort_edit.setText(''),
        self.roasting_degree_edit.setText(''), self.condition_edit.setText(''), self.taste_edit.setText(''),
        self.cost_edit.setText(''), self.volume_edit.setText('')

    def show_all(self):
        self.sort_label.show(), self.roasting_degree_label.show(), self.condition_label.show(),
        self.taste_label.show(), self.cost_label.show(), self.volume_label.show(),
        self.sort_edit.show(), self.roasting_degree_edit.show(), self.condition_edit.show(),
        self.taste_edit.show(), self.cost_edit.show(), self.volume_edit.show(), self.yes_button.show()

    def change_method(self):
        self.flag = 1
        self.hide_all()
        self.id_edit.show()
        self.ok_button.show()

    def delete_method(self):
        self.flag = 0
        self.hide_all()
        self.id_edit.show()
        self.ok_button.show()

    def new_inf_method(self):
        self.flag = 2
        self.hide_all()
        self.show_all()

    def ok_method(self):
        con = sqlite3.connect('data/coffee.sqlite.db')
        cur = con.cursor()
        res = [int(i[0]) for i in (cur.execute('''SELECT id FROM cofes''').fetchall())]
        if int(self.id_edit.text()) in res:
            self.id = int(self.id_edit.text())
            if self.flag == 0:
                self.signal_label.setText('Успешно удалён')
                cur.execute('''DELETE FROM cofes WHERE id = {}'''.format(self.id))
            elif self.flag == 1:
                res = cur.execute('''SELECT * FROM cofes WHERE id = {}'''.format(self.id)).fetchall()
                self.hide_all()
                self.show_all()
                self.sort_edit.setText(res[0][1])
                self.roasting_degree_edit.setText(res[0][2])
                self.condition_edit.setText(res[0][3])
                self.taste_edit.setText(res[0][4])
                self.cost_edit.setText(str(res[0][5]))
                self.volume_edit.setText(str(res[0][6]))
        else:
            self.signal_label.setText('Такого кофе нет')
        con.commit()
        con.close()

    def result_method(self):
        con = sqlite3.connect('data/coffee.sqlite.db')
        cur = con.cursor()
        if self.flag == 1:
            cur.execute('''UPDATE cofes SET sort_name = '{}', roasting_degree = '{}', condition = '{}',
              taste = '{}', cost = {}, volume = {} WHERE id = {}'''.format(self.sort_edit.text(),
                                                                           self.roasting_degree_edit.text(),
                                                                           self.condition_edit.text(),
                                                                           self.taste_edit.text(),
                                                                           int(self.cost_edit.text()),
                                                                           int(self.volume_edit.text()), self.id))
            self.signal_label.setText('Изменения внесены')
        else:
            res = cur.execute('''SELECT id FROM cofes''').fetchall()
            res.sort(key=lambda x: x[0], reverse=True)
            cur.execute('''INSERT INTO cofes(id, sort_name, roasting_degree, condition, taste, cost, volume) VALUES(
            {}, '{}', '{}', '{}', '{}', {}, {})'''.format(int(res[0][0] + 1), self.sort_edit.text(),
                                                          self.roasting_degree_edit.text(), self.condition_edit.text(),
                                                          self.taste_edit.text(),
                                                          int(self.cost_edit.text()), int(self.volume_edit.text())))
            self.signal_label.setText('Кофе добавлен')
        con.commit()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddForm()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
