from definitions.definitions import (
    constraints_priority
    )

from src.recipe_allocator import (
    allocate_recipes,
    )

from src.constraints_checker import (
    tally_total_allocated_stocks,
    check_available_stock,
    check_duplicated_recipes,
    check_no_vegetarian_orders_have_gourmet_boxes,
    )

from pathlib import Path

import sys
import os
import json
import argparse


def parse_args(argument):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--orders', nargs=1, required=True,
                        help="Name of orders input file without the .json extension")

    parser.add_argument('--stocks', nargs=1, required=True,
                        help="Name of stocks input file without the .json extension")

    return parser.parse_args(argument)


if __name__ == "__main__":

    args = parse_args(sys.argv[1:])
    current_file = os.path.realpath(__file__)
    current_dir = str(Path(current_file).parent)
    output_file_name = f"{args.orders[0]}_{args.stocks[0]}.json"
    orders_file_path = os.path.join(current_dir, 'bin', 'inputs', f'{args.orders[0]}.json')
    stocks_file_path = os.path.join(current_dir, 'bin', 'inputs', f'{args.stocks[0]}.json')
    output_file_path = os.path.join(current_dir, 'bin', 'outputs', output_file_name)

    with open(orders_file_path) as json_file:
        orders = json.load(json_file)

    with open(stocks_file_path) as json_file:
        stocks = json.load(json_file)

    # check that we have the minimum number of required stock before proceeding..
    assert check_available_stock(stocks, orders)

    # allocate stocks
    allocated_orders = allocate_recipes(stocks, orders, constraints_priority)

    # check constraint 1: total allocated stock == total required stocks (fully allocated)
    constraint_1 = tally_total_allocated_stocks(orders, allocated_orders)
    # check constraint 2: no duplicated recipes
    constraint_2 = check_duplicated_recipes(allocated_orders)
    # check constraint 3: all vegetarian orders are allocated vegetarian boxes
    constraint_3 = check_no_vegetarian_orders_have_gourmet_boxes(allocated_orders)

    with open(output_file_path, 'w') as json_file:
        json_string = json.dumps(allocated_orders)
        json_file.write(json_string)

    all_constraints_met = constraint_1 is True and constraint_2 is True and constraint_3 is True

    if all_constraints_met is True:
        print(f"All constraints met: {all_constraints_met}")
    else:
        print(f"constraint_1: {constraint_1}, constraint_2: {constraint_2}, constraint_3: {constraint_3}")

