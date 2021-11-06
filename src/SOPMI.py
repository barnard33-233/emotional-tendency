# -*- coding = UTF-8 -*-
import globalv
import math


class Word:
    def __init__(self, word_name: str) -> None:
        self.word = word_name
        self.cnt_self = 0.0
        self.cnt_seeds = {}
        self.dist_seeds = {}
        for word in globalv.seed_words["positive"] + globalv.seed_words["negative"]:
            self.cnt_seeds[word] = 0.0
            self.dist_seeds[word] = globalv.max_dist

    def isInComment(self, cnt_seeds: dict):
        self.cnt_self += 1
        for seed in cnt_seeds:
            self.cnt_seeds[seed] += cnt_seeds[seed]

    def UpdateDist(self, dist_seeds: dict):
        for word in self.dist_seeds:
            if self.dist_seeds[word] > dist_seeds[word]:
                self.dist_seeds[word] = dist_seeds[word]
        return None

    def Cal_SOPMI(self, cnt_comment: float, p_seeds: dict) -> float:
        so_pmi = 0.0
        for seed in self.cnt_seeds:
            p_tog = float(self.cnt_seeds[seed] + 1) / cnt_comment
            p_word = (self.cnt_self + 1) / cnt_comment
            pmi = math.log(p_tog, 2) - math.log(p_seeds[seed] * p_word, 2)
            # pmi = max(pmi, globalv.floor_pmi)
            if seed in globalv.seed_words["positive"]:
                so_pmi += pmi
            elif seed in globalv.seed_words["negative"]:
                so_pmi -= pmi
        return so_pmi

    def Cal_SOPMIp(self, cnt_comment: float, cnt_seeds: dict):
        sopmi_pos = 0.0
        sopmi_neg = 0.0
        cnt_seed = len(cnt_seeds) / 2
        for seed in self.cnt_seeds:
            cnt_tog = self.cnt_seeds[seed] + 1
            cnt_word = self.cnt_self + 1
            distance = self.dist_seeds[seed]
            pmi = math.log(cnt_tog * cnt_comment, 2) - math.log((cnt_seeds[seed] + 1) * cnt_word * distance * cnt_seed, 2)
            # pmi = max(pmi, globalv.floor_pmi)
            if seed in globalv.seed_words["positive"]:
                sopmi_pos += pmi
            elif seed in globalv.seed_words["negative"]:
                sopmi_neg += pmi
        return (sopmi_pos, sopmi_neg)


def SOPMI(splited_data: list):
    # init
    word_lib = {}
    p_seeds = {}
    word_sopmi = {}
    for seed in (globalv.seed_words["positive"] + globalv.seed_words["negative"]):
        p_seeds[seed] = 0.0
    cnt_commet = len(splited_data)
    # cnt
    for comment in splited_data:
        comment_words = {x for x in comment["review"]}
        cnt_seeds = {}
        # preprocess data of seeds
        for seed in p_seeds:
            cnt_seeds[seed] = 1 if seed in comment_words else 0
            p_seeds[seed] += 1 if seed in comment_words else 0
        # cnt normal words
        for word in comment_words:
            if word in word_lib:
                word_lib[word].isInComment(cnt_seeds)
            elif word not in globalv.seed_words["positive"]+globalv.seed_words["negative"] and word not in globalv.blacklist_words:
                word_lib[word] = Word(word)
                word_lib[word].isInComment(cnt_seeds)
    # cal
    for seed in p_seeds:
        p_seeds[seed] = (p_seeds[seed] + 1) / cnt_commet
    for word in word_lib:
        word_sopmi[word] = word_lib[word].Cal_SOPMI(cnt_commet, p_seeds)
    return word_sopmi


def SOPMI_d(splited_data):
    # init
    word_lib = {}
    hit_seeds = {}
    word_sopmi = {}
    for seed in (globalv.seed_words["positive"] + globalv.seed_words["negative"]):
        hit_seeds[seed] = 0.0
    cnt_commet = len(splited_data)
    # cnt
    for comment in splited_data:
        comment_set = {x for x in comment["review"]}
        # preprocess
        index_seeds = {word: [] for word in hit_seeds}
        cnt_seeds = {word: 0 for word in hit_seeds}
        for seed in hit_seeds:
            if seed in comment_set:
                hit_seeds[seed] += 1
                cnt_seeds[seed] = 1
                index_seeds[seed] = [i for i, x in enumerate(comment["review"]) if x == seed]
        for word in comment_set:
            index_words = [i for i, x in enumerate(comment["review"]) if x == word]
            minds = {x: globalv.max_dist for x in hit_seeds}
            for seed in minds:
                for wid in index_words:
                    for sid in index_seeds[seed]:
                        minds[seed] = min(minds[seed], abs(wid - sid))
            if word not in hit_seeds and word not in globalv.blacklist_words:
                if word not in word_lib:
                    word_lib[word] = Word(word)
                word_lib[word].isInComment(cnt_seeds)
                word_lib[word].UpdateDist(minds)
    # cal
    for word in word_lib:
        word_sopmi[word] = word_lib[word].Cal_SOPMIp(cnt_commet, hit_seeds)
    return word_sopmi


def SplitSOPMIp(word_sopmi: dict):
    pos_sopmi = dict()
    neg_sopmi = dict()
    for word in word_sopmi:
        pos_sopmi[word] = word_sopmi[word][0]
        neg_sopmi[word] = word_sopmi[word][1]
    posw = sorted(pos_sopmi.items(), key=lambda key: key[1], reverse=True)
    negw = sorted(neg_sopmi.items(), key=lambda key: key[1], reverse=True)
    return [posw, negw]


# def SplitNSort(word_sopmi: dict) -> list:
#     posw_sopmi = {x: word_sopmi[x] for x in word_sopmi if word_sopmi[x] > 0.0}
#     negw_sopmi = {x: word_sopmi[x] for x in word_sopmi if word_sopmi[x] < 0.0}
#     posw = sorted(posw_sopmi.items(), key=lambda key: key[1], reverse=True)
#     negw = sorted(negw_sopmi.items(), key=lambda key: key[1], reverse=False)
#     result = [posw, negw]
#     return result
