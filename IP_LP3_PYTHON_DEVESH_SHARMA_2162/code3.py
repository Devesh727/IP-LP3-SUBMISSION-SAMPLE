#code3
n  = int(input())

Set = set()
Dict = {}

for i in range(n):
    x = input()[:-1]
    if x not in Set:
        Set.add(x)
        Dict[x] = 1
    else:
        Dict[x] += 1

print(len(Set))
# print(' '.join(list(map(str, Dict.values()))))
print(*Dict.values())
