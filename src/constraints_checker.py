from src.recipe_allocator import (
    count_orders_and_boxes,
    count_stock
    )


def tally_stocks(input_dict:dict) -> int:
    count_stocks = 0
    for lvl1_key in list(input_dict.keys()):
        for lvl2_key in list(input_dict[lvl1_key].keys()):
            for lvl3_key in list(input_dict[lvl1_key][lvl2_key].keys()):
                for lvl4_key in list(input_dict[lvl1_key][lvl2_key][lvl3_key].keys()):
                    count_stocks += input_dict[lvl1_key][lvl2_key][lvl3_key][lvl4_key]['allocated_stock']
    return count_stocks


def tally_total_allocated_stocks(orders_dict: dict, allocated_stocks: dict) -> bool:
    """
    Function to reconcile the total number of allocated boxes against the total number of required boxes
    :param orders_dict: input dictionary of orders
    :param allocated_stocks: dictionary of allocated stocks
    :return:
    """
    # Count total stocks required
    vegetarian_orders, vegetarian_boxes = count_orders_and_boxes(orders_dict, "vegetarian")
    gourmet_orders, gourmet_boxes = count_orders_and_boxes(orders_dict, "gourmet")

    # Count total allocated stocks
    allocated_vegetarian_orders = allocated_stocks["vegetarian"]
    allocated_gourmet_orders = allocated_stocks["gourmet"]

    count_vegetarian_stock = tally_stocks(allocated_vegetarian_orders)
    count_gourmet_stock = tally_stocks(allocated_gourmet_orders)

    return True if count_vegetarian_stock == vegetarian_boxes and count_gourmet_stock == gourmet_boxes else False


def check_available_stock(stock_dict: dict, orders_dict: dict)-> bool:
    """
    Function to check that we have at least the required amount of boxes to go around!
    Vegetarian orders can only take vegetarian boxes, whislt gourmet orders can take both vegetarian and gourmet boxes
    :param stock_dict: input stock dictionary
    :param orders_dict: input orders dictionary
    :return:
    """
    vegetarian_orders, vegetarian_boxes = count_orders_and_boxes(orders_dict, "vegetarian")
    gourmet_orders, gourmet_boxes = count_orders_and_boxes(orders_dict, "gourmet")

    vegetarian_stock = count_stock(stock_dict, "vegetarian")
    gourmet_stock = count_stock(stock_dict, "gourmet")

    remaining_vegetarian_stock = max(vegetarian_stock - vegetarian_boxes, 0)
    gourmet_available_stock = gourmet_stock + remaining_vegetarian_stock

    return True if vegetarian_stock >= vegetarian_boxes and gourmet_available_stock >= gourmet_boxes