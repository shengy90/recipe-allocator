from pathlib import Path

import os
import json


current_file = os.path.realpath(__file__)
parent_dir = str(Path(current_file).parent.parent)

# test orders
test_default_order_json_path = os.path.join(parent_dir, 'bin', 'test_files', 'test_default_orders.json')
test_default_order_1_json_path = os.path.join(parent_dir, 'bin', 'test_files', 'test_default_orders_1.json')

# test stocks
test_stock_json_path = os.path.join(parent_dir, 'bin', 'test_files', 'test_stock.json')

with open(test_default_order_json_path) as json_file:
    TEST_DEFAULT_ORDERS_DICT = json.load(json_file)

with open(test_default_order_1_json_path) as json_file:
    TEST_DEFAULT_ORDERS_1_DICT = json.load(json_file)

with open(test_stock_json_path) as json_file:
    TEST_STOCK_DICT = json.load(json_file)
