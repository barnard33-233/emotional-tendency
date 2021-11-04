# -*- coding=utf-8 -*-
import init
import globalv
import dataop


def getFrequency(data: list):
    word_cnt = {}
    for comment in data:
        word_lib = set(comment["review"])
        for word in word_lib:
            if word in word_cnt:
                word_cnt[word] += 1
            else:
                word_cnt[word] = 1
    result = sorted(word_cnt.items(), key=lambda key: key[1], reverse=True)
    return (result, word_cnt)


if __name__ == "__main__":
    init.initialize()
    file = dataop.ReadCsv(globalv.data_location)
    data = dataop.SplitSentences(file)
    (frequency, word_cnt) = getFrequency(data)
    dataop.WriteCsv(frequency, ["word", "cnt"], globalv.frequency_location)
