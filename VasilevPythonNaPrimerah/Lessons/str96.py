#Пользователь вводит значение
res = eval(input("Введите что-нибудь : "))
#Тип значения запоминаем в переменной
resType = type(res)
#используем условные операторы (упрощенная форма)
#для проверки типа введенного пользователя значения
if resType ==int :
    #Если целое число
    print("Это целое число! ")
elif resType == float:
    #Ечли действительное число
    print("Это действительное число!")
else:
    #если не число
    print("Наверное  это текст!")
print("работа завершена!")