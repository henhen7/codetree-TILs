# %2 == 0 : 모두 O
# 3초 후 부터 +3 단위(3, 7, 11 ...)
# 5초 후 부터 +3 단위(5, 9, 13 ...)

from collections import deque

n, m, s = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]


def simulate(n, m, s, graph):
    if s == 1:
        return graph
    elif s % 2 == 0:
        return [['O'] * m for _ in range(n)]
        
    def bfs(graph):
        Q = deque()
        
        # 방문 리스트 초기화
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 'O':
                    Q.append((i, j))

        dx = [-1, 0, 1, 0] # 북쪽부터 시계방향
        dy = [0, 1, 0, -1]
        
        fin_graph = [['O'] * m for _ in range(n)]
        while Q:
            x, y = Q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    fin_graph[x][y] = '.'
                    fin_graph[nx][ny] = '.'
        return fin_graph


    three_seconds = bfs(graph)
    five_seconds = bfs(three_seconds)

    return three_seconds if s % 4 == 3 else five_seconds


ans = simulate(n, m, s, graph)
for i in range(n):
    for j in range(m):
        print(ans[i][j], end = '')
    print()