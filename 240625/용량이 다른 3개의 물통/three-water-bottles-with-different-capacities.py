# 입력 받기
capacity = []
water = []

for _ in range(3):
    c, w = map(int, input().split())
    capacity.append(c)
    water.append(w)

# 1 → 2, 2 → 3, 3 → 1 순서로 물을 옮기는 작업을 100번 반복
for _ in range(100):
    # 1번 물통에서 2번 물통으로 물 옮기기
    transfer = min(water[0], capacity[1] - water[1])
    water[0] -= transfer
    water[1] += transfer

    # 2번 물통에서 3번 물통으로 물 옮기기
    transfer = min(water[1], capacity[2] - water[2])
    water[1] -= transfer
    water[2] += transfer

    # 3번 물통에서 1번 물통으로 물 옮기기
    transfer = min(water[2], capacity[0] - water[0])
    water[2] -= transfer
    water[0] += transfer

# 결과 출력
print(water[0])
print(water[1])
print(water[2])