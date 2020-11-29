from definitions.test_jsons import (
    TEST_DEFAULT_ORDERS_1_DICT,
    TEST_STOCK_4VEGE4GOURMET20EA_DICT,
    )

from definitions.definitions import (
    constraints_priority
    )

from src.recipe_allocator import (
    allocate_recipes,
    count_stock,
    count_orders_and_boxes
    )

from src.constraints_checker import (
    tally_total_allocated_stocks,
    check_available_stock
    )


if __name__ == "__main__":
    stock = TEST_STOCK_4VEGE4GOURMET20EA_DICT
    orders = TEST_DEFAULT_ORDERS_1_DICT

    # check that we have the minimum number of required stock before proceeding..
    assert check_available_stock(stock, orders)
    # allocate stocks
    allocated_orders = allocate_recipes(stock, orders, constraints_priority)
    print(allocated_orders)
    # checking constraints 1: total allocated stock == total required stocks (fully allocated)
    constraint_1 = tally_total_allocated_stocks(orders, allocated_orders)
