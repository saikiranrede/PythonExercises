class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        self.name = name
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name': name, 'price': price})
        return self.items

    def stock_price(self):
        return sum([item['price'] for item in self.items])


store = Store('Kiran')
print(store.items)
print(store.add_item('Sai', 56))
print(store.add_item('Kiran', 88))
print(store.stock_price())
