class Store:
    discount = 0.9

    def __init__(self, product_name, unit_price, quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    def price_discount(self):
        self.unit_price = self.unit_price * self.discount


store = Store('laptop_asus', 30000, 6)
print(store.product_name)
print(store.unit_price)
store.price_discount()
print(store.unit_price)

store1 = Store('tablet_lenovo', 15000, 10)
print(store1.product_name)
print(store1.unit_price)
store1.price_discount()
print(store1.unit_price)