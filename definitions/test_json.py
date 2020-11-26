from pathlib import Path

import os
import json

# Get test dataframe
dir = os.getcwd()
current_dir = Path(dir)
parent_dir = str(current_dir.parent)

TEST_STOCK_JSON = json.loads(os.path.join(parent_dir, 'test', 'json', 'test_stock.json'))
TEST_DEFAULT_ORDER_JSON = json.loads(os.path.join(parent_dir, 'test', 'json', 'test_default_order,json'))

