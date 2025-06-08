import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

ingredient_test_cases = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150),
]

@pytest.mark.parametrize("ingredient_type, expected_name, expected_price", ingredient_test_cases)
def test_ingredient_type_getter(ingredient_type, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type, expected_name, expected_price)
    assert ingredient.get_type() == ingredient_type

@pytest.mark.parametrize("ingredient_type, expected_name, expected_price", ingredient_test_cases)
def test_ingredient_name_getter(ingredient_type, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type, expected_name, expected_price)
    assert ingredient.get_name() == expected_name

@pytest.mark.parametrize("ingredient_type, expected_name, expected_price", ingredient_test_cases)
def test_ingredient_price_getter(ingredient_type, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type, expected_name, expected_price)
    assert ingredient.get_price() == expected_price