# import csv
# import re
# from korean_word_relay import preprocess_word

# RAW_DATA = 'raw_data/korean5800.csv'
# FORMED_DATA = 'korean_word_relay/data/korean5800.txt'

# word_set = {'사랑', '우정', '기쁨', '슬픔'}


# with open(RAW_DATA, 'r') as fr:
#     reader = csv.reader(fr)
#     for row in reader:
#         if row[2] in ['명', '부']:
#             word = preprocess_word(row[1])
#             if word:
#                 word_set.add(word)

# with open(FORMED_DATA, 'w') as fw:
#     data = '\n'.join(list(word_set))
#     fw.write(data)

import re
with open('raw_data/killing_words_original.txt', 'r') as fr:
    with open('raw_data/killing_words.txt', 'w') as fw:
        data = fr.readlines()
        for word in data:
            word = word.strip()
            if word.startswith('['):
                continue
            patt = re.match(r'\d', word)
            if patt:
                continue
            word = word.replace('[한방]', '')
            word = word.replace(']', '')
            fw.writelines(word + '\n')

