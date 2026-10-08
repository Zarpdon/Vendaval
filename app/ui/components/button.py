from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

        self.setObjectName("button")
        self.setCursor(Qt.CursorShape.PointingHandCursor)