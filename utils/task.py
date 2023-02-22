class Store:
    discount = 0.9

    def __init__(self, product_name, unit_price, quantity):
        """Название товара, цена за единицу и количество товара в магазине"""
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self):
        """Общая стоимость товара"""
        return self.quantity * self.unit_price

    def price_discount(self):
        """Скидка для товара"""
        return self.unit_price * self.discount


store = Store('laptop_asus', 30_000, 6)
print(store.product_name)
store.total_cost()
print(f'Общая стоимость товара: {store.total_cost()}')
store.price_discount()
print(f'Стоимость товара с учетом скидки: {store.unit_price}')

store1 = Store('tablet_lenovo', 15_000, 10)
print(store1.product_name)
print(f'Общая стоимость товара: {store1.total_cost()}')
store1.price_discount()
print(f'Стоимость товара с учетом скидки: {store1.unit_price}')