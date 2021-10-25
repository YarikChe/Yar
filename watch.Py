sec = int(input("Введите секунды:\n"))
h = sec//3600
m = sec%3600//60
c = sec%60

print(str(h) + "час. " + str(m) + "мин. " + str(c) + "сек. ")