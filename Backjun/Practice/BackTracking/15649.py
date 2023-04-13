n, m = map(int, input().split())
from itertools import permutations

results = list(permutations(range(1, n+1), m))

for a in results:
    print(*a)
