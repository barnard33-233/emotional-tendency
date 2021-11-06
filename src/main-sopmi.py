# -*- coding=utf-8 -*-
import dataop
import globalv
import SOPMI
from test import test
import sys
import init


def main():
    file = dataop.ReadCsv(globalv.data_location)
    splited_data = dataop.SplitSentences(file)
    word_sopmi = SOPMI.SOPMI(splited_data)
    [posw, negw] = dataop.SplitNSort(word_sopmi)
    dataop.WriteCsv(posw, ["word", "so-pmi"], globalv.pos_location)
    dataop.WriteCsv(negw, ["word", "so-pmi"], globalv.neg_location)
    return None


if __name__ == '__main__':
    globalv.version = '_sopmi'
    init.initialize()
    print(globalv.seed_words)
    if globalv.test_flag:
        Stdout_save = sys.stdout
        sys.stdout = open("./out.txt", 'w', encoding='utf-8')
        test()
    else:
        main()
