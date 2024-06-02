a = list(map(int, input().split()))
ans = 1
if (a[0] % 2 == 0) and (a[1] % 2 == 0) and (a[2] % 2 == 0):
    ans = a[0] * a[1] * a[2]

for i in a:
    if i % 2 == 1:
        ans *= i

print(ans)