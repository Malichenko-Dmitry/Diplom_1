import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_price.return_value = 10.0
    ingredient.get_type.return_value = "FILLING"
    return ingredient

@pytest.fixture
def mock_bun_class():
    with patch('database.Bun') as mock_bun_cls:
        yield mock_bun_cls

@pytest.fixture
def mock_ingredient_class():
    with patch('database.Ingredient') as mock_ing_cls:
        yield mock_ing_cls

@pytest.fixture
def mock_burger_class():
    with patch('burger.Burger') as mock_burger_cls:
        yield mock_burger_cls

@pytest.fixture
def patched_bun_instance():
    bun_mock = MagicMock()
    return bun_mock

@pytest.fixture
def patched_ingredient_instance():
    ingredient_mock = MagicMock()
    return ingredient_mock

@pytest.fixture
def patched_burger_instance():
    burger_mock = MagicMock()
    return burger_mock
