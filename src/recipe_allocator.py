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


def allocate_recipes(stock_dict: dict, orders_dict: dict, constraint_priority: dict) -> bool:
    """
    Function to allocate recipes, checking all constraints are met
    :param stock_dict: input dictionary of stocks
    :param orders_dict: input dictionary of orders
    :param constraint_priority: input dictionary of constraint priorities
    :return: True if all constraints are met, False if not all constraints are met
    """
    stock_allocation_dict = orders_dict.copy()

    for priority in constraint_priority:
        constraint = constraint_priority[priority]
        number_of_recipes = list(orders_dict[constraint].keys())
        prioritised_recipe_list = get_prioritised_list(number_of_recipes, "recipes")

        for recipe in prioritised_recipe_list:
            number_of_portions = list(orders_dict[constraint][recipe])
            prioritised_portion_list = get_prioritised_list(number_of_portions, "portions")

            for portion in prioritised_portion_list:

                print(f"Allocating: {constraint} {recipe} {portion}")
                number_of_orders = orders_dict[constraint][recipe][portion]
                stock_required = number_of_orders * extract_number_from_string(portion, "_")

                shortlisted_recipe, \
                shortlisted_recipe_stock = get_recipe_with_highest_stock_given_constraint(
                    stock_dict,
                    constraint)
                print(number_of_orders, stock_required, shortlisted_recipe, shortlisted_recipe_stock)
    return stock_allocation_dict



