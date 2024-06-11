from collections import deque
n, m = map(int, input().split())

# 맵, 방문 리스트 생성
graph = []
visit = []

graph.append([9]*(m+2))
for _ in range(n):
    graph.append([9] + list(map(int, input().split())) + [9])
graph.append([9]*(m+2))

# 직사각형 크기, 시작점, 도착점 좌표 받기
h, w, sx, sy, ex, ey = map(int, input().split())

# print(graph[2][3])
# print(n, m, h, w, sx, sy, ex, ey)

# BFS
# 큐: sx, sy, count 전부 넣고 돌림
# sx, sy를 시작점으로 오른쪽으로 w, 아래쪽으로 h만큼 bfs 인접 노드 탐색
# 1인 노드 있으면 False 반환, 없으면 방문 처리 후 카운트 +1
# 도착점에 도착 시 리턴, 카운트 +1
# 이동할 수 없는 경우(큐 나와서) -1 반환


# (1.1) -> (2.4)
# dx : 0 1
# dy : 0 1 2 3


def bfs(x, y):
    # 큐 생성(시작점, 카운트)
    Q = deque()
    Q.append((x, y, 0))
    count = 0

    dx = [-1, 0, 1, 0] # 북쪽부터 시계방향
    dy = [0, 1, 0, -1]

    # 방문 리스트 초기화
    for _ in range(n + 2):
        visit.append([False] * (m + 2))
    
    # 시작점 방문 처리
    visit[x][y] = True

    # 큐
    while Q:
        (x, y, count) = Q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # nx, ny가 맵 안에 있고, 값이 0이고 방문 처리 없는지 확인
            if (1 <= nx <= n) and (1 <= ny <= m) and graph[nx][ny] == 0 and not visit[nx][ny]:
                # 직사각형이 맵 내에서 지나갈 수 있는 지 체크
                if nx < 1 or ny < 1 or nx + h - 1 > n or ny + w - 1> m:
                    continue # for i in range(4) loop: 직사각형이 맵을 벗어나는 경우, 해당 방향을 건너뜀
                for i in range(h):
                    for j in range(w):
                        if graph[nx + i][ny + j] == 1:
                            break # for j in range(w) loop
                    else: # 파이썬 for - else문: for loop이 성공적으로 돌면 else를 실행
                        continue # for i in range(h) loop: 직사각형 내부에 1이 없는 경우, 다시 방향 탐색
                    break # for i in range(h) loop
                
                else:
                # 지나갈 수 있다면 방문 체크하고 큐에 추가
                    if nx == ex and ny == ey:
                        return count + 1
                    visit[nx][ny] = True
                    Q.append((nx, ny, count + 1))
    return -1 # 이동에 실패하면 -1 리턴

print(bfs(sx, sy))