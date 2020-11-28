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
