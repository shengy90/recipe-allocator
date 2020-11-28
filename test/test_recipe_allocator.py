from definitions.test_jsons import (
    TEST_STOCK_DICT,
    TEST_STOCK_4VEGE1GOURMET_DICT,
    TEST_DEFAULT_ORDERS_DICT,
    TEST_DEFAULT_ORDERS_1_DICT,
    )
from src.recipe_allocator import *

import pytest


@pytest.mark.parametrize("test_orders,box_type,expected_value_orders,expected_value_boxes",
                         [
                             pytest.param(TEST_DEFAULT_ORDERS_DICT, "vegetarian", 67273, 584992),
                             pytest.param(TEST_DEFAULT_ORDERS_DICT, "gourmet", 184289, 1220712),
                             pytest.param(TEST_DEFAULT_ORDERS_1_DICT, "vegetarian", 6, 54),
                         ])
def test_count_orders(test_orders: dict, box_type:str, expected_value_orders, expected_value_boxes: int):
    orders, boxes = count_orders_and_boxes(test_orders, box_type=box_type)
    assert orders == expected_value_orders and boxes == expected_value_boxes


@pytest.mark.parametrize("test_stock,box_type,expected_value",
                         [
                             pytest.param(TEST_STOCK_DICT, "vegetarian", 67816),
                             pytest.param(TEST_STOCK_DICT, "gourmet", 186796),
                             pytest.param(TEST_STOCK_4VEGE1GOURMET_DICT, "gourmet", 1),
                             pytest.param(TEST_STOCK_4VEGE1GOURMET_DICT, "vegetarian", 4),
                         ])
def test_count_stock(test_stock: dict, box_type: str, expected_value: int):
    assert count_stock(test_stock, box_type=box_type) == expected_value
