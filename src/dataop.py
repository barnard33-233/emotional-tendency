# -*- coding = UTF-8 -*-
# import globalv
import csv
import jieba
import paddle

black_list = []


def ReadCsv(file_name):
    try:
        file = open(file_name, 'r', encoding="utf-8")
        result = csv.DictReader(file)
        result_l = []
        for item in result:
            result_l.append(item)
    except IOError:
        print("ERROR: faile to open file %s" % (file_name))
        return []
    else:
        print("File %s is opened successfully ......" % (file_name))
        return result_l


def WriteCsv(data: list, field_names: list, path: str):
    with open(path, "w", encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_writer.writeheader()
        for item in data:
            csv_writer.writerow({x: item[field_names.index(x)] for x in field_names})
    print("finish writing %s" % (path))
    return None


def SplitSentences(file: list):
    paddle.enable_static()
    jieba.enable_paddle()
    for item in file:
        item["review"] = jieba.lcut(item["review"], use_paddle=True)
    return file

# data structure
# [
# ...
# {lable: <lable: int>, rivew: <rivew: list>}
# ...
# ]
