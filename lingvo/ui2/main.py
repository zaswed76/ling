import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import paths
from libs.dictsequence import DictSeq

from ui2.centrallframe import ChooseDictStack, ViewStack, CenterFrame







class ToolBar(QToolBar):
    def __init__(self, main, *__args):
        super().__init__(*__args)
        self.main = main
        self.setFixedHeight(42)
        self.addAction(QAction(QIcon(str(paths.ICONS / "dict.png")), "chooseDict", self))
        # self.dictList = QComboBox(self)
        # self.dictList.currentIndexChanged.connect(self.currentDictChanged)
        # self.actionTriggered.connect(self.toolActions)
        # self.updateDictList()

    # def currentDictChanged(self, text):
    #     print(self.dictList.currentText())
    #     print(text)
    #
    #
    # def toolActions(self, action):
    #     print(action)
    #
    # def updateDictList(self):
    #     self.dictList.addItems(self.main.dictList)
    #     self.addWidget(self.dictList)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dictSeq = DictSeq(paths.DATA)
        self.resize(600, 600)
        self.centerFrame = CenterFrame(self)
        self.setCentralWidget(self.centerFrame)
        self.__setToolBar()
        self.stackWidgets = {}
        self.chooseDictStack = ChooseDictStack(self)
        self.viewStack = ViewStack(self)
        self.stackWidgets["chooseDict"] = self.chooseDictStack
        self.stackWidgets["view"] = self.viewStack
        self.centerFrame.setStackWidgets(self.stackWidgets)
        self.centerFrame.initStack()
        self.centerFrame.showStack("view")

    def __setToolBar(self):
        self.toolBar = ToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar.actionTriggered.connect(self.toolActions)


    def toolActions(self, act):
        getattr(self, "{}Action".format(act.text()))()

    def chooseDictAction(self):
        print("-chooseDictAction-")

    @property
    def dictList(self):
        return self.dictSeq.dictNames()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())