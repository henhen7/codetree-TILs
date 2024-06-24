from collections import defaultdict
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
# print(li)

count = defaultdict(int)
for i in range(n):
    start = li[i][0]
    length = li[i][1] - li[i][0]
    computer = li[i][2]
    for j in range(length):
        count[start + j] += computer
# print(count)

print(max(count.values()))