ticket = int(input('Введите количество билетов которе желаете приобрести (от 1 до 100): '))
discount = ticket
list_age = []           # пустой список
count1 = 0              # счетчик от 18 до 25
count2 = 0              # счетчик от 26
if ticket <= 0:         #проверка на корректность ввода
    ticket = int(input('Введите корректное количество билетов от 1 до 100: ')) 

for i in range(ticket):
    list_age = list(map(int,input('Введите возраст учасника онлайн - конференции: ').split()))    # записываем возраст в список
    for j in list_age:          # проходим по списку сравниваем возраст
        if j < 18:
            print('Лица до 18 лет проходят бесплатно.')
        elif 18 <= j <= 25:
            count1 += 990
        else:
            count2 += 1390
if discount > 3:
    discount = int((count1 + count2) * 10 / 100)    # считаем дисконт
    print('Итого к оплате, с учетом скидки 10%:', (count1 + count2) - discount,'руб.')
else:
    print('Итого к оплате:',count1 + count2,'руб.')


        
