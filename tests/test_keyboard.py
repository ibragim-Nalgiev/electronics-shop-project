import pytest

from src.keyboard import KeyBoard


@pytest.fixture()
def keyboard1():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test__str__(keyboard1):
    assert str(keyboard1.language) == "EN"


def test_language_setter(keyboard1):
    with pytest.raises(AttributeError):
        keyboard1.language = "CN"


def test_change_lang(keyboard1):
    keyboard1.language = "RU"
    assert keyboard1.language == "RU"

