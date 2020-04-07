#!/usr/bin/env python3
import fileinput
import glob
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import config
import paths
from core import readTable
from ui.centralFrame import CenterFrame


def fileInput(folder):
    files_list = glob.glob(folder + "/*.css")
    ls = []
    with fileinput.input(files=files_list) as f:
        for line in f:
            ls.append(line)
    return "".join(ls)


class ToolBar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(42)
        self.addAction(QAction("open", self))


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.cfg = config.Config(paths.CONFIG)
        self.label = CenterFrame()
        self.setCentralWidget(self.label)
        self.toolBar = ToolBar()
        self.addToolBar(self.toolBar)
        self._set_style_sheet("base")
        self.currentItem = None
        self.altFlag = False

        self.table = readTable.Table(paths.DATA / 'slovar1.xlsx')
        self.newGame()

    def _set_style_sheet(self, sheetName):
        """
        :param sheetName: str имя стиля
        """
        styleSheet = fileInput(str(paths.CSS / sheetName))
        QApplication.instance().setStyleSheet(styleSheet)

    def newGame(self):
        self.table.shuffle()
        self.table.reset()


    def setCurrentItemAltText(self):
        if self.currentItem is not None:
            self.label.setText(
                """{}\n[{}]""".format(self.currentItem.ru, self.currentItem.rutrans))

    def setCurrentItemText(self):
        if self.currentItem is not None:
            self.label.setText(self.currentItem.en)

    def setFinishText(self):
        self.label.setText("Finish")

    def nextItem(self):
        self.altFlag = False
        item = next(self.table)
        self.currentItem = item
        if self.currentItem is not None:
            self.setCurrentItemText()
        else:
            self.setFinishText()
            self.newGame()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.nextItem()
        elif event.key() == Qt.Key_Space:
            if self.altFlag:
                self.altFlag = False
                self.setCurrentItemText()
            else:
                self.altFlag = True
                self.setCurrentItemAltText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())
