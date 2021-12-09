import os
import re
from hgtk import letter, checker

installpath = os.path.dirname(os.path.realpath(__file__))

def preprocess_word(word):
    if not word:
        return None
    word = word.strip()
    word = re.sub('\W+', '', word)
    word = re.sub('\d', '', word)
    if len(word) < 2:
        return None
    return word

def load_words_from_txt(word_path):
    if not word_path.endswith('.txt'):
        raise ValueError('words file extension should be .txt')
    with open(word_path, 'r') as fr:
        lines = fr.readlines()
    holder = []
    for word in lines:
        processed = preprocess_word(word)
        if processed:
            holder.append(processed)
    return holder

def words2dict(word_list, word_dict):
    assert type(word_dict) is dict
    for word in word_list:
        if word[0] in word_dict:
            word_dict[word[0]].add(word)
        else:
            word_dict[word[0]] = {word}
    return word_dict


def dueum(char):
    DU_MO = ['ㅣ', 'ㅑ', 'ㅕ', 'ㅛ', 'ㅠ']
    if not checker.is_hangul(char):
        return None
    ja = letter.decompose(char)
    if len(ja) < 2:
        return None
    ja = list(ja)
    cand_list = []
    # ㄹ 두음법칙
    if ja[0] in ['ㄹ']:
        ja[0] = 'ㄴ'
        cand_list.append(letter.compose(*ja))
    # ㄴ 두음법칙
    if ja[0] in ['ㄴ'] and ja[1] in DU_MO:
        ja[0] = 'ㅇ'
        cand_list.append(letter.compose(*ja))
    return cand_list 

if __name__ == '__main__':
    result = dueum('류')
    print(result)
