#!/usr/bin/env python3

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CenterLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("New\nGame")
        self.setStyleSheet("""QLabel{color: #0BBB24;}""")
        self.setAlignment(Qt.AlignCenter)

        self._rect = self.rect()

        self.image = QLabel(self)
        self.image.setFixedSize(150, 150)

    def setImage(self, path):
        self.image.move(self._rect.topRight().x() - self.image.width() * 1.5 + 5,
                        self._rect.topRight().y() + 5)
        pixmap = QPixmap(path)
        pxm = pixmap.scaled(150, 150, 1, 1)
        self.image.setPixmap(pxm)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
