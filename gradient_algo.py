#!/usr/local/bin/python3.6

import csv
import sys

GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'


my_w0_error, my_w1_error = lambda data, a, b, size: sum(k - (a * v + b)), sum((k - (a * v + b)) * v) for k, v in data.items()) / size
my_w1_error = lambda data, a, b, size: sum((k - (a * v + b)) * v for k, v in data.items()) / size
new_w0 = lambda previous_w0, learning_rate: previous_w0 - learning_rate * my_w0_error(res, previous_w0, previous_w1, size)

def training_set(res, previous_w0, previous_w1, learning_rate):
    size = len(res)
    new_w0 = previous_w0 - learning_rate * my_w0_error(res, previous_w0, previous_w1, size)
    new_w1 = previous_w1 - learning_rate * my_w1_error(res, previous_w0, previous_w1, size)
    return new_w0, new_w1

def get_data_from_csv(name):
    val = {}
    try:
        with open(name) as csvfile:
            file = csv.DictReader(csvfile, delimiter=',')
            for row in file:
                val[int(row['km'])] = int(row['price']) # dict of data
            print(val)
            return val
    except Exception as e:
        print(f"{BRED}Error while reading file: {ENDC} {str(e)}")



if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = get_data_from_csv(sys.argv[1])

    else:
        print(f'{BRED}Usage ./gradient_algo.py filename.csv {ENDC}')

