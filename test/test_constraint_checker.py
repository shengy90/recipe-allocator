from definitions.test_files_allocated_stock import (
    happy_case
    )

from src.constraints_checker import *

import pytest


@pytest.mark.parametrize("allocated_stocks,expected_value",
                         [
                             pytest.param(happy_case.HAPPY_CASE["vegetarian"], 54),
                             pytest.param(happy_case.HAPPY_CASE["gourmet"], 54),
                         ])
def test_tally_stocks(allocated_stocks,expected_value):
    count_stocks = tally_stocks(allocated_stocks)
    assert count_stocks == expected_value
