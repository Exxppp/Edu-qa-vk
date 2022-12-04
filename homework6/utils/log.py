import os
import re
from collections import Counter
from urllib.parse import urlparse

rep = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
log = os.path.join(rep, 'access.log')


def count_lines():
    with open(log, 'r') as file:
        _sum = sum(1 for line in file)

    return [{'count': _sum}]


def count_request():
    my_dict = Counter()
    with open(log, 'r') as file:
        pattern = r'"[A-Z]{3,12}\s'
        for line in file.readlines():
            find = re.search(pattern, line)
            if find:
                my_dict.update({find[0][1:-1]: 1})
    my_dict = dict(my_dict)
    return [{'type': name, 'count': count} for name, count in my_dict.items()]


def most_frequent_requests(top=10):
    my_dict = Counter()
    with open(log, 'r') as file:
        for line in file.readlines():
            path = urlparse(line.split(' ')[6]).path
            my_dict.update({path: 1})

    my_dict = my_dict.most_common(top)
    return [{'url': url, 'count': count} for url, count in my_dict]


def largest_requests_in_size_with_4xx_error(top=5):
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
    my_list = my_list[:top]

    return [{'url': url, 'status_code': status_code, 'byte_size': byte_size, 'ip': ip}
            for url, status_code, byte_size, ip in my_list]


def users_with_5xx_error(top=5):
    my_dict = Counter()
    with open(log, 'r') as file:
        for line in file.readlines():
            ip, status_code = line.split(' ')[0:9:8]
            if status_code.startswith('5'):
                my_dict.update({ip: 1})
    my_dict = my_dict.most_common(top)

    return [{'ip': ip, 'count': count} for ip, count in my_dict]
