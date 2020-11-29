from utils.utils import (
    extract_number_from_string,
    assert_box_type,
    get_prioritised_list
    )

from num2word import word


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


def get_recipe_with_highest_stock_given_constraint(stock_dict: dict, constraint: str) -> str:
    """
    Function to get the name of the recipe with the highest stock count
    :param stock_dict: input dictionary of stock
    :param constraint: box type
    :return: name of the recipe with the highest stock count
    """
    output_recipe_name = None
    output_recipe_stock = 0

    # Looping through each element of the stock dictionary
    for recipe in stock_dict.keys():
        # Get the stock level of the current recipe
        recipe_stock = stock_dict[recipe]['stock_count']
        # If the stock level of the current recipe is higher than previously read value(s), overwrite the recipe name
        if recipe_stock > output_recipe_stock and stock_dict[recipe]['box_type'] == constraint:
            output_recipe_name = recipe
            output_recipe_stock = recipe_stock # overwrite output_recipe_stock with new highest value
    return output_recipe_name, output_recipe_stock


def compile_order_allocation_list(orders_dict: dict) -> list:
    """
    Function to compile allocation list in prioritised order (first by constraints,
    then by number of recipes, then by number of portions" in which orders would be fulfilled.
    :param orders_dict: input order dictionary
    :param constraint_priority: input dictionary of constraints ordered by priority
    :return: ordered list by which orders would be fulfilled.
    """
    recipe_list = []
    portion_list = []
    output_list = []
    box_types = set(orders_dict.keys())

    for box_type in box_types:
        recipe_list.extend(list(orders_dict[box_type].keys()))
    recipe_types = get_prioritised_list(list(set(recipe_list)), "recipes")

    for recipe_type in recipe_types:
        portion_list.extend(list(orders_dict[box_type][recipe_type].keys()))
    portion_types = get_prioritised_list(list(set(portion_list)), "portions")

    # Prioritising order list
    for box_type in box_types:
        for portion_type in portion_types:
            for recipe_type in recipe_types:
                output_list.append(f"{box_type}:{recipe_type}:{portion_type}")

    return output_list


def update_stock_levels(stock_dict: dict, recipe: str, allocated_stock: int) -> dict:
    """
    Function to update stock inventory levels after each iteration of allocation. Note - function only allows
    for stock levels to be updated if current stock level >= allocated stock. For allocation of multiple recipes
    to a given 'order type' (e.g. vegetarian four_recipes four_portions), the logic needs to be handled outside
    of this function.

    :param stock_dict: input stock inventory levels
    :param recipe: recipe for which stock is being allocated
    :param allocated_stock: amount of stock that was allocated
    :return: output stock inventory levels
    """
    assert stock_dict[recipe]['stock_count'] >= allocated_stock
    stock_dict[recipe]['stock_count'] -= allocated_stock
    return stock_dict


def allocate_recipes(stock_dict: dict, orders_dict: dict, constraints_priority: dict) -> bool:
    """
    Function to allocate recipes, checking all constraints are met
    :param stock_dict: input dictionary of stocks
    :param orders_dict: input dictionary of orders
    :param constraints_priority: input dictionary of constraint priorities
    :return: True if all constraints are met, False if not all constraints are met
    """
    stock_allocation_dict = orders_dict.copy()
    testout = compile_order_allocation_list(orders_dict, constraints_priority)
    print(testout)
    return stock_allocation_dict



