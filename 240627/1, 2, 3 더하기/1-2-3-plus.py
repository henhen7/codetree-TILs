'''
a[1] = 1
a[2] = 2
a[3] = 4
a[4] = 7
a[5] = 13
a[6] = 24
...
a[n] = a[n-1] + a[n-2] + a[n-3]
'''

n = int(input())
d = [0 for _ in range(3 + n)]
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(n + 1):
    if i > 3:
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

print(d[n])