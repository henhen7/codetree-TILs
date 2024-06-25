storage = []
water = []
count = 0

for _ in range(3):
    s, w = map(int, input().split())
    storage.append(s)
    water.append(w)

# 1 → 2, 2 → 3, 3 → 1 순서로 물을 옮기는 작업을 100번 반복
while (True):
    # 1번 물통에서 2번 물통으로 물 옮기기
    if water[0] + water[1] >= storage[1]:
        move = storage[1] - water[1]
    else:
        move = water[0]
    water[0] -= move
    water[1] += move
    count += 1
    if count == 100:
        break

    # 2번 물통에서 3번 물통으로 물 옮기기
    if water[1] + water[2] >= storage[2]:
        move = storage[2] - water[2]
    else:
        move = water[1]
    water[1] -= move
    water[2] += move
    count += 1
    if count == 100:
        break

    # 3번 물통에서 1번 물통으로 물 옮기기
    if water[2] + water[0] >= storage[0]:
        move = storage[0] - water[0]
    else:
        move = water[2]
    water[2] -= move
    water[0] += move
    count += 1
    if count == 100:
        break
    
# 결과 출력
print(water[0])
print(water[1])
print(water[2])