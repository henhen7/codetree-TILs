from collections import deque

n, m = map(int, input().split())

# 인접 리스트 생성
graph = [list(map(int, input().split())) for _ in range(n)]

# BFS 큐 생성(deque 사용)
def bfs():
    Q = deque()
    Q.append((0, 0))
    
    dx = [-1, 0, 1, 0]  # 북쪽부터 시계방향
    dy = [0, 1, 0, -1]
    
    # 방문 리스트 초기화
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    
    # 시작 위치의 거리 초기화
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1  # 출발 지점도 1로 계산
    
    while Q:
        x, y = Q.popleft()  # 현재 위치
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:  # 경계 내에 있는지 확인
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    Q.append((nx, ny))

                    if nx == n-1 and ny == m-1:  # 목적지에 도달한 경우
                        return distance[nx][ny]

    return -1  # 목적지에 도달할 수 없는 경우 -1 반환 (필요에 따라 수정 가능)

print(bfs())