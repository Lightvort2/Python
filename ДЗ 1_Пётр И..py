### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты:
# <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

print('Задание 1')
dur = int(input('duration = '))
days = dur // 86400 % 30
hours = dur // 3600 % 24
minutes = dur // 60 % 60
seconds = dur % 60
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)

print('Задание 2')
cubic_x = [x**3 for x in range(1, 1001, 2)]

# 2.1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

sum_of_numbers = 0
sum_of_numbers_list = []

for s in range(len(cubic_x)):
    str_2 = str(cubic_x[s])
    list_2 = list(str_2)
    for s in range(len(list_2)):
        list_2[s] = int(list_2[s])
    for s in range(len(list_2)):
        sum_of_numbers = sum_of_numbers + list_2[s]
    if sum_of_numbers % 7 == 0:
        sum_of_numbers_list.append(sum_of_numbers)

print('Задание 2.1. - список чисел, сумма которых делится на 7: ', sum_of_numbers_list)
print('Задание 2.1. - сумма чисел из списка = ', sum(sum_of_numbers_list))

# 2.2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

cubic_x = [(x**3)+17 for x in range(1, 1001, 2)]

sum_of_numbers = 0
sum_of_numbers_list_17 = []

for s in range(len(cubic_x)):
    str_2 = str(cubic_x[s])
    list_2 = list(str_2)
    for s in range(len(list_2)):
        list_2[s] = int(list_2[s])
    for s in range(len(list_2)):
        sum_of_numbers = sum_of_numbers + list_2[s]
    if sum_of_numbers % 7 == 0:
        sum_of_numbers_list_17.append(sum_of_numbers)

print('Задание 2.2. - новый список чисел, сумма которых делится на 7: ', sum_of_numbers_list_17)
print('Задание 2.2. - сумма чисел из нового списка = ', sum(sum_of_numbers_list_17))

# 3. Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100

print('Задание 3')
for w in range(100):
    str_3 = str(w+1)
    list_3 = list(str_3)
    if int(list_3[-1]) == 1 and w + 1 != 11:
        print('{} процент'.format(w + 1))
    elif int(list_3[-1]) > 1 and int(list_3[-1]) <= 4:
        if w + 1 > 10 and w + 1 <= 14:
            print('{} процентов'.format(w + 1))
        else:
            print('{} процента'.format(w + 1))
    else:
        print('{} процентов'.format(w + 1))