n, m = map(int, input().split())
# 2차원 리스트 맵 생성
graph = []
# 맵의 상하좌우에 0으로 둘러싸이도록 1칸씩 확장
graph.append([0] * (m+2))
for i in range(n):
    graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0] * (m+2))

# 방문 처리를 위한 리스트 생성
visit = []
for i in range(n + 2):
    visit.append([False] * (m + 2))
count = 0

# 2차원 맵 내에서의 스택 생성
def dfs(x, y):
    global count
    stack = []
    stack.append((x, y))
    # 현재 노드가 0이고, 해당 노드를 방문하지 않았을 시 방문 처리
    if graph[x][y] == 0 and visit[x][y] == False:
        visit[x][y] = True
    
    while stack:
        x, y = stack.pop()
        # 각 인접칸의 방향 정의 -> 짝수행인 경우, 홀수행인 경우
        if x % 2 == 0:
            directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
        else:
            directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        
        for dx, dy in directions:
            # 현재 노드의 인접칸 좌표를 설정하고, 하나씩 반복문 돌며 확인
            nx, ny = x + dx, y + dy 
            # 인접 노드가 맵의 범위 내에 있는 경우만 방문 처리를 확인한다.
            # 맵에서 1로 주어진 경우, 벽의 개수를 1개 추가한다.
            if (0 <= nx < n + 2) and (0 <= ny < m + 2):
                if graph[nx][ny] == 1:
                    count += 1
            # 인접 노드가 방문하지 않은 노드인 경우, 스택에 추가하고 방문 처리
                if graph[nx][ny] == 0 and visit[nx][ny] == False:
                    stack.append((nx, ny))
                    visit[nx][ny] = True

# 내부의 빈 부분까지 확인할 필요는 없으므로, 시작점을 (0,0)으로 설정해 겉부분만 탐색
# 맵의 확장으로 인해 모든 칸이 연결되어 있다.
dfs(0,0)
print(count)