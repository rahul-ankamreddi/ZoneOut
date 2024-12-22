# built-in
import sys

# installed
from PyQt5.QtWidgets import QApplication

# local
from MainWindow import MainWindow


if __name__ == '__main__':

    try:

        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

    except Exception as e:
        print(e)
    else:
        app.exec_()
