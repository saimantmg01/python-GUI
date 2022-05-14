from email.charset import QP
import sys


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox, QRadioButton, QButtonGroup
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Create a subclass of QMainWindow to setup the calculator's GUI
class LibUi(QMainWindow):
    
    def __init__(self):
        """View initializer."""
        super().__init__()
        
        self.setWindowTitle('Library App')
        self.setFixedSize(900, 600)
        # Set the central widget
        self.generalLayout = QGridLayout()
        
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.BookWidget = QtWidgets.QScrollArea(self)
        self.BookWidget.setGeometry(QtCore.QRect(10, 20, 600,400))
        
        #adds all the books retrieved from the back end to book widget
        self.data = self.getLibraryInfo()
        self.ButttonGroup  = QButtonGroup(self);

        self.ButttonGroup.buttonClicked[int].connect(self.show_content)

        self.BookGridLayout = self._createBookGrid()
        self.BookWidget.setLayout(self.BookGridLayout)
        
        
        
       

    def getLibraryInfo(self):
        # data = {'shelf1': {'Curious George':['monkey', 'Christopher'], 
        #                   'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
        #                   'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
        #                   'Bone': ['human bones', 'Michelle']
        #                   }
        #                   ,'shelf2': {'Curious George':['monkey', 'Christopher'], 
        #                   'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
        #                   'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
        #                   'Bone': ['human bones', 'Michelle']
        #                   }
        #                 #   ,'shelf3': {'Curious George':['monkey', 'Christopher'], 
        #                 #   'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
        #                 #   'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
        #                 #   'Bone': ['human bones', 'Michelle']
        #                 #   } }

        data = {'Shelf1': {'Catcher in the Rye': ['Fiction', 'J.D. Salinger'],
            'Don Quixote': ['Fiction', 'Miguel de Cervantes'],
            'One Hundred Years of Solitude': ['Fiction',
                                              'Gabriel Garcia Marquez']},
                'Shelf2': {'Hamlet': ['Fiction', 'William Shakespeare'],
                            'Moby Dick': ['Fiction', 'Herman Melville'],
                            'Odyssey': ['Fiction', 'Homer'],
                            'The Great Gatsby': ['Fiction', 'F.Scott Fitzgerald'],
                            'War and Peace ': ['Fiction', 'Leo Tolstoy']},
                'Shelf3': {'The Complete Works of Plato': ['Non Fiction', 'Plato'],
                            'The Diary of a Young Girl': ['Non fiction', 'Anne Frank'],
                            'Walden': ['Non fiction', 'Henry David Thoreau']}}
                          
        return data

   
    
    def _createBookGrid(self):
        self.icons = {}
        GridLayout = QGridLayout()
        counter = 0
    
        # data = self.getLibraryInfo()
        for row, books in self.data.items():
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

####################################################
                button = QRadioButton()
                button.setText("")
                self.ButttonGroup.addButton(button, counter);
                counter+=1
                boxLayout.addWidget(button)




                self.icons[bookName] =  box

                
                
                
              
                
                GridLayout.addWidget(self.icons[bookName], row, col)
        GridLayout.setGeometry(QtCore.QRect(530, 20, 271, 171))
        

        return GridLayout

        
    def show_content(self, id):
        counter = 0
        for _, books in self.data.items():
            for _, info in enumerate(books.items()):
                if counter == id:
                    print(info)
                counter+=1

        



def main():
    
    pycalc = QApplication(sys.argv)
    
    view = LibUi()
    view.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()