class Product:
    def __init__(
        self,
        id: int,
        name: str,
        price_in_cents: int,
        stock: int = 0,
    ):
        if price_in_cents < 0:
            raise ValueError("Price cannot be negative")

        self.id = id
        self.name = name
        self.price_in_cents = price_in_cents
        self.stock = stock

    def update_stock(self, quantity: int):
        new_stock = self.stock + quantity

        if new_stock < 0:
            raise ValueError("Stock cannot be negative")

        self.stock = new_stock