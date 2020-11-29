from definitions.test_files_allocated_stock import (
    happy_case
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
