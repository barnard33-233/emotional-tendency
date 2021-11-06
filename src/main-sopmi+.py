# -*- coding=utf-8 -*-
import dataop
import globalv
import SOPMI
import init


def main():
    file = dataop.ReadCsv(globalv.data_location)
    splited_data = dataop.SplitSentences(file)
    word_sopmi = SOPMI.SOPMI_d(splited_data)
    [posw, negw] = SOPMI.SplitSOPMIp(word_sopmi)
    dataop.WriteCsv(posw, ["word", "sopmi"], globalv.pos_location)
    dataop.WriteCsv(negw, ["word", "sopmi"], globalv.neg_location)
    return None


if __name__ == "__main__":
    globalv.version = "_sopmi+"
    init.initialize()
    main()
