n, m, s = map(int, input().split())
li = [[] for _ in range(n + 1)]

# 인접 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a) 

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
        # 해당 노드에 연결된 노드의 리스트를 역순으로 정렬
        # 이후 스택처리를 할 때 큰 노드를 먼저 쌓고 작은 노드를 먼저 꺼내기 위함
        li[node].reverse() 
        for i in (li[node]):
            stack.append(i)
        dfs.append(node)

from collections import deque # deque 자료구조 처리를 위해 import
visit = [False] * (n + 1)
deque = deque([s])

# BFS 큐 생성(deque 사용)
while deque:
    node = deque.popleft() # 방문 노드 처리(큐로 처리하기 위해 왼쪽에서부터 꺼냄)
    if not visit[node]:
        visit[node] = True
        # li를 다시 원래 순서로 재정렬(DFS에서 역순으로 돌려놔서...)
        li[node].reverse() 
        for i in (li[node]):
            deque.append(i)
        bfs.append(node)

for i in dfs:
    print(i, end = ' ')
print()
for i in bfs:
    print(i, end = ' ')