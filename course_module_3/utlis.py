import csv
import pandas as pd
import json


def hash_func(user_input_1, user_input_2, user_input_3, filename):
    hash_str = f'{user_input_1}{user_input_2}{user_input_3}'
    with open('hash.json', 'r') as f:
        content = json.load(f)
    if content[0].get(hash_str):
        if content[0][hash_str] != filename:
            with open(content[0][hash_str]) as f:
                data = csv.reader(f)
                with open(filename, 'w') as file:
                    writer = csv.writer(file)
                    for row in data:
                        writer.writerow(row)
            for i in content[0].keys():
                if filename == content[0][i]:
                    content[0].pop(i)
                    break
            content[0][hash_str] = filename
    else:
        for i in content[0].keys():
            if filename == content[0][i]:
                content[0].pop(i)
                break
        content[0][hash_str] = filename
        print('Запуск...')
        select_sorted(user_input_1, user_input_2, user_input_3, filename)
    with open('hash.json', 'w') as f:
        json.dump(content, f)
    print(f'Информация загружена в файл "{filename}"')


def quick_sort(items):
    if len(items) <= 1:
        return items
    elem = items[0][1]
    left = list(filter(lambda x: x[1] < elem, items))
    mid = [i for i in items if i[1] == elem]
    right = list(filter(lambda x: x[1] > elem, items))
    return quick_sort(left) + mid + quick_sort(right)


def select_sorted(sort_columns, order, limit, filename):
    df = pd.read_csv("all_stocks_5yr.csv", sep=',')
    items = list(enumerate(df[sort_columns]))
    print('Сортировка...')
    list_ = quick_sort(items)
    if order == 'asc':
        list_ = list_[: limit]
    else:
        list_ = reversed(list_[-limit:])
    with open(filename, 'w') as f:
        pass
    list_in = [i[0] for i in list_]
    print('Запись...')
    df.iloc[list_in].to_csv(filename, index=False)


def search(list_date, date, list_name=None, name=None):
    low = list_date[0][0]
    high = list_date[-1][0]
    while low <= high:
        mid = (low + high) // 2
        item = list_date[mid][1]
        if item == date:
            list_mid = []
            old_mid = mid
            while list_date[mid][1] == date:
                if list_name is None or list_name[mid][1] == name:
                    list_mid.append(mid)
                mid -= 1
            mid = old_mid
            while list_date[mid][1] == date:
                if list_name is None or list_name[mid][1] == name:
                    list_mid.append(mid)
                if mid >= high:
                    break
                mid += 1
            return list_mid
        if item > date:
            high = mid - 1
        else:
            low = mid + 1
    return None


def get_by_date(date, name, filename):
    if date is None and name is None:
        print('Нет аргументов')
    df = pd.read_csv('all_stocks_5yr.csv', index_col='date', parse_dates=True)
    df = df.sort_index()
    df = df.reset_index()
    if date is not None and name is not None:
        list_date = list(enumerate(df['date']))
        list_name = list(enumerate(df['Name']))
        date = pd.to_datetime(date)
        result = search(list_date, date, list_name, name)
    if date is None and name is not None:
        list_name = list(enumerate(df['Name']))
        result = [i[0] for i in list_name if i[1] == name]
    if date is not None and name is None:
        list_date = list(enumerate(df['date']))
        date = pd.to_datetime(date)
        result = search(list_date, date)
    with open(filename, 'w') as f:
        pass
    if not result:
        print('нет совпадений')
    elif result is not None:
        df.iloc[result].to_csv(filename, index=False)
    else:
        print('нет совпадений')
