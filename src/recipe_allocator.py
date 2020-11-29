from utils.utils import (
    extract_number_from_string,
    assert_box_type,
    get_prioritised_list
    )

import math


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


def get_recipe_with_highest_stock_given_constraint(stock_dict: dict, constraint: str = None) -> str:
    """
    Function to get the name of the recipe with the highest stock count
    :param stock_dict: input dictionary of stock
    :param constraint: box type
    :return: name of the recipe with the highest stock count
    """
    output_recipe_name = None
    output_recipe_boxtype = None
    output_recipe_stock = 0

    # Looping through each element of the stock dictionary
    for recipe in stock_dict.keys():
        # Get the stock level of the current recipe
        recipe_stock = stock_dict[recipe]['stock_count']
        recipe_boxtype = stock_dict[recipe]['box_type']

        # If the stock level of the current recipe is higher than previously read value(s), overwrite the recipe name

        # If no constraint is applied, select any recipe that meets criteria
        if constraint is None:
            if recipe_stock > output_recipe_stock:
                output_recipe_name = recipe
                output_recipe_stock = recipe_stock
                output_recipe_boxtype = recipe_boxtype
        # Otherwise if a constraint was specified, only select recipes that satisfies the constraint
        else:
            if recipe_stock > output_recipe_stock and stock_dict[recipe]['box_type'] == constraint:
                output_recipe_name = recipe
                output_recipe_stock = recipe_stock  # overwrite output_recipe_stock with new highest value
                output_recipe_boxtype = recipe_boxtype
    return output_recipe_name, output_recipe_stock, output_recipe_boxtype


def compile_order_allocation_list(orders_dict: dict, constraints_priority: dict) -> list:
    """
    Function to compile allocation list in prioritised order (first by constraints,
    then by number of recipes, then by number of portions" in which orders would be fulfilled.
    :param orders_dict: input order dictionary
    :param constraints_priority: input dictionary of constraints ordered by priority
    :return: ordered list by which orders would be fulfilled.
    """
    recipe_list = []
    portion_list = []
    output_list = []
    box_types = []

    for constraint in constraints_priority:
        box_type = constraints_priority[constraint]
        box_types.append(box_type)
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
    available_stock = stock_dict[recipe]['stock_count']
    stock_dict[recipe]['stock_count'] -= allocated_stock
    assert available_stock >= allocated_stock
    return stock_dict


def calculate_stock_requirements(orders_dict: dict, box_type: str, recipe_type: str, portion_type: str) -> int:
    """
    Function to calculate the required stock amount for a given order type by multiplying number of orders for the
    order type by the number of portions
    :param orders_dict: input dictionary of orders
    :param box_type: box type (vegetarian or gourmet)
    :param recipe_type: number of recipe
    :param portion_type: number of portions
    :return:
    """
    number_of_orders = orders_dict[box_type][recipe_type][portion_type]
    number_of_portions = extract_number_from_string(portion_type, "_")
    stock_required = number_of_orders * number_of_portions
    return stock_required, number_of_orders, number_of_portions


def allocate_recipes(stock_dict: dict, orders_dict: dict, constraints_priority: dict) -> bool:
    """
    Function to allocate recipes, checking all constraints are met
    :param stock_dict: input dictionary of stocks
    :param orders_dict: input dictionary of orders
    :param constraints_priority: input dictionary of constraint priorities
    :return: True if all constraints are met, False if not all constraints are met
    """
    stock_allocation_dict = orders_dict.copy()
    order_allocation_list = compile_order_allocation_list(orders_dict, constraints_priority)

    for order_type in order_allocation_list:

        # Get order metadata
        key_list = order_type.split(":")
        box_type = key_list[0]
        recipe_type = key_list[1]
        portion_type = key_list[2]
        number_of_recipes_needed = extract_number_from_string(recipe_type, "_")

        # Calculate stock requirements
        stock_required, number_of_orders, number_of_portions = calculate_stock_requirements(orders_dict, box_type, recipe_type, portion_type)
        outstanding_orders = number_of_orders
        stock_allocation_dict[box_type][recipe_type][portion_type] = {}

        for i in range(number_of_recipes_needed):

            # Set constraints for vegetarian box type
            constraint = "vegetarian" if box_type == "vegetarian" else None

            # Counter for number of recipes allocated per order
            count_allocated_recipe = 1
            count_loops = 0

            # While loop to keep allocating stock to orders until:
            # all orders per order type is fulfilled (outstanding orders == 0) or
            # we have ran out of stock in which case the while loop will break
            # manually break the program and raise error if > 1000 loops - we should never ever see this error!

            while outstanding_orders > 0:
                
                # Select available recipes
                selected_recipe, selected_recipe_stock, selected_recipe_boxtype = get_recipe_with_highest_stock_given_constraint(stock_dict, constraint)

                if selected_recipe is not None:
                    # Allocating stock
                    number_of_fulfilled_orders = min(math.floor(selected_recipe_stock / number_of_portions), outstanding_orders)
                    allocated_stock = number_of_fulfilled_orders * number_of_portions
                    outstanding_orders = max(outstanding_orders - number_of_fulfilled_orders, 0)
                    # Updating stock inventory
                    stock_dict = update_stock_levels(stock_dict, selected_recipe, allocated_stock)

                elif count_loops > 1000:
                    # Print unexpected behaviour - we shouldn't encounter
                    raise ValueError(f"Warning : More than 1000 loops encounted....")

                else:
                    print(f"Warning... Ran out of stock for order type {box_type} {recipe_type} {portion_type}!")
                    break

                # Save allocation
                stock_allocation_dict[box_type][recipe_type][portion_type][f'selected_recipes_{count_allocated_recipe}'] = {}
                stock_allocation_dict[box_type][recipe_type][portion_type][f'selected_recipes_{count_allocated_recipe}']['recipe_name'] = selected_recipe
                stock_allocation_dict[box_type][recipe_type][portion_type][f'selected_recipes_{count_allocated_recipe}']['allocated_stock'] = allocated_stock
                stock_allocation_dict[box_type][recipe_type][portion_type][f'selected_recipes_{count_allocated_recipe}']['recipe_box_type'] = selected_recipe_boxtype
                count_allocated_recipe += 1
                count_loops += 1

    return stock_allocation_dict





