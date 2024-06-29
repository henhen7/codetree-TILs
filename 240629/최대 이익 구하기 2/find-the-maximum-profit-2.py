'''
조건
(1) 여러 일은 동시에 할 수 없다.
(2) 태스크는 매일 하나씩 주어진다.
(3) 모든 일은 n일 안에 마무리되어야 한다.

참고 사항
- 일하는 날 / 일 넘기는 날 분리(날마다 하나씩 주어지므로)
- 일 끝나면 보수 누적하고 탐색 시작
- 메모제이션 활용해보기

함수 정의
n = 총 주어진 날짜(아래 줄마다 주어지는 태스크가 순서대로 할당됨)
t, p = 일하는 데 걸리는 날짜, 보수(최대: max_p)
li = (t, p)의 리스트
- 메모제이션 리스트(memo) 초기화: 각 날짜별 최대 이익 저장
- 백트래킹(모든 경우의 수 순회)
'''
n = int(input())
li = []
for i in range(n):
    t, p = map(int, input().split())
    li.append((t, p))

def max_p(n, li):
    memo = [-1] * n # 메모제이션 리스트 초기화
    
    def count(day):
        if day >= n:
            return 0 # n 이상이면 일을 시작할 수 없으므로 보수 0
        
        if memo[day] != -1:
            return memo[day] # 메모제이션 되어 있으면 값 반환
            memo[day] = max(max_p_skip, max_p_work)
        
        # 일 넘기는 날
        max_p_skip = count(day + 1)
        # 보수 저장하지 않고 다음날 탐색(재귀 호출)
        
        # 새 일 시작하는 날
        max_p_work = 0
        if day + li[day][0] <= n:  # 일을 마칠 수 있는 경우에만 새 일 진행
            max_p_work = li[day][1] + count(day + li[day][0])
            # 현재 일의 보수 저장하고 새 일 진행 경우의 수 탐색(재귀 호출)
        
            memo[day] = max(max_p_skip, max_p_work)
        return memo[day]
    
    return count(0)


# 결과 출력
print(max_p(n, li))