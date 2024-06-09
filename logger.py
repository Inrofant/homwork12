from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def print_data():
    print('Вывожу данные из первого файла: \n')
    data_first = read_file('data_first_variant.csv')
    print(''.join(data_first))

    print('Вывожу данные из второго файла: \n')
    data_second = read_file('data_second_variant.csv')
    print(''.join(data_second))

def search_record(file_name, search_term):
    lines = read_file(file_name)
    record = []
    found = False
    for line in lines:
        if search_term in line:
            found = True
        if found:
            record.append(line)
            if line.strip() == "":
                break
    return record if record else None

def update_record(var, search_term):
    file_name = 'data_first_variant.csv' if var == 1 else 'data_second_variant.csv'
    lines = read_file(file_name)
    record = search_record(file_name, search_term)
    if record is None:
        print("Запись не найдена")
        return

    print("Текущая запись: ")
    print(''.join(record))

    name = input("Введите новое имя: ")
    surname = input("Введите новую фамилию: ")
    phone = input("Введите новый номер телефона: ")
    address = input("Введите новый адрес: ")

    if var == 1:
        updated_record = [f"{name}\n", f"{surname}\n", f"{phone}\n", f"{address}\n\n"]
    elif var == 2:
        updated_record = [f"{name};{surname};{phone};{address}\n\n"]

    start = lines.index(record[0])
    end = start + len(record)
    lines[start:end] = updated_record

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Запись обновлена")

def delete_record(var, search_term):
    file_name = 'data_first_variant.csv' if var == 1 else 'data_second_variant.csv'
    lines = read_file(file_name)
    record = search_record(file_name, search_term)
    if record is None:
        print("Запись не найдена")
        return

    print("Удаляемая запись: ")
    print(''.join(record))

    start = lines.index(record[0])
    end = start + len(record)
    del lines[start:end]

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Запись удалена")

