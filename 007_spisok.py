from random import randint

list = []
length = int(input("Длина списка:"))
max = int(input("Максимальное число:"))
for i in range(length):
    list.append(randint(0,max))

print ("Без сортировки:", list)
list.sort()
print ("С сортировкой:", list)



