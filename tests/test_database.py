from unittest.mock import MagicMock
from database import Database
from bun import Bun
from ingredient import Ingredient

class TestDatabase:

    def test_available_buns_returns_list(self):
        buns = Database().available_buns()
        assert isinstance(buns, list)


    def test_available_buns_elements_type(self):
        buns = Database().available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)


    def test_available_buns_contains_expected_names(self):
        buns = Database().available_buns()
        bun_names = [bun.get_name() for bun in buns]
        expected_names = ["black bun", "white bun", "red bun"]
        for name in expected_names:
            assert name in bun_names

    def test_available_ingredients_returns_list(self):
        ingredients = Database().available_ingredients()
        assert isinstance(ingredients, list)


    def test_available_ingredients_elements_type(self):
        ingredients = Database().available_ingredients()
        assert all(isinstance(ing, Ingredient) for ing in ingredients)


    def test_available_ingredients_contains_expected_names(self):
        ingredients = Database().available_ingredients()
        ingredient_names = [ing.get_name() for ing in ingredients]
        expected_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        for name in expected_names:
            assert name in ingredient_names


    def test_bun_get_name_and_price(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"
        assert bun.get_price() == 100


    def test_ingredient_getters(self):
        ing = Ingredient("SAUCE", "hot sauce", 100)
        assert ing.get_name() == "hot sauce"
        assert ing.get_type() == "SAUCE"
        assert ing.get_price() == 100


    def test_database_initialization_with_mocks(self, mock_bun_class, mock_ingredient_class):
        mock_bun1 = MagicMock(spec=Bun)
        mock_bun1.get_name.return_value = 'mocked bun'
        mock_bun1.get_price.return_value = 123
        mock_ing1 = MagicMock(spec=Ingredient)
        mock_ing1.get_name.return_value = 'mocked ingredient'
        mock_ing1.get_price.return_value = 456
        mock_bun_class.side_effect = [mock_bun1] * 3
        mock_ingredient_class.side_effect = [mock_ing1] * 6
        db_instance = Database()
        buns = db_instance.available_buns()
        ingredients = db_instance.available_ingredients()
        assert all(bun.get_name() == 'mocked bun' for bun in buns)
        assert all(ing.get_name() == 'mocked ingredient' for ing in ingredients)


    def test_get_price_calculation_with_mocks(self):
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 150
        ingredient1 = MagicMock()
        ingredient1.get_price.return_value = 50
        ingredient2 = MagicMock()
        ingredient2.get_price.return_value = 70
        burger_mock = MagicMock()
        burger_mock.bun = mock_bun
        burger_mock.ingredients = [ingredient1, ingredient2]
        expected_total_price = (mock_bun.get_price.return_value * 2) + sum(
            ing.get_price() for ing in burger_mock.ingredients)

        burger_mock.get_price.return_value = expected_total_price
        price_result = burger_mock.get_price()
        assert price_result == expected_total_price
