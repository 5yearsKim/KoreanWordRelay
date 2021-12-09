# korean-word-relay
### 끝말잇기 package for python 
* 한국어 낱말 게임 끝말잇기를 쉽게 커스터마이징 할 수 있는 패키지
* 모델이 사용할 끝말잇기 단어 직접 선택 (난이도 조절 가능)
* 두음법칙 적용 (여부 선택)
* 이전 단어와 이어지지 않거나 이미 나왔던 단어 입력시 패배


## Installation
Using `pip`:
```
pip install korean-word-relay
```

## Usage
### Quick Start
```python
from korean_word_relay import WordRelay

word_relay = WordRelay()
word_relay.play()
```
### result
```
--------------끝말잇기----------------
시작 단어: 파이썬
<< 썬샤인
>> 인간
<< 간택
>> 택시
<< 시리
>> 리그
<< 그대
>> 대략
<< 약관
>> 관람
<< 람보
>> 보도
<< 도로묵
------------------------------
no word to answer
YOU WIN!
```
<hr/>

### Default optional parameter
```python
word_relay = WordRelay(import_default=True, words_path=None, use_dueum=True, debug_print=True):
)
```
- import_default(boolean): If True, import candidates of korean words from ['자주 쓰이는 한국어 낱말 모음 5800'](https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800)
- `words_path(None|string)`: If given path(.txt), import candidates of words list from txt file
- `use_dueum(boolean)`: If True, 두음법칙 is allowed
- `debug_print(boolean)`: If True, print warning message on console

### Example format for words_path
`words_path` should be `None` or **list of korean words in txt extension**. For instance, `word_list.txt` should be
```
사랑
우정
믿음
.
.
여자친구
```
If you want to make game much difficult, get `killing_words.txt` from [here](https://github.com/5yearsKim/korean_word_relay/blob/main/raw_data/killing_words.txt).

<hr/>

###  Methods of WordRelay

```python
word_relay = WordRelay()

# 주어진 낱말에 이어지는 단어 리턴
# set log_history=False if you don't want to add word in history
next_word = word_relay.get_next('성질') # next_word is None or 질X (예: 질문)

# 두 낱말이 이어지는지 여부 체크
is_continue = word_relay.check_continue('질문', '문지기') # is_continue == True

# 특정 낱말을 이미 나온말(history)에 추가
word_relay.add_history('문지기')
print(word_relay.history) # word_relay.history = ['질문', '문지기'], 질문 was added get_next above

# history 를 초기화
word_relay.reset()
print(word_relay.history) # word_relay.history = []
```

## etc
Checking whether word is valid or not is not implemented in this project, since 1. criteria for *valid language* is keep changing, 2. including korean dictionary can make this package too big. You can implement your own code to check whether word is valid or not.


