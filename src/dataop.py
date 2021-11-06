# -*- coding = UTF-8 -*-
# import globalv
import csv
import re
import jieba
import paddle


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
        tmp_review = re.split(r'(\W+)', item['review'])
        item["review"] = []
        for s in tmp_review:
            s = jieba.lcut(s)
            item["review"] += s
    return file

# data structure
# [
# ...
# {lable: <lable: int>, rivew: <rivew: list>}
# ...
# ]


def SplitNSort(words: dict) -> list:
    posws = {x: words[x] for x in words if words[x] > 0.0}
    negws = {x: words[x] for x in words if words[x] < 0.0}
    posw = sorted(posws.items(), key=lambda key: key[1], reverse=True)
    negw = sorted(negws.items(), key=lambda key: key[1], reverse=False)
    result = [posw, negw]
    return result
