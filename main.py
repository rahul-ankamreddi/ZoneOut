import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QDateTime


class FloatingButtonApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 100, 100)  # Initial position and size

        # Create the floating button
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(0, 0, 100, 40)
        self.button.clicked.connect(self.record_click_time)

        # Create a label to show the last click time
        self.label = QLabel("Last Click: None", self)
        self.label.setGeometry(0, 50, 200, 40)
        self.label.setStyleSheet("color: white; background: transparent;")

        # Button style
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; 
                color: white; 
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

    def record_click_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.label.setText(f"Last Click: {current_time}")
        print(f"Button clicked at {current_time}")

    def mousePressEvent(self, event):
        # Enable dragging the floating window
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        # Update window position while dragging
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = FloatingButtonApp()
    main_window.show()
    sys.exit(app.exec_())
