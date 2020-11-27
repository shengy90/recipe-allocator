from pathlib import Path

import os
import json


current_file = os.path.realpath(__file__)
parent_dir = str(Path(current_file).parent.parent)
test_default_order_json_path = os.path.join(parent_dir, 'bin', 'test_default_orders.json')
test_stock_json_path = os.path.join(parent_dir, 'bin', 'test_stock.json')

with open(test_default_order_json_path) as json_file:
    TEST_DEFAULT_ORDERS_DICT = json.load(json_file)

with open(test_stock_json_path) as json_file:
    TEST_STOCK_DICT = json.load(json_file)
