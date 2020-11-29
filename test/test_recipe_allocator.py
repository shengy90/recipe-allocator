from definitions.test_jsons import (
    TEST_STOCK_DICT,
    TEST_STOCK_4VEGE1GOURMET_DICT,
    TEST_DEFAULT_ORDERS_DICT,
    TEST_DEFAULT_ORDERS_1_DICT,
    )
from definitions.definitions import constraints_priority
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


@pytest.mark.parametrize("stock_dict,constraint,expected_recipe_value,expected_stock_value",
                         [
                             pytest.param(
                                 {"recipe_3": {"stock_count": 10, "box_type": "vegetarian"},
                                  "recipe_5": {"stock_count": 20, "box_type": "vegetarian"},
                                  "recipe_7": {"stock_count": 30, "box_type": "vegetarian"}},
                                 "vegetarian",
                                 "recipe_7",
                                 30
                             ),
                             pytest.param(
                                 {"recipe_19": {"stock_count": 50, "box_type": "vegetarian"},
                                  "recipe_03": {"stock_count": 20, "box_type": "vegetarian"},
                                  "recipe_46": {"stock_count": 10, "box_type": "vegetarian"}},
                                 "vegetarian",
                                 "recipe_19",
                                 50
                             ),
                             pytest.param(TEST_STOCK_DICT, "vegetarian", "recipe_6", 43705),
                         ])
def get_recipe_with_highest_stock_given_constraint(stock_dict, constraint, expected_recipe_value, expected_stock_value):
    output_recipe_name, output_recipe_stock = get_recipe_with_highest_stock_given_constraint(stock_dict, constraint)
    assert output_recipe_name == expected_recipe_value and output_recipe_stock == expected_stock_value


@pytest.mark.parametrize("stock_dict,recipe,allocated_stock,expected_value",
                         [
                             pytest.param(TEST_STOCK_DICT, "recipe_3", 123, 1682),
                             pytest.param(TEST_STOCK_DICT, "recipe_8", 10000, 0,  marks=pytest.mark.xfail(raises=AssertionError)),
                         ])
def test_update_stock_levels(stock_dict, recipe, allocated_stock, expected_value):
    updated_stock = update_stock_levels(stock_dict, recipe, allocated_stock)
    assert updated_stock[recipe]['stock_count'] == expected_value


@pytest.mark.parametrize("orders_dict,constraints_priority,expected_value",
                         [
                             pytest.param(TEST_DEFAULT_ORDERS_DICT,
                                          constraints_priority,
                                          ["vegetarian:four_recipes:four_portions",
                                           "vegetarian:three_recipes:four_portions",
                                           "vegetarian:two_recipes:four_portions",
                                           "vegetarian:four_recipes:two_portions",
                                           "vegetarian:three_recipes:two_portions",
                                           "vegetarian:two_recipes:two_portions",
                                           "gourmet:four_recipes:four_portions",
                                           "gourmet:three_recipes:four_portions",
                                           "gourmet:two_recipes:four_portions",
                                           "gourmet:four_recipes:two_portions",
                                           "gourmet:three_recipes:two_portions",
                                           "gourmet:two_recipes:two_portions",
                                           ]
                                          ),

                         ])
def test_compile_order_allocation_list(orders_dict, constraints_priority, expected_value):
    assert compile_order_allocation_list(orders_dict, constraints_priority) == expected_value
