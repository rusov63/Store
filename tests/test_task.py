from utils.task import Store

def test_total_cost():
    """Общая стоимость товара"""
    store = Store('laptop_asus', 30_000, 6)
    store1 = Store('tablet_lenovo', 15_000, 10)
    assert store.total_cost() == 180000
    assert store1.total_cost() == 150000

def test_price_discount():
    """Скидка для товара"""
    store = Store('laptop_asus', 30_000, 6)
    store1 = Store('tablet_lenovo', 15_000, 10)
    assert store.price_discount() == 27000
    assert store1.price_discount() == 13500


