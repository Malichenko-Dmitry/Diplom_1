import pytest
from bun import Bun

bun_test_cases = [
    ("white bun", 200),
    ("black bun", 100),
    ("red bun", 300),
]

class TestBun:
    @pytest.mark.parametrize("name, price", bun_test_cases)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", bun_test_cases)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price