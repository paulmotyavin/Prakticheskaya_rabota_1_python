print("Введите число: ") # добавляем сопроводительное сообщение
number_one = int(input()) # реализуем пользовательский ввод для числа
if (number_one > 0): # реализуем условный оператор для числа, если он больше нуля, то прибавляем 1
    number_one = number_one + 1 # прибавляем к числу один
elif (number_one == 0): # реализуем условный оператор для числа, если число равно нулю, то выводится ошибка, т.к. нуль не
    # является ни положительным, ни отрицательным числом.
    print("Ошибка! Введите другое значение числа.") # добавляем сопроводительное сообщение
else: # иначе, если не удовлетворяет первое условие, то число остается неизменным
    number_one = number_one # оставляем неизменным число
print("Результат:", number_one) # реализуем вывод числа