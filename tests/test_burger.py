import pytest
from unittest.mock import Mock
from burger import Burger


def test_set_buns_assigns_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient_appends_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient

def test_remove_ingredient_removes_correct_index(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    another_mock = Mock()
    burger.add_ingredient(another_mock)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == another_mock


@pytest.mark.parametrize("initial_indices,new_index", [
    ([0, 1, 2], 2),
    ([0, 1], 0),
])
def test_move_ingredient_moves_element_correctly(initial_indices, new_index, mock_bun, mock_ingredient):
    ingredients = []
    for i in initial_indices:
        mock_ing = Mock()
        mock_ing.get_name.return_value = f"Ingredient {i}"
        ingredients.append(mock_ing)
    burger = Burger()
    for ing in ingredients:
        burger.add_ingredient(ing)
    burger.move_ingredient(0, new_index)
    expected_order = ingredients[1:] + [ingredients[0]] if new_index > 0 else [ingredients[0]] + ingredients[1:]
    assert burger.ingredients[new_index].get_name() == f"Ingredient {initial_indices[0]}"


@pytest.mark.parametrize("bun_price,ingredients_prices", [
    (50.0, [10.0, 20.0]),
    (100.0, [5.5, 4.5]),
])
def test_get_price_calculates_correctly(bun_price, ingredients_prices, mock_bun, mock_ingredient):
    mock_bun.get_name.return_value = "Test Bun"
    mock_bun.get_price.return_value = bun_price
    ingredients = []
    for price in ingredients_prices:
        ing = Mock()
        ing.get_name.return_value = "Ing"
        ing.get_price.return_value = price
        ingredients.append(ing)

    burger = Burger()
    burger.set_buns(mock_bun)

    for ing in ingredients:
        burger.add_ingredient(ing)

    expected_price = bun_price * 2 + sum(ingredients_prices)
    actual_price = burger.get_price()
    assert abs(actual_price - expected_price) < 1e-6


def test_get_receipt_includes_all_parts(mock_bun, mock_ingredient):
    mock_bun.get_name.return_value = "Sesame"
    mock_bun.get_price.return_value = 50
    ingredient1 = Mock()
    ingredient1.get_name.return_value = "Lettuce"
    ingredient1.get_type.return_value = "FILLING"
    ingredient1.get_price.return_value = 5
    ingredient2 = Mock()
    ingredient2.get_name.return_value = "Ketchup"
    ingredient2.get_type.return_value = "SAUCE"
    ingredient2.get_price.return_value = 2
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    receipt_str = burger.get_receipt()
    assert "(==== Sesame ====)" in receipt_str
    assert "= filling Lettuce =" in receipt_str.lower() or "= filling lettuce =" in receipt_str.lower()
    assert "= sauce Ketchup =" in receipt_str.lower() or "= sauce ketchup =" in receipt_str.lower()
    expected_total = mock_bun.get_price() * 2 + 5 + 2
    assert f"Price: {expected_total}" in receipt_str