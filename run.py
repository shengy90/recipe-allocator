from definitions.test_jsons import (
    TEST_DEFAULT_ORDERS_1_DICT,
    TEST_STOCK_4VEGE4GOURMET20EA_DICT,
    )

from definitions.definitions import (
    constraints_priority
    )

from src.recipe_allocator import (
    allocate_recipes
    )

from src.constraints_checker import (
    tally_total_allocated_stocks
    )


if __name__ == "__main__":
    stock = TEST_STOCK_4VEGE4GOURMET20EA_DICT
    orders = TEST_DEFAULT_ORDERS_1_DICT
    allocated_orders = allocate_recipes(stock, orders, constraints_priority)
    # print("\n")
    print(allocated_orders)
    tally_total_allocated_stocks(orders, allocated_orders)