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
        globalv.pos_location = '.\\data\\result_pos.csv'
        globalv.neg_location = '.\\data\\result_neg.csv'
        globalv.frequency_location = '.\\data\\frequency.csv'
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
