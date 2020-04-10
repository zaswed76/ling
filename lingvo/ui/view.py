

#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class GraphicsImage(QGraphicsPixmapItem):
    def __init__(self, imgpath=None, *__args):
        super().__init__(*__args)

class GraphicsText(QGraphicsTextItem):
    def __init__(self, scene, *__args):
        super().__init__(*__args)
        self.scene = scene
        font = QFont("Helvetica", 142, 400)
        self.setFont(font)

    def to_center(self):
        w = self.scene.width() / 2 - self.boundingRect().width() / 2
        h = self.scene.height() / 2 - self.boundingRect().height() / 2
        self.setPos(w, h)

class View(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setFixedSize(504, 504)


class Scene(QGraphicsScene):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setSceneRect(0, 0, 500, 500)

class Widget(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(504, 504)
        self.box = QHBoxLayout(self)
        self.view = View()
        self.scene = Scene(self)
        self.view.setScene(self.scene)
        self.view.setSceneRect(0, 0, 500, 500)
        self.box.addWidget(self.view)

        item = GraphicsText(self.scene, "cat")
        self.scene.addItem(item)
        self.sceneRect = self.scene.sceneRect()
        item.to_center()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()

    main.show()
    sys.exit(app.exec_())