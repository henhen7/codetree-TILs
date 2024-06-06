n, m = map(int, input().split())

# 노드의 총 개수가 n개 주어지므로, 행이 n + 1개인 인접 리스트 생성
# 노드가 1번부터 시작하므로, 계산의 용이성을 위해 1번 행부터 시작
li = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b) # a번 노드와 b번 노드가 연결이므로, a번 행에 b값 추가
    li[b].append(a) # (당연히 양방향 연결이니까) b번 행에 a값 추가

# 스택을 사용하여 해결하는 방법
# 방문 처리를 위한 리스트 생성(n + 1개: 노드 번호에 맞추려고.., default = False)
visit = [False] * (n + 1)
# 1번 노드부터 시작하므로 스택에 추가
stack = [1]
count = 0 # 연결 노드 수

while stack:
    node = stack.pop() # 방문 노드(스택에서 제거한 원소)
    if not visit[node]: 
        visit[node] = True # 방문 리스트가 False인 경우, 방문 처리
        for i in li[node]: # 방문 노드 내의 원소를 돌면서, 방문 확인
            if not visit[i]:
                # 방문 처리 안 된 노드인 경우, 스택에 해당 원소를 쌓음
                # 스택 리스트에서 노드가 다 빠질 때까지 반복문을 돌면서 방문 처리 및 확인
                stack.append(i) 
        if node != 1: # 현재 방문한 노드가 1번이 아니면, 연결 노드 수 1 추가
            count += 1 

print(count)