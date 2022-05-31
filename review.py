from itertools import combinations, permutations

## re 정규식 사용하기
## re.sub(정규 표현식, 대상 문자열, 치환문자) -> 정규식 공부하기!

import re
text = "I like apble And abple"
text_mod = re.sub('apble|abple', "apple", text) # "I like apple And apple"


## 리스트 여러개 있을 때 중복 제거
a = [4, 2, 3, 1, 3, 2,2, 1, 6]
a_no_rep = list(set(a))

## 중복을 제거하되 기존 리스트의 순서를 우지하는 경우
a_noo_rep_retain_seq = list(dict.fromkeys(a))

from collections import OrderedDict
list(OrderedDict.fromkeys(a))

seq = ('name', 'age', 'sex')
print(dict.fromkeys(seq)) # {'age':None, 'name':None, 'sex':None}
print(dict.fromkeys(seq, 10)) # {'age':None, 'name':None, 'sex':None}

# 리스트 갯수 세기
print(a.count(3))
