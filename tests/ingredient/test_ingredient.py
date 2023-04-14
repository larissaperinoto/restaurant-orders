from src.models.ingredient import Ingredient


def test_ingredient():
    instance = Ingredient('lactose')
    instance2 = Ingredient('seafood')

    assert instance.name == 'lactose'
    assert hash(instance) == hash('lactose')
    assert repr(instance) == "Ingredient('lactose')"
    assert instance == instance
    assert instance != instance2
    assert instance.restrictions == set()
