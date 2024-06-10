from collections import deque
s = int(input())
def char(s):
    # 큐 생성: (화면 문자 카운트, 클립보드 문자 카운트, 연산 카운트)
    Q = deque([(1, 0, 0)]) # 초기 화면에 문자 1개
    visit = [(1, 0)] # 화면, 클립보드 방문 리스트

    while Q:
        screen, clipboard, count = Q.popleft()

        if screen == s:
            return count

        # 복사
        if (screen, screen) not in visit: # screen의 값을 클립보드에 복사하므로 클립보드의 값도 screen
            visit.append((screen, screen))
            Q.append((screen, screen, count + 1))

        # 붙여넣기
        if clipboard > 0 and (screen + clipboard, clipboard) not in visit:
            visit.append((screen + clipboard, clipboard))
            Q.append((screen + clipboard, clipboard, count + 1))

        # 삭제
        if screen > 1 and (screen - 1, clipboard) not in visit:
            visit.append((screen - 1, clipboard))
            Q.append((screen - 1, clipboard, count + 1))

print(char(s))