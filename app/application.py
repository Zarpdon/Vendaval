import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow
from app.utils.styles import load_stylesheet


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.app.setStyleSheet(load_stylesheet())

        self.window.show()
        self.app.exec()