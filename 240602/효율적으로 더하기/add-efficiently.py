n = int(input())
a = list(map(int, input().split()))
a.sort() # 총 합의 최솟값이므로 배열 오름차순 정렬하고 더하면 됨

b = 0
answer = 0

for i in range(n):
    b += a[i]
    answer += b

print(answer)