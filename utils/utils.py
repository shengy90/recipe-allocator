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
