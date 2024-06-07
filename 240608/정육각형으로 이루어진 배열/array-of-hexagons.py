"""
6방향 인접칸 구하기
(2,3)일 때
(x - 1, y - 1)
(x - 1, y)
(x, y - 1)
(x, y + 1)
(x + 1, y - 1)
(x + 1, y)

(3,3)일 때
(x - 1, y)
(x - 1, y + 1)
(x, y - 1)
(x, y + 1)
(x + 1, y)
(x + 1, y + 1)
"""

n, m = map(int, input().split())
# 2차원 리스트 맵 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 방문 처리를 위한 리스트 생성
visit = []
for i in range(n):
    visit.append([False] * m)

# 2차원 맵 내에서의 재귀함수 생성
def dfs(x, y):
    # 현재 노드가 1이고, 해당 노드를 방문하지 않았을 시 방문 처리
    if graph[x][y] == 1 and visit[x][y] == False:
        visit[x][y] = True
        count = 0
        # 각 인접칸의 방향 정의 -> 짝수행인 경우, 홀수행인 경우
        if x % 2 == 0:
            directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
        else:
            directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        
        for dx, dy in directions:
            # 현재 노드의 인접칸 좌표를 설정하고, 하나씩 반복문 돌며 확인
            nx, ny = x + dx, y + dy 
            # 인접 노드의 값이 0이거나 범위를 벗어나는 경우, 벽의 개수 카운트 증가
            # 범위를 벗어나는 경우, 값을 가지지 않으므로(index를 벗어나는 값) 해당 경우 조건을 먼저 처리
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or graph[nx][ny] == 0:
                count += 1
            # 인접 노드가 방문하지 않은 노드인 경우, dfs를 재귀적으로 돌며 위 반복문에 대한 카운트 추가
            # dfs 탐색
            elif graph[nx][ny] == 1 and visit[nx][ny] == False:
                count += dfs(nx, ny)
        return count
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == False:
            ans += dfs(i, j)

print(ans)