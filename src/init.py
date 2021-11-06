# -*- coding=utf-8 -*-
import os
import globalv
import csv


def initialize():
    set_path()
    read_seeds()


def set_path():
    present_path = os.listdir(".")
    if 'data' in present_path:
        globalv.data_location = '.\\data\\comments.csv'
        globalv.seeds_location = '.\\data\\seeds.csv'
        globalv.pos_location = '.\\data\\result_pos{}.csv'.format(globalv.version)
        globalv.neg_location = '.\\data\\result_neg{}.csv'.format(globalv.version)
        globalv.frequency_location = '.\\data\\frequency.csv'
        globalv.result_location = '.\\data\\result{}.csv'.format(globalv.version)
    else:
        globalv.seeds_location = '..\\data\\seeds.csv'
        globalv.data_location = '..\\data\\comments.csv'
        globalv.pos_location = '..\\data\\result_pos{}.csv'.format(globalv.version)
        globalv.neg_location = '..\\data\\result_neg{}.csv'.format(globalv.version)
        globalv.frequency_location = '..\\data\\frequency.csv'
        globalv.result_location = '..\\data\\result{}.csv'.format(globalv.version)
    return None


def read_seeds():
    try:
        seedsfile = open(globalv.seeds_location, 'r', encoding='utf-8')
        CsvReader = csv.reader(seedsfile)
        for row in CsvReader:
            globalv.seed_words[row[0]] = row[1: len(row)]
    except IOError:
        print("Fail to open seeds.csv")
        return None
