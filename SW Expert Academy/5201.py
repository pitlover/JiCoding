'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''

n = int(input())


def sol(weights, trucks):
    result = 0

    weights.sort(reverse=True)
    trucks.sort(reverse=True)

    for truck in trucks:
        for weight in weights:
            if weight <= truck:
                result += weight
                weights.remove(weight)
                break
    return result


for i in range(n):
    n, m = map(int, input().split(" "))
    weights = list(map(int, input().split(" ")))
    trucks = list(map(int, input().split(" ")))
    result = sol(weights, trucks)
    print(f"#{i + 1} {result}")
