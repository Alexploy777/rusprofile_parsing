# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_ofd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_frame = QtWidgets.QFrame(self.centralwidget)
        self.input_frame.setGeometry(QtCore.QRect(10, 50, 681, 115))
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.frame = QtWidgets.QFrame(self.input_frame)
        self.frame.setGeometry(QtCore.QRect(10, 10, 421, 95))
        self.frame.setMinimumSize(QtCore.QSize(421, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 97, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inn = QtWidgets.QLineEdit(self.frame)
        self.inn.setGeometry(QtCore.QRect(30, 40, 361, 40))
        self.inn.setMinimumSize(QtCore.QSize(167, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inn.setFont(font)
        self.inn.setCursorPosition(0)
        self.inn.setAlignment(QtCore.Qt.AlignCenter)
        self.inn.setDragEnabled(False)
        self.inn.setObjectName("inn")
        self.search_inn = QtWidgets.QPushButton(self.input_frame)
        self.search_inn.setGeometry(QtCore.QRect(440, 50, 181, 40))
        self.search_inn.setMinimumSize(QtCore.QSize(181, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_inn.setFont(font)
        self.search_inn.setObjectName("search_inn")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 170, 661, 561))
        self.tabWidget_2.setMinimumSize(QtCore.QSize(651, 491))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setToolTip("")
        self.label_2.setObjectName("label_2")
        self.fio_dir = QtWidgets.QLineEdit(self.tab)
        self.fio_dir.setGeometry(QtCore.QRect(20, 120, 361, 40))
        self.fio_dir.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fio_dir.setFont(font)
        self.fio_dir.setStyleSheet("padding = 20px")
        self.fio_dir.setObjectName("fio_dir")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(400, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.email_dir = QtWidgets.QLineEdit(self.tab)
        self.email_dir.setGeometry(QtCore.QRect(400, 120, 241, 40))
        self.email_dir.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email_dir.setFont(font)
        self.email_dir.setObjectName("email_dir")
        self.phonegen_btn = QtWidgets.QPushButton(self.tab)
        self.phonegen_btn.setGeometry(QtCore.QRect(470, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phonegen_btn.setFont(font)
        self.phonegen_btn.setObjectName("phonegen_btn")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.phone = QtWidgets.QLineEdit(self.tab)
        self.phone.setGeometry(QtCore.QRect(20, 200, 281, 40))
        self.phone.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.phone.setFont(font)
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.togs = QtWidgets.QLineEdit(self.tab)
        self.togs.setGeometry(QtCore.QRect(210, 470, 281, 40))
        self.togs.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.togs.setFont(font)
        self.togs.setText("")
        self.togs.setObjectName("togs")
        self.pfr = QtWidgets.QLineEdit(self.tab)
        self.pfr.setGeometry(QtCore.QRect(210, 320, 281, 40))
        self.pfr.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pfr.setFont(font)
        self.pfr.setText("")
        self.pfr.setObjectName("pfr")
        self.fss = QtWidgets.QLineEdit(self.tab)
        self.fss.setGeometry(QtCore.QRect(210, 420, 281, 40))
        self.fss.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fss.setFont(font)
        self.fss.setText("")
        self.fss.setObjectName("fss")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 480, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.rosstat = QtWidgets.QLineEdit(self.tab)
        self.rosstat.setGeometry(QtCore.QRect(210, 370, 281, 40))
        self.rosstat.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rosstat.setFont(font)
        self.rosstat.setText("")
        self.rosstat.setObjectName("rosstat")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 380, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 430, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.fns = QtWidgets.QLineEdit(self.tab)
        self.fns.setGeometry(QtCore.QRect(210, 270, 281, 40))
        self.fns.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fns.setFont(font)
        self.fns.setText("")
        self.fns.setObjectName("fns")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setKerning(False)
        self.label_10.setFont(font)
        self.label_10.setToolTip("")
        self.label_10.setObjectName("label_10")
        self.company_name = QtWidgets.QLineEdit(self.tab)
        self.company_name.setGeometry(QtCore.QRect(20, 40, 621, 40))
        self.company_name.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.company_name.setFont(font)
        self.company_name.setText("")
        self.company_name.setAlignment(QtCore.Qt.AlignCenter)
        self.company_name.setObjectName("company_name")
        self.checkBox_cod = QtWidgets.QCheckBox(self.tab)
        self.checkBox_cod.setGeometry(QtCore.QRect(350, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_cod.setFont(font)
        self.checkBox_cod.setChecked(False)
        self.checkBox_cod.setObjectName("checkBox_cod")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.label_top_info = QtWidgets.QLabel(self.centralwidget)
        self.label_top_info.setGeometry(QtCore.QRect(20, 0, 671, 50))
        self.label_top_info.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_top_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_top_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top_info.setObjectName("label_top_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите ИНН"))
        self.inn.setPlaceholderText(_translate("MainWindow", "введите строку"))
        self.search_inn.setText(_translate("MainWindow", "ИСКАТЬ"))
        self.label_2.setText(_translate("MainWindow", "ФИО руководителя"))
        self.label_3.setText(_translate("MainWindow", "EMAIL пользователя"))
        self.phonegen_btn.setText(_translate("MainWindow", "генерировать"))
        self.label_4.setText(_translate("MainWindow", "Телефон пользователя"))
        self.label_9.setText(_translate("MainWindow", "РОССТАТ код ТОГС"))
        self.label_7.setText(_translate("MainWindow", "РОССТАТ"))
        self.label_8.setText(_translate("MainWindow", "ФСС"))
        self.label_6.setText(_translate("MainWindow", "ПФР"))
        self.label_5.setText(_translate("MainWindow", "ФНС"))
        self.label_10.setText(_translate("MainWindow", "Название компании"))
        self.checkBox_cod.setText(_translate("MainWindow", "КОД +7"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "ОФД"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_top_info.setText(_translate("MainWindow", "Здесь будет разная инфа"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
