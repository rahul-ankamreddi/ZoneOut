# installed
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("ZoneOut")

        layout = QVBoxLayout()

        capture_button = QPushButton("Capture")

        layout.addWidget(capture_button)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
