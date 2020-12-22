with open("day1.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

cache = set()
for i in lines:
    if 2020 - i in cache:
        print(i, 2020 - i, i * (2020 - i))
    else:
        cache.add(i)
cache.clear()

for i in lines:
    for j in lines:
        if 2020 - i - j in cache:
            print(i, j, 2020 - i - j, i * j * (2020 - i - j))
        else:
            cache.add(j)
    cache.clear()
