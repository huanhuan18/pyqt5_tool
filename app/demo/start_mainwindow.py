from test_mainwindow import Ui_MainWindow
from PyQt5.Qt import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore


class Main_pane(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 涉及到背景图片的要加上这句，否则Qt会把样式禁掉
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.resize(629, 557)


if __name__ == '__main__':
    # Qt designer预览的和执行的窗口不一致，加上下面这句
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    main_pane = Main_pane()

    main_pane.show()
    sys.exit(app.exec_())
