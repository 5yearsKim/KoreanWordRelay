# korean-word-relay
### 끝말잇기 패키지 for python 
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
- import_default(boolean): If True, import candidates of korean words from '자주 쓰이는 한국어 낱말 모음 5800' https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800 
- words_path(None|string): If given path(.txt), import candidates of words list from txt file
- use_dueum(boolean): If True, 두음법칙 is allowed
- debug_print(boolean): If True, print warning message on console

### Example format for words_path
`words_path` should be None or **list of korean words in txt extension**. For instance, `word_list.txt` should be
```
사랑
우정
믿음
.
.
여자친구
```



