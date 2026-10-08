class Sale:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        self.items.append({
            "product": product,
            "quantity": quantity,
        })
    def get_total(self) -> int:
        return sum(
            item["product"].price_in_cents * item["quantity"]
            for item in self.items
        )