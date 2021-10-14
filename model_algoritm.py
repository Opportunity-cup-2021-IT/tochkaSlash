# Задаём функцию, которая будет добавлять в хранилище всех перенесённых работ их номер и время сдвига
def func(id_shift, shift_time):

    # добавляем глобальную переменную стоимости переноса, чтобы работать напрямую
    global shift_cost

    # для каждой связанной с переданной работой работы
    for id_connected_work in a[id_shift - 1]["post"]:

        # задаём резерв между концом переданной работы и началом связанной
        reserve = a[id_connected_work - 1]["start"] - a[id_shift - 1]["end"]

        if (shift_time) > reserve:

            # проверяем: не добавлялась ли работа в хранилище всех перенесённых работ  -
            # иначе нет смысла считать стоимость её переноса 2ой раз
            if (id_connected_work not in all_shifted_works):
                # добавляем связанную работу в хранилище всех перенесённых работ
                # со значением выхода за временные рамки резерва
                all_shifted_works[id_connected_work] = shift_time - reserve

                # Проверяем: веха ли связанная работа или нет, и добавляем в стоимость переноса
                # стоимость переноса связанной работы
                if a[id_connected_work - 1]["duration"] != 0:
                    shift_cost += 1
                elif a[id_connected_work - 1]["duration"] == 0:
                    shift_cost += 1000


            # меняем значение сдвига связанной работы в хранилище всех перенесённых работ на наибольшее значение выхода
            # за временные рамки резерва
            if (all_shifted_works[id_connected_work] < (shift_time - reserve)):
                all_shifted_works[id_connected_work] = shift_time - reserve

            # образуем рекурсию
            func(id_connected_work, (shift_time - reserve))


#  Вводим данные работ
work1 = {"ID": 1, "start": 1577836800, "end": 1578268800, "post": [2, 3, 4]}
#Wed, 01 Jan 2020 00:00:00 - Mon, 06 Jan 2020 00:00:00

work2 = {"ID": 2, "start": 1579132800, "end": 1579305600, "post": [5]}
# Thu, 16 Jan 2020 - Sat, 18 Jan 2020

work3 = {"ID": 3, "start": 1578787200, "end": 1579046400, "post": [5]}
# Sun, 12 Jan 2020 - Wed, 15 Jan 2020

work4 = {"ID": 4, "start": 1578355200, "end": 1579132800, "post": [8]}
# Tue, 07 Jan 2020 - Thu, 16 Jan 2020

work5 = {"ID": 5, "start": 1579305600, "end": 1579305600, "post": [6, 7]}
# Sat, 18 Jan 2020 - Sat, 18 Jan 2020

work6 = {"ID": 6, "start": 1579305600, "end": 1578268800, "post": [9]}
# Sat, 18 Jan 2020 -  Wed, 22 Jan 2020

work7 = {"ID": 7, "start": 1579305600, "end": 1579824000, "post": [9]}
# Sat, 18 Jan 2020 - Fri, 24 Jan 2020

work8 = {"ID": 8, "start": 1579478400, "end": 1579478400, "post": [9]}
# Mon, 20 Jan 2020 - Mon, 20 Jan 2020

work9 = {"ID": 9, "start": 1579910400, "end": 1580256000, "post": []}
# Sat, 25 Jan 2020 - Wed, 29 Jan 2020


# делаем массив работ для удобного обращения к ним, а также в свойства каждой работы добавляем её длительность
a = [work1, work2, work3, work4, work5, work6, work7, work8, work9]
for work in a:
    work["duration"] = work["end"] - work["start"]


# Запрашиваем номер сдвинутой работы и время сдвига в днях
id_shifted_work = int(input('Введите номер сдвинутой работы: '))
shift_time = int(input('Введите количество дней сдвига: '))

# Переводим время в днях в unixtime
shift_time = shift_time * 86400

# Значение потери по умолчанию равен стоимости переноса запрошенной работы
if a[id_shifted_work - 1]["duration"] != 0:
    shift_cost = 1
else:
    shift_cost = 1000

# Определяем хранилище всех перенесённых работ и добавляем туда запрошенную работу и время её сдвига
all_shifted_works = {}
all_shifted_works[id_shifted_work] = shift_time

# начинаем просчёт
func(id_shifted_work, shift_time)

# Если программа вызывается непосредственно, то выводим стоимость переноса и id работ
if __name__ == "__main__":
    for elem in all_shifted_works:
        print(f"Работа {elem} перенесётся на {int(all_shifted_works[elem] / 86400)} дня/дней")

    print(f'\n***Стоимость всех переносов {shift_cost} рубля/рублей***')

# если программа вызывается визуализатором, то определяем массив id перенесённых работ
else:
    shifted_ids = []
    for key in list(all_shifted_works.keys()):
        shifted_ids.append(key)