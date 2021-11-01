a = int(input("Ввелите сумму денег : " ))
y = int(input("Введите количество лет :"))

i=1
while i <= y :
	y-=1
	a= a+a/10
print(a)