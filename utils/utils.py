from word2number import w2n
from num2word import word


def assert_box_type(box_type: str) -> bool:
    """
    Check that box_type must be either 'vegetarian' or 'gourmet'
    :param box_type: box type
    :return: True if box_type is either 'vegetarian' or 'gourmet', else False
    """
    return True if box_type in ['vegetarian', 'gourmet'] else False


def extract_number_from_string(string: str, delimiter: str = None) -> int:
    """
    Function to extract the first 'number word' from a string
    :param string: a word2number package 'number word'
    :param delimiter: delimiter, defaults to None
    :return: integer
    """
    number_word = string if delimiter is None or delimiter == "" else string.split(delimiter)[0]
    return w2n.word_to_num(number_word)


def get_prioritised_list(input_list: list, suffix: str) -> list:
    """
    Function to prioritise input list in descending order
    :param input_list: list, where elements are in the format two_xxxx, four_xxxxx, three_xxxxxx
    :return: ordered list
    """
    intermediate_list = [extract_number_from_string(element, "_") for element in input_list]
    intermediate_list.sort(reverse=True)
    output_list = [f"{word(element).lower()}_{suffix}" for element in intermediate_list]
    return output_list
