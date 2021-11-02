# -*- coding = UTF-8 -*-
import globalv
import math


class Word:
    def __init__(self, word_name: str) -> None:
        self.word = word_name
        self.cnt_self = 0.0
        self.cnt_seeds = {}
        for word in globalv.seed_words["positive"] + globalv.seed_words["negative"]:
            self.cnt_seeds[word] = 0.0

    def isInComment(self, cnt_seeds: dict):
        self.cnt_self += 1
        for seed in cnt_seeds:
            self.cnt_seeds[seed] += cnt_seeds[seed]

    def Cal_SOPMI(self, cnt_comment: float, p_seeds: dict) -> float:
        pos_pmi = {}
        neg_pmi = {}
        so_pmi = 0.0
        for seed in self.cnt_seeds:
            p_tog = float(self.cnt_seeds[seed]) / cnt_comment
            p_word = self.cnt_self / cnt_comment
            if globalv.log_flag:
                print("SOPMI->Word'%s'->Cal_SOPMI->p_tog" % (self.word), p_tog)
                print("SOPMI->Word'%s'->Cal_SOPMI->p_word" % (self.word), p_word)
            pmi = math.log(p_tog + 1, 2) - math.log(p_seeds[seed] * p_word + 1, 2)
            if seed in globalv.seed_words["positive"]:
                pos_pmi[seed] = pmi
            elif seed in globalv.seed_words["negative"]:
                neg_pmi[seed] = pmi
        for seed in pos_pmi:
            so_pmi += pos_pmi[seed]
        for seed in neg_pmi:
            so_pmi -= neg_pmi[seed]
        return so_pmi


def SOPMI(splited_data: list):
    word_lib = {}
    p_seeds = {}
    word_sopmi = {}
    for seed in (globalv.seed_words["positive"] + globalv.seed_words["negative"]):
        p_seeds[seed] = 0.0
    cnt_commet = len(splited_data)
    for comment in splited_data:
        comment_words = {x for x in comment["review"]}
        cnt_seeds = {}
        for seed in p_seeds:
            cnt_seeds[seed] = 1 if seed in comment_words else 0
            p_seeds[seed] += 1 if seed in comment_words else 0
        for word in comment_words:
            if word in word_lib:
                word_lib[word].isInComment(cnt_seeds)
            elif word not in globalv.seed_words["positive"]+globalv.seed_words["negative"] and word not in globalv.blacklist_words:
                word_lib[word] = Word(word)
                word_lib[word].isInComment(cnt_seeds)
    for seed in p_seeds:
        p_seeds[seed] /= cnt_commet
    for word in word_lib:
        word_sopmi[word] = word_lib[word].Cal_SOPMI(cnt_commet, p_seeds)
    return word_sopmi


def SplitNSort(word_sopmi: dict) -> list:
    posw_sopmi = {x: word_sopmi[x] for x in word_sopmi if word_sopmi[x] > 0.0}
    negw_sopmi = {x: word_sopmi[x] for x in word_sopmi if word_sopmi[x] < 0.0}
    posw = sorted(posw_sopmi.items(), key=lambda key: key[1], reverse=True)
    negw = sorted(negw_sopmi.items(), key=lambda key: key[1], reverse=False)
    result = [posw, negw]
    return result
