import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from gui_design import Ui_MainWindow

class MainWindow:
    def __init__(self) -> None:
        self.main_Win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_Win)


        self.ui.stackedWidget.setCurrentWidget(self.ui.Welcome)

        self.ui.SubmitButton.clicked.connect(self.showDisplay)
    
    def show(self):
        self.main_Win.show()
    
    def showDisplay(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Display)
        self.ui.promptlabel.setText(f"Hello, {self.ui.input.text()}")
    #     self.show_contents()

    # def show_contents(self):
    #     library = csv_reader()
    #     self.ui.Content.setText(library)



def window():
    app = QApplication(sys.argv)
    #calling the class
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()
