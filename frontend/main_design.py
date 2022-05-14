from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMainWindow
import sys

class Main_UI(QMainWindow):
    def __init__(self):
        super(Main_UI, self).__init__()
        self.resize(830, 660)
        self.setWindowTitle("LIBRARY-GUI")
        #stackedwidget to stack different widget on each other
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 0, 820, 650)) 
        #first widget - welcome window /screen
        self.Welcome = QtWidgets.QWidget()
        # 2nd widget for application - main content shows library
        self.Display = QtWidgets.QWidget()
        #run the entire code for application
        self.initUI()


    def initUI(self):
        #setup welcome window
        self.Welcome_Window()
        #setup display window
        self.Display_Window()
        #put appropriate text for each Qlabel, comboboxes, placeholder for Qlineedit
        self.settingtext()
        
        #set current default widget on stacked widget to be welcome page
        self.stackedWidget.setCurrentWidget(self.Welcome)

        #call the event/functions
        #when name is submitted go to main content which shows library contents, history and others
        self.SubmitButton.clicked.connect(self.showDisplay)


    def Welcome_Window(self):
        #Qlabel to greet user on Welcome Widget
        self.label1 = QtWidgets.QLabel(self.Welcome)
        self.label1.setGeometry(QtCore.QRect(150, 80, 421, 51))
        #set the font for label1
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
       
        #Qlabel to ask for name in Welcome widget
        self.label2 = QtWidgets.QLabel(self.Welcome)
        self.label2.setGeometry(QtCore.QRect(247, 170, 221, 20))
        #set the font for label1
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        
        #QLineEdit- text edit where user can type  the name in Welcome widget
        self.input = QtWidgets.QLineEdit(self.Welcome)
        self.input.setGeometry(QtCore.QRect(272, 220, 191, 21))
         
        #QPushButton - to submit name and revert to another window in Welcome widget
        self.SubmitButton = QtWidgets.QPushButton(self.Welcome)
        self.SubmitButton.setGeometry(QtCore.QRect(310, 270, 100, 32))
        
        # add Library Widget on stacked widget
        self.stackedWidget.addWidget(self.Welcome)

    def Display_Window(self):
        #history widget
        self.HistoryWidget = QtWidgets.QScrollArea(self.Display)
        self.HistoryWidget.setGeometry(QtCore.QRect(530, 20, 271, 171))
        self.HistoryWidget.setWidgetResizable(True)
        self.HistoryScrollAreaWidgetContents = QtWidgets.QWidget()
        self.HistoryScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 169))
        self.HistoryLabel = QtWidgets.QLabel(self.HistoryScrollAreaWidgetContents)
        self.HistoryLabel.setGeometry(QtCore.QRect(120, 0, 47, 13))
        self.HistoryWidget.setWidget(self.HistoryScrollAreaWidgetContents)

        #action widget
        self.ActionWidget = QtWidgets.QGroupBox(self.Display)
        self.ActionWidget.setGeometry(QtCore.QRect(530, 190, 271, 211))
        self.ActionWidget.setAlignment(QtCore.Qt.AlignCenter)
        #buttons assocated with action widget
        self.TakeOutBookButton = QtWidgets.QPushButton(self.ActionWidget)
        self.TakeOutBookButton.setGeometry(QtCore.QRect(90, 40, 91, 23))
        self.ReturnBookButton = QtWidgets.QPushButton(self.ActionWidget)
        self.ReturnBookButton.setGeometry(QtCore.QRect(90, 80, 91, 23))
        self.pushButton = QtWidgets.QPushButton(self.ActionWidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 91, 21))

         #user widget
        self.UserWidget = QtWidgets.QGroupBox(self.Display)
        self.UserWidget.setGeometry(QtCore.QRect(530, 400, 271, 211))
        self.UserWidget.setAlignment(QtCore.Qt.AlignCenter)
        #label for user widget
        self.promptlabel = QtWidgets.QLabel(self.UserWidget)
        self.promptlabel.setGeometry(QtCore.QRect(100, 40, 91, 23))
        self.promptlabel.setAlignment(QtCore.Qt.AlignCenter)

        #preview widget
        self.PreviewWidget = QtWidgets.QScrollArea(self.Display)
        self.PreviewWidget.setGeometry(QtCore.QRect(10, 420, 511, 191))
        self.PreviewWidget.setWidgetResizable(True)
        self.PreviewScrollAreaWidgetContents = QtWidgets.QWidget()
        self.PreviewScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 189))
        self.PreviewContents = QtWidgets.QLabel(self.PreviewScrollAreaWidgetContents)
        self.PreviewContents.setGeometry(QtCore.QRect(150, 70, 311, 101))
        self.PreviewWidget.setWidget(self.PreviewScrollAreaWidgetContents)
        self.PreviewLabel = QtWidgets.QLabel(self.PreviewScrollAreaWidgetContents)
        self.PreviewLabel.setGeometry(QtCore.QRect(220, 0, 47, 13))

        #book widget
        self.BookWidget = QtWidgets.QScrollArea(self.Display)
        self.BookWidget.setGeometry(QtCore.QRect(10, 20, 511, 381))
        self.BookWidget.setWidgetResizable(True)
        self.BookScrollAreaWidgetContents = QtWidgets.QWidget()
        self.BookScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 379))
        self.SelectBooks = QtWidgets.QComboBox(self.BookScrollAreaWidgetContents)
        self.SelectBooks.setGeometry(QtCore.QRect(370, 0, 111, 22))
        self.SelectBooks.setEditable(True)
        self.SelectBooks.addItem("")
        self.SelectBooks.addItem("")
        self.BookImage = QtWidgets.QLabel(self.BookScrollAreaWidgetContents)
        self.BookImage.setGeometry(QtCore.QRect(40, 30, 91, 71))
        self.BookImage.setText("")
        self.BookImage.setPixmap(QtGui.QPixmap("book.png"))
        self.BookImage.setScaledContents(True)
        self.Book1_label = QtWidgets.QLabel(self.BookScrollAreaWidgetContents)
        self.Book1_label.setGeometry(QtCore.QRect(70, 90, 51, 31))
        self.BookLabel = QtWidgets.QLabel(self.BookScrollAreaWidgetContents)
        self.BookLabel.setGeometry(QtCore.QRect(220, 0, 47, 13))
        self.BookWidget.setWidget(self.BookScrollAreaWidgetContents)

        # add Display Widget on stacked widget
        self.stackedWidget.addWidget(self.Display)



    def showDisplay(self):
        #change the current widget in stacked widget to display widget window
        self.stackedWidget.setCurrentWidget(self.Display)
        #set text on promptlabel inside the User to bear name of what user entered in library screen
        self.promptlabel.setText(f"Name:  {self.input.text()}")

    def settingtext(self):
        self.label1.setText("Welcome to World\'s Best Library")
        self.label2.setText("What is your name?")
        self.input.setPlaceholderText("Type your name...")
        self.SubmitButton.setText("Submit")

        self.HistoryLabel.setText("History")
        self.ActionWidget.setTitle("Actions")
        self.TakeOutBookButton.setText("Take out book")
        self.TakeOutBookButton.adjustSize()
        self.ReturnBookButton.setText("Return book")
        self.ReturnBookButton.adjustSize()
        self.pushButton.setText("Preview")
        self.pushButton.adjustSize()
        self.UserWidget.setTitle("User")
        self.PreviewContents.setText("contents")
        self.SelectBooks.setCurrentText("Library Books")
        self.SelectBooks.setItemText(0, "Library Books")
        self.SelectBooks.setItemText(1, "User Books")
        self.Book1_label.setText("Book 1")
        self.BookLabel.setText("Books")
        self.PreviewLabel.setText("Preview")

        self.promptlabel.setText("Name: ")


def window():
    #setup the app to run
    app = QApplication(sys.argv)
    #call the Main_UI class
    win = Main_UI()
    # show the window
    win.show()
    # do a clean exit. Close the application
    sys.exit(app.exec_())

window()