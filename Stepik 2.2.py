quantity = int(input())
count1, count2, count3, count4 = [0,0,0,0]
for i in range(quantity):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        count1 += 1
    elif x < 0 and y > 0:
        count2 += 1
    elif x < 0 and y < 0:
        count3 += 1
    elif x > 0 and y <0:
        count4 += 1

print(f"Первая четверть: {count1}")
print(f"Вторая четверть: {count2}")
print(f"Третья четверть: {count3}")
print(f"Четвертая четверть: {count4}")



x = list(map(int, input().split()))
count = 0
for i in range(1,len(x)):
    if x[i] > x[i-1]:
        count += 1
print(count)

x = list(map(int, input().split()))
for i in range(0, len(x) - 1, 2):
    x[i], x[i + 1] = x[i + 1], x[i]
print(*x)


x = list(map(int, input().split()))
x.insert(0, x.pop())
print(*x)

x = set(map(int, input().split()))
print(len(x))

l = [int(input()) for n in range(int(input()))]
n = int(input())
res = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] == n:
            res = True
            break

print('ДА' if res == True else 'НЕТ')