# -*- coding=utf-8 -*-
import OpenHowNet
import globalv


def OHN(data: list):
    HowNet = OpenHowNet.HowNetDict()
    HowNet.initialize_sememe_similarity_calculation()
    word_lib = {}
    for comment in data:
        word_set = set(comment["review"])
        for word in word_set:
            if word not in globalv.seed_words["positive"] + globalv.seed_words["negative"]:
                if word not in globalv.blacklist_words:
                    if word not in word_lib:
                        word_lib[word] = Polarity(word, HowNet)
    return word_lib


def Polarity(word: str, HowNet):
    if not HowNet.has(word):
        return 0.0
    polar = 0.0
    cnt_pos = len(globalv.seed_words["positive"])
    cnt_neg = len(globalv.seed_words["negative"])
    for seed in globalv.seed_words["positive"]:
        polar += float(HowNet.calculate_word_similarity(word, seed)) / float(cnt_pos)
    for seed in globalv.seed_words["negative"]:
        polar -= float(HowNet.calculate_word_similarity(word, seed)) / float(cnt_neg)
    return polar
