import globalv
import dataop
import SOPMI
import os


def test():
    print("start to run test module...")
    print("path of sourcedata:", globalv.data_location)
    file = dataop.ReadCsv(globalv.data_location)
    splited_data = dataop.SplitSentences(file)
    print("finish preoperate of data")
    # word = SOPMI.Word("test word")
    # for i in word.cnt_seeds:
    #     word.cnt_seeds[i] = 5
    # word.cnt_self = 20
    # print("word:", word.word)
    # print("seeds:", word.cnt_seeds)
    # print("cnt:", word.cnt_self)
    # p_seeds = {
    #     "好吃": 0.25,
    #     "难吃": 0.05,
    #     "好评": 0.25,
    #     "差评": 0.05
    # }
    # cntall = 100
    # sopmi = word.Cal_SOPMI(cntall, p_seeds)
    # print("sopmi=", sopmi)
    print("finish test module")
    return None


def test_x():
    print("start with test")
    print(os.listdir("."))
    print(os.listdir(".."))
    print("end test")


if __name__ == "__main__":
    test_x()
