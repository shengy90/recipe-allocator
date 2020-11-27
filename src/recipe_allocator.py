def assert_box_type(box_type: str) -> bool:
    """
    Check that box_type must be either 'vegetarian' or 'gourmet'
    :param box_type: box type
    :return: True if box_type is either 'vegetarian' or 'gourmet', else False
    """
    return True if box_type in ['vegetarian', 'gourmet'] else False


def count_orders(input_dict: dict, box_type: str) -> int:
    """
    Count the total number of default orders for a given order type
    :param input_dict: input dictionary
    :param box_type: box type - must either be 'vegetarian' or 'gourmet'
    :return: total count
    """

    assert assert_box_type(box_type)

    recipes = list(input_dict[box_type])
    total_count = 0
    for recipe in recipes:
        portions = list(input_dict[box_type][recipe])
        for portion in portions:
            total_count += input_dict[box_type][recipe][portion]

    return total_count


def count_stock(input_dict: dict, box_type: str) -> int:
    """
    :param input_dict: input dictionary
    :param box_type: box type - must either be 'vegetarian' or 'gourmet'
    :return: total count
    """

    assert assert_box_type(box_type)

    recipes = list(input_dict.keys())
    total_count = 0
    for recipe in recipes:
        if input_dict[recipe]['box_type'] == box_type:
            total_count += input_dict[recipe]['stock_count']

    return total_count

