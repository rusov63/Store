from utils.task import Item
def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100_000

def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False

def test__repr__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__repr__() != Item('Смартфон', '10000', '20')

def test__str__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__str__() != Item('Смартфон', '10000', '20')

