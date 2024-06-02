n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

# 내림차순으로 정렬하여 3개 단위로 슬라이스
list = []
for i in range(0, n, 3):
    list.append(a[i:i+3])

ans = 0

# 3개로 단위로 슬라이스된 경우, 리스트 안의 각 배열의 최솟값을 제외하고 합계 구함
# 3개 미만인 경우 그냥 합
for i in list:
    if len(i) == 3:
        lsum = sum(i) - min(i)
        ans += lsum
    else:
        ans += sum(i)

print(ans)