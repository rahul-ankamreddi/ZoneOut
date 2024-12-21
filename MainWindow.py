# installed
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("ZoneOut")
