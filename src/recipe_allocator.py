

def load_json(json_file):
    """
    Function to load JSON file and returns output dict
    :param json:
    :return:
    """
    output_dict = json.loads(json_file)
    print(output_dict)
    return output_dict