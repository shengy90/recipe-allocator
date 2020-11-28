from word2number import w2n


def extract_number_from_string(string: str, delimiter: str = None) -> int:
    """
    Function to extract the first 'number word' from a string
    :param string: a word2number package 'number word'
    :param delimiter: delimiter, defaults to None
    :return: integer
    """
    number_word = string if delimiter is None or delimiter == "" else string.split(delimiter)[0]
    return w2n.word_to_num(number_word)


def get_recipe_with_highest_stock(stock_dict: dict) -> str:
    """
    Function to get the name of the recipe with the highest stock count
    :param stock_dict: input dictionary of stock
    :return: name of the recipe with the highest stock count
    """
    output_recipe_name = None
    output_recipe_stock = 0

    # Looping through each element of the stock dictionary
    for recipe in stock_dict.keys():
        # Get the stock level of the current recipe
        recipe_stock = stock_dict[recipe]['stock_count']
        # If the stock level of the current recipe is higher than previously read value(s), overwrite the recipe name
        if recipe_stock > output_recipe_stock:
            output_recipe_name = recipe
            output_recipe_stock = recipe_stock # overwrite output_recipe_stock with new highest value

    return output_recipe_name
