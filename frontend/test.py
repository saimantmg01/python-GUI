import sys


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
from PyQt5 import QtCore
from PyQt5 import QtGui





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
        self._createGrid()
        
        
       

    def getLibraryInfo(self):
        data = {'shelf1': {'Curious George':['monkey', 'Christopher'], 
                          'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
                          'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
                          'Bone': ['human bones', 'Michelle']
                          },'shelf2': {'Curious George':['monkey', 'Christopher'], 
                          'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
                          'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
                          'Bone': ['human bones', 'Michelle']
                          }
                          
              }
        return data

   
    
    def _createGrid(self):
        """Create the buttons."""
        self.icons = {}
        GridLayout = QGridLayout()
    
        data = self.getLibraryInfo()
        for row, books in data.items():
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
                box.setCheckable(True)
                

                boxLayout = QVBoxLayout()
            
                box.setLayout(boxLayout)

                boxLayout.addWidget(image)
                self.icons[bookName] =  box
                
                
                # text = QLabel(bookName)
                # GridLayout.addWidget(text, row, col)
                
                GridLayout.addWidget(self.icons[bookName], row, col)
            
        self.generalLayout.addLayout(GridLayout, 0, 0)

        
        



def main():
    
    pycalc = QApplication(sys.argv)
    
    view = LibUi()
    view.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()