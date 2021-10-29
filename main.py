# -*- coding=utf-8 -*-
import csv
import jieba
import copy

data_location = './外卖评论.csv'
# [
# ...
# {lable: <lable: int>, rivew: <rivew: list>}
# ...
# ]


def ReadCsv(location) -> list:
    this_file = open(location, 'r', encoding='utf-8')
    reader = csv.DictReader(this_file)
    result = []
    for item in reader:
        dict_i = copy.deepcopy(item)
        dict_i["review"] = jieba.lcut(item["review"])
        result.append(dict_i)
    return result


def main():
    data = ReadCsv(data_location)
    # print(data)
    pass


if __name__ == '__main__':
    main()
