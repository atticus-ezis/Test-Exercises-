class Inventory:
    def __init__(self):
        self.list = []

    def add_item(self, item):
        self.list.append(item)
        print(f"{item} added to inventory.")

    def view_items(self):
        print(f"Current Inventory: {self}")

    def __str__(self):
        return ', '.join(str(item) for item in self.list)


class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Item: {self.name}, quantity: {self.quantity}, price: ${self.price}"

beans = Item('beans',200,3)
inv = Inventory()
inv.add_item(beans)
inv.view_items()


