# -*- coding = UTF-8 -*-
test_flag = False
log_flag = False
paddle_flag = True
blacklist_words = [
    ',', '.', ':', ';', '。', '，', '；', '：', '、'
]
seed_words = {
    "positive": [],
    "negative": []
}
seeds_location = '..\\data\\seeds.csv'
data_location = '..\\data\\comments.csv'
pos_location = '..\\data\\result_pos.csv'
neg_location = '..\\data\\result_neg.csv'
frequency_location = '..\\data\\frequency.csv'
# floor_pmi = -0.00000000000001
max_dist = 100000
