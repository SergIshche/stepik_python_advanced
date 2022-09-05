a = 3
b = 8

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)


def imt_function(weight: float, height: float) -> str:
    imt = weight / (height ** 2)
    if imt < 18.5:
        print("Недостаточная масса")
    elif imt >= 18.5 and imt <= 25:
        print("Оптимальная масса")
    else:
        print("Избыточная масса")


imt_function(65, 1.75)

check_stroke = "Тимур - лучший математик на свете!!"
# print(len(check_stroke))
# price = len(check_stroke)*60
# print(price)
# price = str(price)
# print(f"{price[0:-2]} р. {price[-2:]} коп.")

price = (len(check_stroke)*60)
price_rub = price//100
price_kop = price%100
print(f"{price_rub} р. {price_kop} коп.")

print(check_stroke.count(" ")+1)

print(len(check_stroke.split()))

year = 2655
animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

b = (year - 8) - (year//12)* 12
print(animals[b])

s = input()
print(int(s[:-5] + s[-5:][::-1]))

