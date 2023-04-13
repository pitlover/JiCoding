'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''

n = int(input())
cards = map(int, input().split())
m = int(input())
cases = map(int, input().split())

card_dict = {}
for card in cards:
    if card_dict.get(card) == None:
        card_dict[card] = 1
    else:
        card_dict[card] += 1


for case in cases:
    if card_dict.get(case) == None:
        print(0, end=" ")
    else:
        print(card_dict[case], end=" ")
