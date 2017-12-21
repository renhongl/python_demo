"""IO study"""

import json

def run():
    """run function"""
    with open('./input/data.txt', 'r') as txt_data:
        temp = {}
        for line in txt_data.readlines():
            line = line.strip()
            line = line.split(' ')
            temp[line[0]] = line[1]

        print('After format: ' + json.dumps(temp))

        with open('./output/data.json', 'w') as json_data:
            json.dump(temp, json_data)


if __name__ == '__main__':
    run()
