# -*- coding = UTF-8 -*-
test_flag = False
log_flag = False
blacklist_words = [
    ',', '.', ':', ';', '。', '，', '；', '：', '、'
]
seed_words = {
    "positive": ["好吃", "好评"],
    "negative": ["难吃", "差评"]
}
seeds_location = '..\\data\\seeds.csv'
data_location = '..\\data\\comments.csv'
pos_location = '..\\data\\result_pos.csv'
neg_location = '..\\data\\result_neg.csv'
