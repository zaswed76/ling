import sys
from PyQt5.QtWidgets import QApplication

from ui import main as _main

def main():
    app = QApplication(sys.argv)
    main = _main.Main()
    main.show()
    sys.exit(app.exec_())

main()


