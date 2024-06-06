n, m = map(int, input().split())

li = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b) # 단방향 처리

# 방문 처리를 위한 리스트 생성
visit = [False] * (n + 1)

# 재귀 함수 생성
def dfs(node):
    visit[node] = True 
    for i in li[node]:
        if not visit[i]:
            dfs(i) 
        
result = [[] for _ in range(n + 1)] # 각 노드별 방문 횟수를 담을 리스트 생성

for i in range(n + 1):
    dfs(i)
    result[i].append((sum(visit) - 1))
    visit = [False] * (n + 1) # 모든 케이스를 처리해야하므로, 방문 표시 초기화

ans = []
for i in range(n + 1):
    if result[i] == max(result): #반복문을 돌면서 result의 최대값과 일치할 시, i를 정답 리스트에 추가
        ans.append(i)

for i in ans:      
    print(i, end = ' ')