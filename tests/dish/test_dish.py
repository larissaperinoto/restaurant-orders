from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    instance = Dish('Abacate', 3.4)
    another_instance = Dish('Alho', 1.90)

    assert instance.name == 'Abacate'

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('a', '2332')

    error = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=error):
        Dish('a', -3)

    assert repr(instance) == "Dish('Abacate', R$3.40)"
    assert instance == instance
    assert instance != another_instance
    assert hash(instance) == hash(repr(instance))
    assert hash(instance) != hash(repr(another_instance))

    instance.add_ingredient_dependency(Ingredient('Água'), 200)
    assert instance.recipe == {Ingredient('Água'): 200}
    assert instance.get_ingredients() == set(instance.recipe.keys())
    assert instance.get_restrictions() == set()
