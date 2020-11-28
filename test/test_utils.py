from definitions.test_jsons import TEST_STOCK_DICT

from utils.utils import *

import pytest


@pytest.mark.parametrize("string,delimiter,expected_value",
                         [
                             pytest.param("four", "", 4),
                             pytest.param("four", None, 4),
                             pytest.param("eight_", "_", 8),
                             pytest.param("ten_recipes", "_", 10),
                             pytest.param("tenrecipes", None, 10, marks=pytest.mark.xfail(raises=ValueError)),
                             pytest.param("six_", None, 4, marks=pytest.mark.xfail(raises=ValueError)),
                         ])
def test_extract_number_from_string(string, delimiter, expected_value):
    assert extract_number_from_string(string, delimiter) == expected_value


@pytest.mark.parametrize("stock_dict,expected_value",
                         [
                             pytest.param(
                                 {"recipe_3": {"stock_count": 10, "box_type": "vegetarian"},
                                  "recipe_5": {"stock_count": 20, "box_type": "vegetarian"},
                                  "recipe_7": {"stock_count": 30, "box_type": "vegetarian"}},
                                 "recipe_7"),
                             pytest.param(
                                 {"recipe_19": {"stock_count": 50, "box_type": "vegetarian"},
                                  "recipe_03": {"stock_count": 20, "box_type": "vegetarian"},
                                  "recipe_46": {"stock_count": 10, "box_type": "vegetarian"}},
                                 "recipe_19"),
                             pytest.param(TEST_STOCK_DICT, "recipe_6"),
                         ])
def test_get_recipe_with_highest_stock(stock_dict, expected_value):
    assert get_recipe_with_highest_stock(stock_dict) == expected_value

