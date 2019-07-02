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

#Задача Hard - на скорую руку. Я понимаю, что тут лучше использовать словарь, но не успел разобраться

name = input('Ваши имя и фамилия: ')
while len(name) < 2:
    print('Введите пожалуйста Имя и Фамилию')
    name = input('Ваши имя и фамилия: ')

age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

med_data = []
med_data.append([name, age, weight])

if age < 30 and weight > 50 < 120:
    print('Уважаемый {}, {} год, вес {}'.format(med_data[0][0], med_data[0][1], med_data[0][2]),' - хорошее состояние')
elif age > 40 and weight < 50 or weight > 120:
    print('Уважаемый {}, {} год, вес {}'.format(med_data[0][0], med_data[0][1], med_data[0][2]),' - следует обратится к врачу!')
elif age > 30 and weight < 50 or weight > 120:
    print('Уважаемый {}, {} год, вес {}'.format(med_data[0][0], med_data[0][1], med_data[0][2]),' - следует заняться собой')
else: print('Уважаемый {}, {} год, вес {}'.format(med_data[0][0], med_data[0][1], med_data[0][2]),' - Вы не в нашей компетенции')
