import sys
from PySide.QtGui import *
from PySide import QtCore, QtGui
from model import MyModel
from view import MyView

class MyController(QWidget):

    """ MVC pattern: Creates a controller - mvc pattern.
    """
    def __init__(self, parent=None):
        """
        Create a new controller with a object MyView and a object MyModel
        Autor: Andi Ernhofer
        """
        super().__init__(parent)
        self.myForm = MyView.Ui_Form()
        self.myForm.setupUi(self)
        self.myModel = MyModel.MyModel()
        #Buttons in ein Array speichern
        #self.addButtons()
        #connect the buttons with the clicked signal
        self.connectButtons()
        # start a new game
        #self.start()

        self.myForm.textBrowser.insertPlainText("hallo")
        self.myForm.textBrowser.insertPlainText("\nmuh")

    def connectButtons(self):
        """
        Buttons connecten
        :return:
        """
        self.myForm.pushButton.clicked.connect(self.click)

    def click(self):
        """
        Regelt, was beim druecken eines Buttons passieren soll
        :param nr: Die Nummer des geklickten Buttons
        :return:
        """
        #Ueberpruefen ob der richtige Button gedrueckt wurde und ob das Spiel zu Ende ist.
        print("Click")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())