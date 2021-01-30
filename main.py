import sys
from PyQt5 import uic, QtWidgets
from voice import say
from process import callback

Form, _ = uic.loadUiType("design.ui")

#say("Hello, I am Atlas, your new assistant, how can I be helpful?")

class Ui (QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.assistantStart)

    def assistantStart(self):
        callback()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())