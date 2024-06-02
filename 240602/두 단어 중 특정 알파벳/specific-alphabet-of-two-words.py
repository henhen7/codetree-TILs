from collections import defaultdict

n = int(input())
pair = [input().split() for i in range(n)] 
# 리스트 내에 공백을 기준으로 split하는 2차원 배열을 n만큼 반복문 돌면서 추가

mcount = defaultdict(int) # 유사 딕셔너리 생성: 지정하지 않은 key -> int 0으로 출력
    
for a, b in pair:
    count_a = defaultdict(int) # 단어 a 개수 세는 딕셔너리 생성
    count_b = defaultdict(int) # 단어 b 개수 세는 딕셔너리
        
    for i in a: # 단어 a를 1자리씩 돌면서 딕셔너리에 알파벳 추가
        count_a[i] += 1
    for i in b:
        count_b[i] += 1
        
    for i in 'abcdefghijklmnopqrstuvwxyz': # 전체 딕셔너리 생성해서 최댓값 저장
        mcount[i] += max(count_a[i], count_b[i])
    
for i in 'abcdefghijklmnopqrstuvwxyz':
    print(mcount[i])