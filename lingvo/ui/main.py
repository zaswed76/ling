#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
import paths
import config

class InsertToolBar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(42)
        self.addAction(QAction("img", self))

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.cfg = config.Config(paths.CONFIG)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())