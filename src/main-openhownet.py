# -*- coding=utf-8 -*-
import OHN
import globalv
import init
import dataop


def main():
    file = dataop.ReadCsv(globalv.data_location)
    splited_data = dataop.SplitSentences(file)
    word_polar = OHN.OHN(splited_data)
    [posw, negw] = dataop.SplitNSort(word_polar)
    dataop.WriteCsv(posw, ["word", "sopmi"], globalv.pos_location)
    dataop.WriteCsv(negw, ["word", "sopmi"], globalv.neg_location)
    return None


if __name__ == "__main__":
    globalv.version = '_ohn'
    init.initialize()
    main()
