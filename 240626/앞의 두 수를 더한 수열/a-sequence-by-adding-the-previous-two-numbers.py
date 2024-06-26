n = int(input())

li = [0, 1]
def func(n):
    while True:
        for i in range(len(li)):
            li.append(li[len(li) - 2] + li[len(li) - 1])
            if i == n:
                return li[n]


print(func(n))