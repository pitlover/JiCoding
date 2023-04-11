'''
2
I am happy today
We want to win the first prize
'''

n = int(input())


def my_solution(Text):
    texts = Text.split(" ")
    for text in texts:
        print(text[::-1], end=' ')
    return


for i in range(n):
    my_solution(input())
    print()
