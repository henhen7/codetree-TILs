n = input()
a = list(map(int, input().split()))
a.sort(reverse=True)
for x in a:
    print(x, end=' ')