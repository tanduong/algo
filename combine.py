from itertools import combinations, permutations, chain

# for x in combinations([1, 2], 1):
#     print(x)

# for x in permutations([1, 2]):
#     print(x)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for x in powerset([1, 2, 3]):
    print(x)
