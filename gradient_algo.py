#!/usr/local/bin/python3.6

import csv
import sys

from draw_data import draw_dataset

GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'



def find_partial_derivate(w1, w0, data, size):
    new_w0, new_w1 = 0, 0
    for k, v in data.items():
        # print(str(new_w0) + " " + str(new_w1))
        new_w0 += (w1 * v + w0) - k
        new_w1 += (w1 * v + w0 - k) * v
    return new_w0 / size, new_w1 / size



def training_set(res, learning_rate):
    previous_w0, previous_w1 = 0, 0
    size = len(res)
    for i in range(0, 3000):
        minimize0, minimize1 = find_partial_derivate(previous_w1, previous_w0, res, size)
        new_w0 = previous_w0 - learning_rate * minimize0
        new_w1 = previous_w1 - learning_rate * minimize1
        previous_w0, previous_w1 = new_w0, new_w1
    return new_w0, new_w1

def get_data_from_csv(name):
    val = {}
    try:
        with open(name) as csvfile:
            file = csv.DictReader(csvfile, delimiter=',')
            for row in file:
                val[(int(row['km']))] = int(row['price']) # dict of data
            print(val)
            return val
    except Exception as e:
        print(f"{BRED}Error while reading file: {ENDC} {str(e)}")


def scale_and_rescale(res, data, flag):
    new_res = {}
    if flag:
        for k, v in res.items():
            new_res[(k - data['min_y']) / data['delta_y']] = (v - data['min_x']) /data['delta_x']
    else:
        for k, v in res.items():
            new_res[k*data['delta_y'] + data['min_y']] = v * data['delta_x'] + data['min_x']
    print(new_res)
    return new_res


def get_data(data_dict):
    data = {}
    data['max_x'] = max(data_dict.values())
    data['min_x'] = min(data_dict.values())
    data['delta_x'] = data['max_x'] - data['min_x']
    data['max_y'] = max(data_dict.keys())
    data['min_y'] = min(data_dict.keys())
    data['delta_y'] = data['max_y'] - data['min_y']
    return data


if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = get_data_from_csv(sys.argv[1])
        data = get_data(res)
        res = scale_and_rescale(res, data, 1)
        w0, w1 = training_set(res, 0.1)
        print("After:")
        res = scale_and_rescale(res, data, 0)
        print(w0, w1)
        draw_dataset(res, data, w0, w1)
    else:
        print(f'{BRED}Usage ./gradient_algo.py filename.csv {ENDC}')

