#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



class CenterFrame(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("New\nGame")
        self.setAlignment(Qt.AlignCenter)


        #


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())