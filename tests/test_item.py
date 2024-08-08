import pytest


from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_item_apply_discount(item1):
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0


def test_string_to_number():
    assert Item.string_to_number('101.101') == 101


def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__(item1):
    assert str(item1) == 'Смартфон'


def test_name(item1):
    assert item1.name == 'Смартфон'
    item1.name = "Smartphone_12"
    assert item1.name == "Smartphone"


