# built-ins
import sys

# installed
from PyQt5.QtWidgets import QApplication

# local
from MainWindow import MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
