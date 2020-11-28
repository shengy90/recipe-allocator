from utils.utils import (
    extract_number_from_string
    )


def assert_box_type(box_type: str) -> bool:
    """
    Check that box_type must be either 'vegetarian' or 'gourmet'
    :param box_type: box type
    :return: True if box_type is either 'vegetarian' or 'gourmet', else False
    """
    return True if box_type in ['vegetarian', 'gourmet'] else False


def count_orders_and_boxes(input_dict: dict, box_type: str) -> int:
    """
    Count the total number of default orders for a given order type
    :param input_dict: input dictionary of orders
    :param box_type: box type - must either be 'vegetarian' or 'gourmet'
    :return: total count of orders, total count of boxes
    """

    assert assert_box_type(box_type)

    recipes = list(input_dict[box_type])
    total_orders_count = 0
    total_boxes_count = 0
    for recipe in recipes:
        recipe_number = extract_number_from_string(recipe, "_")
        portions = list(input_dict[box_type][recipe])
        for portion in portions:
            portion_number = extract_number_from_string(portion, "_")
            total_orders_count += input_dict[box_type][recipe][portion]
            total_boxes_count += input_dict[box_type][recipe][portion] * recipe_number * portion_number

    return total_orders_count, total_boxes_count


def count_stock(input_dict: dict, box_type: str) -> int:
    """
    Count the total number of stocks held in inventory
    :param input_dict: input dictionary of stocks
    :param box_type: box type - must either be 'vegetarian' or 'gourmet'
    :return: total count of stocks
    """

    assert assert_box_type(box_type)

    recipes = list(input_dict.keys())
    total_count = 0
    for recipe in recipes:
        if input_dict[recipe]['box_type'] == box_type:
            total_count += input_dict[recipe]['stock_count']

    return total_count


def allocate_recipes(stock_dict: dict, orders_dict: dict, constraint_priority: dict) -> bool:
    """
    Function to allocate recipes, checking all constraints are met
    :param stock_dict: input dictionary of stocks
    :param orders_dict: input dictionary of orders
    :param constraint_priority: input dictionary of constraint priorities
    :return: True if all constraints are met, False if not all constraints are met
    """
    for constraint_order in constraint_priority:
        constraint = constraint_priority[constraint_order]
        assert assert_box_type(constraint)  # check that constraint is a valid box type

        if constraint == "vegetarian":
            box_type = orders_dict[constraint]



