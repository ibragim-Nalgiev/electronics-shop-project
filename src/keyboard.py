from src.item import Item


class MixinLanguage:
    def __init__(self, language='EN'):
        self._language = language  # Используем защищенный атрибут

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in ['EN', 'RU']:
            self._language = value
        else:
            raise AttributeError("Unsupported language")

    def change_lang(self):
        self.language = 'RU' if self.language == 'EN' else 'EN'
        return self

    def __str__(self):
        return f"{self.language}"


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        Item.__init__(self, name, price, quantity)
        MixinLanguage.__init__(self)




