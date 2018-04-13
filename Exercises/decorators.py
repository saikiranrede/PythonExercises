class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"

        return Store(store.name+" - franchise")  #trying to return a new Store object

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

        return '{}, total stock price: {}'.format(store.name, store.stock_price())

store = Store('Sai')
store2 = Store('Kiran')

print(Store.franchise(store))
print(Store.franchise(store2))
#print(Store.franchise('reddy'))

store.add_item('Sai', 54)
store.add_item('Kiran', 86)

print(Store.store_details(store))
print(Store.store_details(store2))
