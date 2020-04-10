#!/usr/bin/env python3
import fileinput
import glob
import sys
from pathlib import Path

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import config
import paths
from core import readTable
from ui.label import CenterLabel

def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)

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
        self.addAction(QAction(QIcon(str(paths.ICONS / "open.png")), "Open", self))
        self.addAction(QAction(QIcon(str(paths.ICONS / "dict.png")), "Dict", self))
        # self.dicts = QComboBox()
        # self.dicts.addItems(["1", "2"])
        # self.addWidget(self.dicts)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.cfg = config.Config(paths.CONFIG)
        self.label = CenterLabel()
        self.setCentralWidget(self.label)
        self.toolBar = ToolBar()
        self.toolBar.actionTriggered.connect(self.toolActions)
        self.addToolBar(self.toolBar)
        self._set_style_sheet("base")
        self.currentItem = None
        self.altFlag = False
        self.currentDict = "slovar1"
        self.currentDictPath = paths.DATA / self.currentDict
        self.table = None
        self.setCurrentDict(self.cfg["core"]["lastFileDict"])

    def actOpen(self):
        files, _ = QFileDialog.getOpenFileName(None, directory=str(paths.DATA))
        if files:
            self.setCurrentDict(files)

    def actDict(self):
        print("787")

    def setCurrentDict(self, file):
        print(file, type(file))
        if not file:
            return

        base = os.path.basename(file)
        dirname = os.path.dirname(file)
        print(base, "888")
        self.currentDict = os.path.splitext(base)[0]
        self.currentDictPath = paths.DATA / self.currentDict
        self.table = readTable.Table(self.currentDictPath / base)
        self.cfg["core"]["lastFileDict"] = file
        self.newGame()

    def toolActions(self, act):
        getattr(self, "act{}".format(act.text()))()

    def _set_style_sheet(self, sheetName):
        """
        :param sheetName: str имя стиля
        """
        styleSheet = fileInput(str(paths.CSS / sheetName))
        QApplication.instance().setStyleSheet(styleSheet)

    def newGame(self):
        self.table.shuffle()
        self.table.reset()
        print(self.table)

    def setCurrentItemAltText(self):
        if self.currentItem is not None:
            self.label.setText(
                """{}\n[{}]""".format(self.currentItem.en, self.currentItem.rutrans))
            self.setAltStyle()

    def setCurrentItemText(self):
        if self.currentItem is not None:
            self.label.setText(self.currentItem.ru)
            self.label.image.clear()
            self.setBaseStyle()

    def setFinishText(self):
        self.label.image.clear()
        self.label.setText("Finish")
        self.label.setStyleSheet("""QLabel{color: #0BBB24;}""")
    def setImage(self):
        if self.currentItem is None:
            return
        st = str(self.currentDictPath) + "/{}.*".format(self.currentItem.en)
        image_lst = glob.glob(st)
        if image_lst:
            image = image_lst[0]
            self.label.setImage(image)


    def nextItem(self):
        if self.table is None:
            return
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
                self.setImage()

    def closeEvent(self, *args, **kwargs):
        self.cfg.save()

    def setBaseStyle(self):
        self.label.setStyleSheet("""
    QLabel{
    background-color: #eeeeee;
    color: #3a3a3a;
    font-family: Helvetica;
    font-size: 124pt;
    font-weight: 600;
    alignment: center;
}
        """)

    def setAltStyle(self):
        self.label.setStyleSheet("""
    QLabel{
    background-color: #eeeeee;
    color: #464646;
    font-family: Helvetica;
    font-size: 114pt;
    font-weight: 500;
    alignment: center;
}""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())
