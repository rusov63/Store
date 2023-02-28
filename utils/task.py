import csv

class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, count):
        self.__name = name
        self.price = price
        self.count = count
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self.__name = name

    def calculate_total_price(self):
        return self.price * self.count

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r', encoding='windows-1251') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
            for a in rows[1:len(rows)]:
                if Item.is_integer(float(a[1])):
                    a[1] = int(a[1])
                if Item.is_integer(float(a[2])):
                    a[2] = int(a[2])
                cls(a[0], a[1], a[2])

    @staticmethod
    def is_integer(num):
        if num - int(num) == 0:
            return True
        else:
            return False

# item = Item("Ноутбук", 20000, 5)
# print(item)
# item.name = 'Смартфон'
# print(item.name)
# print(item)
# item.name = 'СуперСмартфон'
# print(item)
#Item.instantiate_from_csv()
#print(Item.all)
#print(len(Item.all))
# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))


