from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)


def test_init(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_number_of_sim_ok(phone1):
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test__add__(phone1, item1):
    assert phone1 + item1 == 25

