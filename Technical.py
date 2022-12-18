from dataclasses import dataclass


@dataclass(frozen=True)
class Technic:

    name: str
    price: float
    is_or_no: bool

    def make_category(self, other):
        category1 = "Дорогой"
        category2 = "Бюджетный"
        return category1 if self.price > other.price else category2

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ge__(self, other):
        return self.name >= other.name