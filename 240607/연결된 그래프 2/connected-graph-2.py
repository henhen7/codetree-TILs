n, m = map(int, input().split())

li = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b) # 단방향 처리

# 스택으로 처리
def dfs(i):
    visit = [False] * (n + 1)
    stack = [i]
    count = 0

    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node] = True
            for j in li[node]:
                if not visit[j]:
                    stack.append(j)
            if node != i:
                count += 1
    return count

result = [[] for _ in range(n + 1)] # 각 노드별 방문 횟수를 담을 리스트 생성

for i in range(n + 1):
    result[i].append(dfs(i))

ans = []
for i in range(n + 1):
    if result[i] == max(result): #반복문을 돌면서 result의 최대값과 일치할 시, i를 정답 리스트에 추가
        ans.append(i)

for i in ans:      
    print(i, end = ' ')