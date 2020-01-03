from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget
from PyQt5 import uic
import sys, sqlite3


class Maim(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"])
        self.data = sqlite3.connect('coffee.sqlite')
        cur = self.data.cursor()
        lst = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(lst))
        for i in range(len(lst)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(lst[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(lst[i][1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(lst[i][2]))
            if lst[i][3] is not None:
                self.tableWidget.setItem(i, 3, QTableWidgetItem(cur.execute(f"""SELECT title FROM type WHERE id = {lst[i][3]}""").fetchone()[0]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(lst[i][4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(lst[i][5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(lst[i][6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Maim()
    form.show()
    sys.exit(app.exec_())
