import sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for i in range(n)]
ans = [(len(b), b) for b in a]
ans.sort()

for i, j in ans:
    print(j)