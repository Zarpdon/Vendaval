from PySide6.QtWidgets import QMainWindow

from app.ui.main_layout import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = MainLayout()

        self.setCentralWidget(layout.container)

        self.setWindowTitle("Vendaval")
        self.resize(1000, 700)