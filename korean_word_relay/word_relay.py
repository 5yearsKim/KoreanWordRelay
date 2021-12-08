
from .utils import installpath, load_words_from_txt, words2dict, preprocess_word, dueum

err_code = {
    0: 'word is too short',
    1: 'word is already in history',
    2: 'last letter not matching'
}

class WordRelay:
    def __init__(self, import_default=True, words_path=None, use_dueum=True, debug_print=True):
        self.use_dueum = use_dueum
        self.debug_print = debug_print
        word_dict = {}
        if import_default:
            default_words_path = f'{installpath}/data/korean5800.txt'
            words = load_words_from_txt(default_words_path)
            word_dict = words2dict(words, word_dict)
        if words_path:
            words = load_words_from_txt(words_path)
            word_dict = words2dict(words, word_dict)
        self.word_dict = word_dict
        self.history = []
    
    def add_history(self, word):
        word = preprocess_word(word)
        if not word:
            if self.debug_print:
                print(err_code[0])
            return False 
        if word in self.history:
            if self.debug_print:
                print(err_code[1])
            return False
        self.history.append(word)
        return True

    def reset(self):
        self.history = []
    
    def check_continue(self, first, second):
        second = preprocess_word(second)
        if not second:
            if self.debug_print:
                print(err_code[0])
            return False 
        last_letter = first.strip()[-1]
        if last_letter == second[0]:
            return True
        if self.use_dueum:
            dueum_letter = dueum(last_letter)
            if dueum_letter and dueum_letter == second[0]:
                return True
        return False

    def get_next(self, word, log_history=True):
        word = preprocess_word(word)
        if not word:
            if self.debug_print:
                print(err_code[0])
            return False 
        last_letter = word[-1]
        cand_list = [last_letter]  
        if self.use_dueum:
            dueum_letter = dueum(last_letter)
            if dueum_letter:
                cand_list.append(dueum_letter)
        for letter in cand_list:
            if letter in self.word_dict:
                for cand_word in self.word_dict[letter]:
                    if cand_word in self.history:
                        continue
                    else:
                        if log_history:
                            self.add_history(cand_word)
                        return cand_word
        return None

    def play(self, start_word='파이썬'):
        print('--------------끝말잇기----------------')
        last_word = start_word 
        print(f'시작 단어: {last_word}')
        message = ''
        is_win = False
        while True:
            word = input('<< ')
            word = preprocess_word(word)
            if not word:
                if self.debug_print:
                    print(err_code[0])
                message = f'{word} is too short.'
                break
            if word in self.history:
                if self.debug_print:
                    print(err_code[1])
                message = f'{word} is already on game.'
                break
            if not self.check_continue(last_word, word):
                if self.debug_print:
                    print(err_code[2])
                message = f'{last_word} not matching with {word}'
                break
            next_word = self.get_next(word)
            if not next_word:
                is_win = True
                message = 'no word to answer'
                break
            print(f'>> {next_word}')
            last_word = next_word
        print('------------------------------')
        print(message)
        if is_win:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')

            






