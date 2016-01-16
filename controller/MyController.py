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

    def connectButtons(self):
        """
        Button mit Methode verbinden
        :return:
        """
        self.myForm.pushButton.clicked.connect(lambda: self.click( self.myForm.pushButton.text()))
        self.myForm.pushButton_2.clicked.connect(lambda: self.click( self.myForm.pushButton_2.text()))

    def click(self,beschriftung):
        """
        Regelt, was beim druecken eines Buttons passieren soll
        :return:
        """
        text=""
        if beschriftung == "Load":
            text = self.myModel.loadCSV()
        elif beschriftung == "Save":
            self.myModel.saveCSV(self.myForm.textEdit.toPlainText())
            text = "Folgendes wurde gespeichert:\n" + self.myModel.loadCSV()
        self.output(text)

    def output(self, text):
        self.myForm.textEdit.clear()
        self.myForm.textEdit.insertPlainText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())