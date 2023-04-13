'''
4 6
a t c i s w
'''
'''
4 6
a e i o v z
'''
'''
3 6
a e i c d z
'''
from itertools import combinations

l, c = map(int, input().split())
alphas = input().split(" ")
alphas.sort()
all_combs = set(combinations(alphas, l))

non_specs = []
specs = []
for i in alphas:
    if i not in ['a', 'e', 'o', 'u', 'i']:
        non_specs.append(i)
    else:
        specs.append(i)

specs = set(combinations(specs, 1))
non_specs = set(combinations(non_specs, 2))
all_combs_ = []

for spec in specs:
    for non_spec in non_specs:
        tmp = list(spec + non_spec)
        tmp.sort()
        all_combs_.append("".join(tmp))

if l == 3:
    all_combs_.sort()
    for a in all_combs_:
        print("".join(a))
else:
    all_combs = []
    for a in all_combs_:
        a = set(list(a))
        remain = set(alphas) - set(a)
        remains = set(combinations(remain, l - 3))
        for b in remains:
            a_ = list(a.union(b))
            a_.sort()
            all_combs.append("".join(a_))
    all_combs = list(set(all_combs))
    all_combs.sort()

    for a in all_combs:
        print("".join(a))
