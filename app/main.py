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

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from gui_ofd import Ui_MainWindow

from parsing_func import *

# from progress_print import

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
        input_search_str = self.ui.inn.text()
        print(input_search_str, type(input_search_str))
        client = Parser(input_search_str)  # создали объект класса Parser
        ofd_data = client.get_ofd_data() # Вызвали метод get_ofd_data, получили данные для офд
        # fio = ofd_data['фио']
        # print(fio)
        self.ui.label_top_info.setText(str(f"{ofd_data['info']} code: {ofd_data['status_code']} "))
        self.ui.fio_dir.setText(str(ofd_data['фио']))
        self.ui.fns.setText(str(ofd_data['фнс']))
        self.ui.pfr.setText(str(ofd_data['пфр']))
        self.ui.rosstat.setText(str(ofd_data['росстат']))
        self.ui.fss.setText(str(ofd_data['фсс']))

        # print(ofd_data)



def main(): # точка входа
    app = QtWidgets.QApplication([])
    application = Ofd()
    application.show()


    sys.exit(app.exec())




if __name__ == '__main__':
    main()