n, m, s = map(int, input().split())
li = [[] for _ in range(n + 1)]

# 인접 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a) 

# 각 리스트의 원소(정점)을 오름차순으로 정렬
for i in li:
    i.sort()

# 방문 처리 리스트 생성
visit = [False] * (n + 1)
stack = [s]
dfs = []
bfs = []

# DFS 스택 생성
while stack:
    node = stack.pop() # 방문 노드 처리
    if not visit[node]:
        visit[node] = True
        # 해당 노드에 연결된 노드의 리스트를 역순으로 순회하며 스택에 쌓음
        # 스택처리 시 큰 노드를 먼저 쌓고 작은 노드를 먼저 꺼내기 위함
        for i in reversed(li[node]):
            stack.append(i)
        dfs.append(node)

from collections import deque # deque 자료구조 처리를 위해 import
visit = [False] * (n + 1)
Q = deque([s])

# BFS 큐 생성(deque 사용)
while Q:
    node = Q.popleft() # 방문 노드 처리(큐로 처리하기 위해 왼쪽에서부터 꺼냄)
    if not visit[node]:
        visit[node] = True
        for i in (li[node]):
            Q.append(i)
        bfs.append(node)

for i in dfs:
    print(i, end = ' ')
print()
for i in bfs:
    print(i, end = ' ')