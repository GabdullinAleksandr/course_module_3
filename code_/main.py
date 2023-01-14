from utlis import hash_func


def main():
    print('Сортировать по цене')
    user_input_1 = input('открытия (1)\n'
                         'закрытия (2)\n'
                         'максимум [3]\n'
                         'минимум (4)\n'
                         'объем (5)\n')
    user_input_2 = input('Порядок по убыванию [1] / возрастанию (2) - ')
    user_input_3 = input('Ограничение выборки [10] - ')
    user_input_4 = input('Название файла для сохранения результата [dump.csv] - ')
    user_input_1 = 3 if user_input_1 == '' else int(user_input_1)
    user_input_2 = 1 if user_input_2 == '' else int(user_input_2)
    user_input_3 = 10 if user_input_3 == '' else int(user_input_3)
    user_input_4 = 'dump.csv' if user_input_4 == '' else str(user_input_4)
    match user_input_1:
        case 1:
            user_input_1 = 'open'
        case 2:
            user_input_1 = 'close'
        case 3:
            user_input_1 = 'high'
        case 4:
            user_input_1 = 'low'
        case 5:
            user_input_1 = 'volume'
        case _:
            print("incorrect input")
            quit()
    if user_input_2 == 1:
        user_input_2 = 'desc'
    else:
        user_input_2 = 'asc'

    hash_func(user_input_1, user_input_2, user_input_3, user_input_4)
    print('Готово!')


if __name__ == '__main__':
    main()
