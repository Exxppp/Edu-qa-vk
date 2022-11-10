import os
import re
import argparse
import json
from collections import Counter
from urllib.parse import urlparse

rep = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
log = os.path.join(rep, 'access.log')
res_txt = os.path.join(rep, 'result', 'result_python.txt')
one_json = os.path.join(rep, 'result', 'one.json')
two_json = os.path.join(rep, 'result', 'two.json')
three_json = os.path.join(rep, 'result', 'three.json')
four_json = os.path.join(rep, 'result', 'four.json')
five_json = os.path.join(rep, 'result', 'five.json')

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true', default=False)
args = parser.parse_args()


def count_lines():
    with open(log, 'r') as file:
        _sum = sum(1 for line in file)

    if args.json:
        data = {'Total numbers': _sum}
        with open(one_json, 'w') as file:
            json.dump(data, file)
    else:
        with open(res_txt, 'w') as file:
            file.write(f'{str(_sum)}\n')


def count_request():
    my_dict = Counter()
    # count = 0
    with open(log, 'r') as file:
        pattern = r'"[A-Z]{3,12}\s'
        for line in file.readlines():
            # count += 1
            find = re.search(pattern, line)
            if find:
                my_dict.update({find[0][1:-1]: 1})
            # else:
            #     print(f'########################### {find}: {count} ###########################')
    if args.json:
        data = {}
        for request, count in my_dict.items():
            data[request] = count
        with open(two_json, 'w') as file:
            json.dump(data, file)
    else:
        with open(res_txt, 'a') as file:
            file.write('\n')
            for request, count in my_dict.items():
                file.write(f'{request:<4} - {count}\n')


def most_frequent_requests():
    my_dict = Counter()
    with open(log, 'r') as file:
        for line in file.readlines():
            path = urlparse(line.split(' ')[6]).path
            my_dict.update({path: 1})

    if args.json:
        data = {}
        for path, count in my_dict.most_common(10):
            data[path] = count
        with open(three_json, 'w') as file:
            json.dump(data, file)
    else:
        with open(res_txt, 'a') as file:
            file.write('\n')
            for path, count in my_dict.most_common(10):
                file.write(f'{path}\n')
                file.write(f'{count}\n')


def five_largest_requests_in_size_with_4xx_error():
    my_list = list()
    with open(log, 'r') as file:
        for line in file.readlines():
            line_list = line.split(' ')
            ip = line_list[0]
            path = line_list[6]
            status_code = line_list[8]
            byte_size = line_list[9]
            if status_code.startswith('4'):
                my_list.append([path, status_code, int(byte_size), ip])
        my_list.sort(key=lambda el: el[2], reverse=True)

    if args.json:
        data = {}
        number = 0
        for path, status_code, byte_size, ip in my_list[:5]:
            number += 1
            data[str(number)] = {}
            data[str(number)]['path'] = path
            data[str(number)]['status_code'] = status_code
            data[str(number)]['byte_size'] = byte_size
            data[str(number)]['ip'] = ip
        with open(four_json, 'w') as file:
            json.dump(data, file)
    else:
        with open(res_txt, 'a') as file:
            file.write('\n')
            for path, status_code, byte_size, ip in my_list[:5]:
                file.write(f'{path}\n{status_code}\n{byte_size}\n{ip}\n')


def top_five_users_with_5xx_error():
    my_dict = Counter()
    with open(log, 'r') as file:
        for line in file.readlines():
            ip, status_code = line.split(' ')[0:9:8]
            if status_code.startswith('5'):
                my_dict.update({ip: 1})

    if args.json:
        data = {}
        number = 0
        for ip, count in my_dict.most_common(5):
            number += 1
            data[str(number)] = {}
            data[str(number)]['ip'] = ip
            data[str(number)]['count'] = count
        with open(five_json, 'w') as file:
            json.dump(data, file)
    else:
        with open(res_txt, 'a') as file:
            file.write('\n')
            for ip, count in my_dict.most_common(5):
                file.write(f'{ip}\n{count}\n')


count_lines()
count_request()
most_frequent_requests()
five_largest_requests_in_size_with_4xx_error()
top_five_users_with_5xx_error()
