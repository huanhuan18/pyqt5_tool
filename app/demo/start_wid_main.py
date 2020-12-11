from start_widget import Login_pane
from start_mainwindow import Main_pane

"""为了不让以上两个页面有耦合性，所以建立本 页面"""

from PyQt5.Qt import *
from PyQt5 import QtCore

if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    login = Login_pane()
    mainpane = Main_pane()


    def show_mainpane():
        print("展示")
        mainpane.show()


    login.show_mainpane_signal.connect(show_mainpane)

    login.show()
    sys.exit(app.exec_())
