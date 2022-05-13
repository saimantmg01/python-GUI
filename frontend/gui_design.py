# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 0, 741, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.label1 = QtWidgets.QLabel(self.Welcome)
        self.label1.setGeometry(QtCore.QRect(150, 80, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.Welcome)
        self.label2.setGeometry(QtCore.QRect(247, 170, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.input = QtWidgets.QLineEdit(self.Welcome)
        self.input.setGeometry(QtCore.QRect(272, 220, 191, 21))
        self.input.setObjectName("input")
        self.SubmitButton = QtWidgets.QPushButton(self.Welcome)
        self.SubmitButton.setGeometry(QtCore.QRect(310, 270, 100, 32))
        self.SubmitButton.setObjectName("SubmitButton")
        self.stackedWidget.addWidget(self.Welcome)
        self.Display = QtWidgets.QWidget()
        self.Display.setObjectName("Display")
        self.tabWidget = QtWidgets.QTabWidget(self.Display)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 751, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.TabHistory = QtWidgets.QWidget()
        self.TabHistory.setObjectName("TabHistory")
        self.promptlabel = QtWidgets.QLabel(self.TabHistory)
        self.promptlabel.setGeometry(QtCore.QRect(257, 40, 221, 20))
        self.promptlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptlabel.setObjectName("promptlabel")
        self.basicLabel = QtWidgets.QLabel(self.TabHistory)
        self.basicLabel.setGeometry(QtCore.QRect(340, 80, 58, 16))
        self.basicLabel.setObjectName("basicLabel")
        self.Content = QtWidgets.QTextEdit(self.TabHistory)
        self.Content.setGeometry(QtCore.QRect(50, 140, 641, 321))
        self.Content.setObjectName("Content")
        self.tabWidget.addTab(self.TabHistory, "")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.Basiclabel2 = QtWidgets.QLabel(self.Home)
        self.Basiclabel2.setGeometry(QtCore.QRect(260, 20, 211, 20))
        self.Basiclabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.Basiclabel2.setObjectName("Basiclabel2")
        self.historyContent = QtWidgets.QTextEdit(self.Home)
        self.historyContent.setGeometry(QtCore.QRect(20, 90, 701, 371))
        self.historyContent.setObjectName("historyContent")
        self.tabWidget.addTab(self.Home, "")
        self.stackedWidget.addWidget(self.Display)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Welcome to World\'s Best Library"))
        self.label2.setText(_translate("MainWindow", "What is your name?"))
        self.input.setPlaceholderText(_translate("MainWindow", "Type your name..."))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.promptlabel.setText(_translate("MainWindow", "Hello,"))
        self.basicLabel.setText(_translate("MainWindow", "Book List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabHistory), _translate("MainWindow", "Tab 1"))
        self.Basiclabel2.setText(_translate("MainWindow", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

