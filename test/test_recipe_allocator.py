from definitions.test_jsons import(
    TEST_STOCK_DICT,
    TEST_DEFAULT_ORDERS_DICT
    )
from src.recipe_allocator import *

import pytest


@pytest.mark.parametrize("test_orders,box_type,expected_value",
                         [
                             pytest.param(TEST_DEFAULT_ORDERS_DICT, "vegetarian", 67273),
                             pytest.param(TEST_DEFAULT_ORDERS_DICT, "gourmet", 184289),
                         ])
def test_count_orders(test_orders: dict, box_type:str, expected_value: int):
    assert count_orders(test_orders, box_type=box_type) == expected_value


@pytest.mark.parametrize("test_stock,box_type,expected_value",
                         [
                             pytest.param(TEST_STOCK_DICT, "vegetarian", 67816),
                             pytest.param(TEST_STOCK_DICT, "gourmet", 186796),
                         ])
def test_count_stock(test_stock: dict, box_type: str, expected_value: int):
    assert count_stock(test_stock, box_type=box_type) == expected_value
