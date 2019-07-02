#Задача №1
number = input('Введите данные ')

number = int(number)
while number < 0 or number > 10:
    print('Введите правильно значение - от 0 до 10')
    number = int(input('Введите данные '))
if number > 0 and number < 10:
    print('Число в степени 2 = ', number**2)
else: print('Пусто :(')

# Задача №2

number1 = int(input('Введите первое значение '))
number2 = int(input('Введите второе значение '))

number1, number2 = number2, number1

print(number1)
print(number2)