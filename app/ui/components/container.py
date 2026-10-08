from PySide6.QtWidgets import QVBoxLayout, QWidget


class Container(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)