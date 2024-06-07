n = int(input())
# 2차원 리스트 맵 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 방문 처리를 위한 리스트 생성
    visit = []
    for i in range(n):
        visit.append([False] * n)

# 2차원 맵 내에서의 재귀함수 생성
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우, 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 노드가 1이고, 해당 노드를 방문하지 않았을 시 방문 처리
    if graph[x][y] == 1 and visit[x][y] == False:
        visit[x][y] = True
        # 상하좌우 위치 모두 재귀적으로 호출하면서 카운트
        count = 1 # 시작 노드
        count += dfs(x - 1, y)
        count += dfs(x, y - 1)
        count += dfs(x + 1, y)
        count += dfs(x, y + 1)
        return count
    return False

ans = 0
size = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == False:
            ans += 1 # 시작점 체크
            size.append(dfs(i, j)) # dfs 함수 돌면서 사이즈 리스트에 추가

print(ans)
for i in size:
    print(i)