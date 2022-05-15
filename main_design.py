from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMainWindow, QButtonGroup, QVBoxLayout, QLabel, QGroupBox, QGridLayout, QRadioButton, QListView, QListWidget, QComboBox
import sys
from main import *

class Main_UI(QMainWindow):
    def __init__(self):
        super(Main_UI, self).__init__()
        self.setFixedSize(830, 660)
        self.setWindowTitle("LIBRARY-GUI")
        #stackedwidget to stack different widget on each other
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 0, 820, 650)) 
        #first widget - welcome window /screen
        self.Welcome = QtWidgets.QWidget()
        # 2nd widget for application - main content shows library
        self.Display = QtWidgets.QWidget()


        self.selectedBook = []
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
        self.TakeOutBookButton.clicked.connect(self.takeOutBook)
        self.pushButton.clicked.connect(self.preview_content)
        self.SelectBooks.activated.connect(self.handleComboSelection)
    
    def handleComboSelection(self, id):
        if id == 0:
            print("you have selected library books")
        elif id == 1:
            print("you have selected user books")
            
            # self.icons = {}
            # GridLayout = QGridLayout()
            # counter = 0
            # row = 0
            # col = -1
            # layout = self.BookWidget.layout()
            # while(layout.count() != 0):
            #     widgetItem = layout.takeAt(0)
                
            #     layout.removeWidget(widgetItem.widget())
                
            
            
            # for bookName, info in hand.items():
            #     col += 1
            #     if col % 3 == 0 & col != 0:
            #         col = 0
            #         row += 1

                
                

            #     image = QLabel()
            #     image.setText("")
            #     image.setPixmap(QtGui.QPixmap("book.png"))
            #     image.setScaledContents(True)
            #     image.setFixedSize(70, 70)

            #     image.setObjectName(bookName)

        
            #     box = QGroupBox(bookName)
            #     boxLayout = QVBoxLayout()
            #     box.setLayout(boxLayout)
            
            
            

            #     boxLayout.addWidget(image)

            #     button = QRadioButton()
            #     button.setText("")
            #     self.UserButtonGroup.addButton(button, counter);
            #     counter+=1
            #     boxLayout.addWidget(button)

            #     self.icons[bookName] =  box
            #     layout.addChildWidget(box)
                
                # GridLayout.addWidget(self.icons[bookName], row, col)
            # GridLayout.setGeometry(QtCore.QRect(200, 20, 100, 100))
           
            
           
            

           
    
    def takeOutBook(self):
        if len(self.selectedBook) != 0:
            selectedBookName =  self.selectedBook[0]

            
            for _, books in library.items():
                for bookName, info in books.items():
                    if bookName == selectedBookName:
                        hand[bookName] = info
                        break;      
            
        
            
            #user has this book
            # print(f'User has this books in possession: {hand}')
            
            if selectedBookName in library[Library.shelf]:
                del library[Library.shelf][selectedBookName]
           
            layout = self.BookWidget.layout()
           
            widgetToRemove =  []
            for i in range(layout.count()):
                widgetItem = layout.itemAt(i)
                if widgetItem is not None:
                    qLabelName = widgetItem.widget().children()[1]
                    if qLabelName.objectName() == selectedBookName:
                        widgetToRemove.append(widgetItem.widget())

            if len(widgetToRemove) != 0:
                layout.removeWidget(widgetToRemove[0])
            self.BookGridLayout = self._createBookGrid()
            

        
            self.historyContent.addItem(f"-{self.input.text()} has taken out {selectedBookName}")
            self.historyContent.adjustSize()   

            # take_out()
        else:
            print("Please select a book")


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
        # self.historyContent = QtWidgets.QLabel()
        self.historyContent = QtWidgets.QListWidget(self.HistoryScrollAreaWidgetContents)
        # self.historyContent = QtWidgets.QLabel()
        self.historyContent.setGeometry(QtCore.QRect(10, 15, 20, 10))
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
        self.PreviewContents.setGeometry(QtCore.QRect(12, 12, 100, 100))
        self.PreviewWidget.setWidget(self.PreviewScrollAreaWidgetContents)
        self.PreviewLabel = QtWidgets.QLabel(self.PreviewScrollAreaWidgetContents)
        self.PreviewLabel.setGeometry(QtCore.QRect(220, 0, 47, 13))

        #book widget
        self.BookWidget = QtWidgets.QScrollArea(self.Display)
        self.BookWidget.setGeometry(QtCore.QRect(10, 20, 511, 381))
        self.BookWidget.setWidgetResizable(True)
        
        self.SelectBooks = QtWidgets.QComboBox(self.Display)
        self.SelectBooks.setGeometry(QtCore.QRect(370, 0, 111, 22))
        self.SelectBooks.setEditable(False)
        self.SelectBooks.addItem("")
        self.SelectBooks.addItem("")
        

        

        ########
        #adds all the books retrieved from the back end to book widget
        self.ButttonGroup  = QButtonGroup(self);
        self.UserButtonGroup  = QButtonGroup(self);

        self.ButttonGroup.buttonClicked[int].connect(self.show_content)
        
        self.UserButtonGroup.buttonClicked[int].connect(self.userShowContent)

        self.BookGridLayout = self._createBookGrid()
        self.BookWidget.setLayout(self.BookGridLayout)
        self.BookLabel = QtWidgets.QLabel(self.BookWidget)
        self.BookLabel.setGeometry(QtCore.QRect(220, 0, 47, 13))

        # add Display Widget on stacked widget
        self.stackedWidget.addWidget(self.Display)


   
    
    def _createBookGrid(self):
        self.icons = {}
        GridLayout = QGridLayout()
        counter = 0
    
        # data = self.getLibraryInfo()
        for row, books in library.items():
            row = int(row[-1]) - 1
            for col, info in enumerate(books.items()):
                bookName = info[0]

                image = QLabel()
                image.setText("")
                image.setPixmap(QtGui.QPixmap("book.png"))
                image.setScaledContents(True)
                image.setFixedSize(70, 70)

                image.setObjectName(bookName)

        
                box = QGroupBox(bookName)
                boxLayout = QVBoxLayout()
                box.setLayout(boxLayout)
            
              
            

                boxLayout.addWidget(image)

                button = QRadioButton()
                button.setCheckable(True)
                button.setText("")
                self.ButttonGroup.addButton(button, counter);
                counter+=1
                boxLayout.addWidget(button)

                self.icons[bookName] =  box
                
                GridLayout.addWidget(self.icons[bookName], row, col)
        GridLayout.setGeometry(QtCore.QRect(530, 20, 271, 171))
        

        return GridLayout

        
    def show_content(self, id):
        
        selected = self.ButttonGroup.button(id).parentWidget().children()[1].objectName()
        if len(self.selectedBook) == 0:
            self.selectedBook.append(selected)
        else:
            self.selectedBook[0] = selected
        # counter = 0
        

    def userShowContent(self, id):
        counter = 0
        for bookName, info in hand.items():
            if counter == id:
                if len(self.selectedBook) == 0:
                    self.selectedBook.append(info)
                else:
                    self.selectedBook[0] = info
            counter+=1

    def showDisplay(self):
        #change the current widget in stacked widget to display widget window
        self.stackedWidget.setCurrentWidget(self.Display)
        #set text on promptlabel inside the User to bear name of what user entered in library screen
        self.promptlabel.setText(f"Name:  {self.input.text()}")

    def settingtext(self):
        self.label1.setText("Welcome to World\'s Best Library")
        self.label1.adjustSize()
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
        self.promptlabel.setText("Name: ")
     
    #books widget text
        self.SelectBooks.setCurrentText("Library Books")
        self.SelectBooks.setItemText(0, "Library Books")
        self.SelectBooks.setItemText(1, "User Books")
        #self.Book1_label.setText("Book 1")
        self.BookLabel.setText("Books")
        self.PreviewLabel.setText("Preview")

    def preview_content(self):
        if len(self.selectedBook) != 0:
            book = self.selectedBook[0]
            self.PreviewContents.setText(book[1][0])
            self.PreviewContents.adjustSize()
        






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