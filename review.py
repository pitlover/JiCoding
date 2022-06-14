from itertools import combinations, permutations

## re 정규식 사용하기
## re.sub(정규 표현식, 대상 문자열, 치환문자) -> 정규식 공부하기!
# https://wikidocs.net/4308
# findall, finditer
import re
text = "I like apble And abple"
text_mod = re.sub('apble|abple', "apple", text) # "I like apple And apple"

s = "park 010-9999-9988\nkim 010-9909-7789\nlee 010-8789-7768"
p = re.compile('(\w*\s\d{3}[-]\d{4}[-])\d{4}')
print(p.findall(s))

s = re.sub('(\w*\s\d{3}[-]\d{4}[-])\d{4}', '\g<1>****', s)

## dict 값 가져오기
sample.get(a, 0) # sample의 a가져오기 없으면 0

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

## 문자열을 해당 진법으로 바꾸기
tmp = "12"
print(int(tmp, 3))

# list a.sort() vs sorted(a) 중 .sort 가 더 빠름

# dict key 기준으로 sort기
result = {5:100, 2:1000, 10:3, 8:0}
final = sorted(result.items())
# dict value 기준으로 sort
final = dict(sorted(result.items(), key= lambda x:x[1], reverse = True))

# 리스트 갯수 세기
list_ = [1, 2, 1, 1, 2, 5, 6, 6]
print(list_.count(2)) # 2

# 값으로 정렬하기 - 1
>>> dic = {'a': 4, 'b':3, 'c':2, 'd':1}
print(sorted(dic))            # ['a', 'b', 'c', 'd']
print(sorted(dic.items()))    # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print(sorted(dic.items(), key=lambda x:x[1]))     # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(sorted(result.items(), key= lambda x:x[1], reverse = True))   # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

# gcd
from math import gcd

# combinations, permutations
from itertools import permutations, combinations

from collections import Counter

# tuple sort
temp = (5, 1, 2, 3, 4, 1)
sort_temp = tuple(sorted(temp, key=lambda x:x))

# min, max 값의 index
li = [10,20,30,40]

# 가장 작은 값의 index
def min_index(li):
    return min(range(len(li)), key=li.__getitem__)
# 가장 큰 값의 index
def max_index(li):
    return max(range(len(li)), key=li.__getitem__)
>>> min_index(li) # 0
>>> max_index(li) # 3

# eval : string -> dict, list
myStr = '{name: "webisfree", domain: "dotcom"}'
myDict = eval(myStr)

print myStr['name'] # "webisfree"

# set
a = {1, 2, 3}
b = {2, 3, 4}
a.add(4) # {1, 2, 3, 4}
a.difference(b) # {1}
a.union(b) # {1, 2, 3, 4}
a.intersection(b) # {2, 3}
a.symmetric_difference(b) # 대칭차집합 {1, 4}
a.issubset(b) # 부분집합 확인
a.issuperset(b) # 슈퍼집합 확인
a.isdisjoint(b) # 교집합 있는지 확인

# bytearray : string 위치로 변경하기
s = 'Naze'
b = bytearray(s)
b[2] = 'm'
s = str(b)
print(s)

# deque
from collections import deque
a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2) # 시계방향 양수, 그 반대 음수
result = list(q)    # [4, 5, 1, 2, 3]
q.append(6)     # [1, 2, 3, 4, 5, 6]
q.appendleft(0) # [0, 1, 2, 3, 4, 5, 6]
q.pop()     # 6
q.popleft() # 0
#seek
q[0]
