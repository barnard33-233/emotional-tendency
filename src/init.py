import os
import globalv


def initialize():
    set_path()
    read_seeds()


def set_path():
    present_path = os.listdir(".")
    if 'src' in present_path:
        globalv.data_location = '.\\data\\comments.csv'
        globalv.pos_location = '.\\data\\result_pos.csv'
        globalv.neg_location = '.\\data\\result_neg.csv'
    return None


def read_seeds():
    pass
