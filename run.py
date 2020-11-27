from definitions.test_jsons import(
    TEST_DEFAULT_ORDERS_DICT,
    TEST_STOCK_DICT,
    )

from src.recipe_allocator import (
    count_orders,
    count_stock,
    )


if __name__ == "__main__":
    stock = TEST_STOCK_DICT
    default_orders = TEST_DEFAULT_ORDERS_DICT
    vege_count = count_orders(default_orders, box_type="vegetarian")
    gourmet_count = count_orders(default_orders, box_type="gourmet")

    vege_stock_count = count_stock(stock, box_type="vegetarian")
    gourmet_stock_count = count_stock(stock, box_type="gourmet")

    print(vege_count, gourmet_count)
    print(vege_stock_count, gourmet_stock_count)
