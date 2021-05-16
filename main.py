import sys
from PyQt5 import uic, QtWidgets
from voice import say
from process import callback, FileFinder

Form, _ = uic.loadUiType("design.ui")
class Ui (QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.AssistantStart)
        self.fileLine.setPlaceholderText("Enter file name:")
        self.saveButton.clicked.connect(self.Files)

    def AssistantStart(self):
        callback()
    def Files(self):
       filename = self.fileLine.text()
       FileFinder(filename)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
