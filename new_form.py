from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow


class AddForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.flag = None
        uic.loadUi('addEditCoffeeForm.ui', self)
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
        con = sqlite3.connect('coffee.sqlite.db')
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
        con = sqlite3.connect('coffee.sqlite.db')
        cur = con.cursor()
        if self.flag == 1:
            cur.execute('''UPDATE cofes SET sort_name = '{}', roasting_degree = '{}', condition = '{}',
              taste = '{}', cost = {}, volume = {} WHERE id = {}'''.format(self.sort_edit.text(),
                self.roasting_degree_edit.text(), self.condition_edit.text(), self.taste_edit.text(),
                int(self.cost_edit.text()), int(self.volume_edit.text()), self.id))
            self.signal_label.setText('Изменения внесены')
        else:
            res = cur.execute('''SELECT id FROM cofes''').fetchall()
            res.sort(key=lambda x: x[0], reverse=True)
            cur.execute('''INSERT INTO cofes(id, sort_name, roasting_degree, condition, taste, cost, volume) VALUES(
            {}, '{}', '{}', '{}', '{}', {}, {})'''.format(int(res[0][0] + 1), self.sort_edit.text(),
                self.roasting_degree_edit.text(), self.condition_edit.text(), self.taste_edit.text(),
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
