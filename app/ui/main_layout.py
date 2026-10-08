from app.ui.components import Button, Container, Title

class MainLayout:
    def __init__(self):
        self.container = Container()

        self.title = Title("Vendaval")
        self.button = Button("Continuar")

        self.container.layout.addWidget(self.title)
        self.container.layout.addWidget(self.button)