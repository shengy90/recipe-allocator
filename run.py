from definitions.test_jsons import (
    TEST_DEFAULT_ORDERS_1_DICT,
    TEST_STOCK_4VEGE4GOURMET20EA_DICT,
    )

from definitions.definitions import (
    constraints_priority
    )

from src.recipe_allocator import (
    allocate_recipes,
    )

from src.constraints_checker import (
    tally_total_allocated_stocks,
    check_available_stock,
    check_duplicated_recipes,
    check_no_vegetarian_orders_have_gourmet_boxes,
    )


if __name__ == "__main__":
    stock = TEST_STOCK_4VEGE4GOURMET20EA_DICT
    orders = TEST_DEFAULT_ORDERS_1_DICT

    # check that we have the minimum number of required stock before proceeding..
    assert check_available_stock(stock, orders)
    # allocate stocks
    allocated_orders = allocate_recipes(stock, orders, constraints_priority)

    # check constraint 1: total allocated stock == total required stocks (fully allocated)
    constraint_1 = tally_total_allocated_stocks(orders, allocated_orders)
    # check constraint 2: no duplicated recipes
    constraint_2 = check_duplicated_recipes(allocated_orders)
    # check constraint 3: all vegetarian orders are allocated vegetarian boxes
    constraint_3 = check_no_vegetarian_orders_have_gourmet_boxes(allocated_orders)

    all_constraints_met = constraint_1 is True and constraint_2 is True and constraint_3 is True
    print(f"All constraints met: {all_constraints_met}")
