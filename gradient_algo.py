import csv
import sys

GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'



def get_data_from_csv():
    val = {}
    try:
        with open("data.csv") as csvfile:
            file = csv.DictReader(csvfile, delimiter=',')
            for row in file:
                val[int(row['km'])] = int(row['price']) # dict of data
            print(val)
            return val
    except Exception as e:
        print(f"{BRED}Error while reading file: {ENDC} {str(e)}")



if __name__ == '__main__':
    if sys.argv == 2:
        res = get_data_from_csv(sys.argv[2])
    else:
        print(f'{BRED}Usage ./gradient_algo.py filename.csv {ENDC}')

