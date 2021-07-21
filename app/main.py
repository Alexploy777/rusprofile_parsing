# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
# Form, Window = uic.loadUiType("gui_ofd.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()
'''
search_inn
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from gui_ofd import Ui_MainWindow

class Ofd(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ofd, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Источник данных - Rusprofile')
        self.setWindowIcon(QIcon('rusprofile.png'))
        self.ui.inn.setPlaceholderText('введите поисковые данные')
        self.ui.search_inn.clicked.connect(self.search_inn)

    def search_inn(self):
        print('search_inn')


def main(): # точка входа
    app = QtWidgets.QApplication([])
    application = Ofd()
    application.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()