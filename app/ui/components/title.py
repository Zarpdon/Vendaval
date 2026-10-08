from PySide6.QtWidgets import QLabel

class Title(QLabel):
    def __init__(self, text: str, size: int = 24):
        super().__init__(text)

        self.setObjectName("title")
        self.setProperty("size", size)