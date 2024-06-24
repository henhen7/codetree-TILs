n, p = map(int, input().split())
li = [n]
count = []
seen = {}
while li:
    num = li.pop()
    remain = (num * n) % p
    count.append(remain)

    if remain in seen:
        start = seen[remain]
        length = len(count) - start
        break

    li.append(remain)
    seen[remain] = len(count)

print(length)