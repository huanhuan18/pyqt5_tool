from test_widget import Ui_Form
from PyQt5.Qt import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Login_pane(QWidget, Ui_Form):
    show_mainpane_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.resize(300, 300)

    def show_mainwindow(self):
        print("显示mainwindow")
        self.show_mainpane_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pane = Login_pane()

    login_pane.show()
    sys.exit(app.exec_())
