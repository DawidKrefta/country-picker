import sys
from PyQt6.QtWidgets import QApplication
from .ui import MainWindow
from .controller import AppController


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = AppController(window)
    window.show()
    sys.exit(app.exec())
