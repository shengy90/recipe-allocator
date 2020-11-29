from definitions.test_files_allocated_stock import (
    happy_case,
    duplicated_recipes,
    vegetarian_orders_receiving_gourmet_boxes,
    )

from definitions.test_jsons import (
    TEST_DEFAULT_ORDERS_1_DICT,
    TEST_DEFAULT_ORDERS_3_DICT,
    TEST_STOCK_4VEGE4GOURMET20EA_DICT,
    )

from src.constraints_checker import *

import pytest


@pytest.mark.parametrize("allocated_stocks,expected_value",
                         [
                             pytest.param(happy_case.HAPPY_CASE["vegetarian"], 54),
                             pytest.param(happy_case.HAPPY_CASE["gourmet"], 54),
                         ])
def test_tally_stocks(allocated_stocks, expected_value):
    count_stocks = tally_stocks(allocated_stocks)
    assert count_stocks == expected_value


@pytest.mark.parametrize("stock_dict,orders_dict,expected_value",
                         [
                             pytest.param(TEST_STOCK_4VEGE4GOURMET20EA_DICT, TEST_DEFAULT_ORDERS_1_DICT, True),
                             pytest.param(TEST_STOCK_4VEGE4GOURMET20EA_DICT, TEST_DEFAULT_ORDERS_3_DICT, False),
                         ])
def test_check_available_stock(stock_dict, orders_dict, expected_value):
    count_stocks = check_available_stock(stock_dict, orders_dict)
    assert count_stocks == expected_value


@pytest.mark.parametrize("allocated_stock,expected_value",
                         [
                             pytest.param(happy_case.HAPPY_CASE, True),
                             pytest.param(duplicated_recipes.DUPLICATED_RECIPE_CASE_1, False),
                             pytest.param(duplicated_recipes.DUPLICATED_RECIPE_CASE_2, False),
                         ])
def test_check_duplicated_recipes(allocated_stock, expected_value):
    unique_recipes_flag = check_duplicated_recipes(allocated_stock)
    assert unique_recipes_flag == expected_value


@pytest.mark.parametrize("allocated_stock,expected_value",
                         [
                             pytest.param(happy_case.HAPPY_CASE, True),
                             pytest.param(vegetarian_orders_receiving_gourmet_boxes.VEGE_GOURMET_CASE_1, False),
                             pytest.param(vegetarian_orders_receiving_gourmet_boxes.VEGE_GOURMET_CASE_2, False),
                         ])
def test_check_no_vegetarian_orders_have_gourmet_boxes(allocated_stock, expected_value):
    correct_allocation_flag = check_no_vegetarian_orders_have_gourmet_boxes(allocated_stock)
    assert correct_allocation_flag == expected_value
