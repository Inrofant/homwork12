from logger import input_data, print_data, update_record, delete_record

def interface():
    while True:
        print("Добрый день! вы попали на специальный бот!")
        print("1 - Запись данных")
        print("2 - Вывод данных")
        print("3 - Изменение данных")
        print("4 - Удаление данных")
        print("5 - Выход")
        command = int(input('Введите число: '))

        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            var = int(input("Введите вариант (1 или 2): "))
            search_term = input("Введите имя или фамилию для поиска записи: ")
            update_record(var, search_term)
        elif command == 4:
            var = int(input("Введите вариант (1 или 2): "))
            search_term = input("Введите имя или фамилию для поиска записи: ")
            delete_record(var, search_term)
        elif command == 5:
            print("Выход из программы.")
            break
        else:
            print("Неправильный ввод. Попробуйте снова.")
