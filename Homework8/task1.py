# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os
os.system('cls')

filename = 'guide.txt'

def add_tel(): #запись в файл (и создание файла, если его нет)
    data = [
        input("Введите фамилию: "),
        input("Введите имя: "),
        input("Введите отчество: "),
        input("Введите номер телефона: "),
    ]
    st = " ".join(data)
    with open(filename, "a", encoding='utf-8') as write_file:
        write_file.write(st+'\n')
        print('Номер записан')
    write_file.close
    return

def get_guide(): #чтение из файла
    with open(filename,'r', encoding='utf-8') as read_file:
    #read_file = open('guide.txt','r')
        for line in read_file:
            print(line)
    read_file.close
    return

def find_cont(): #поиск контакта
    s_name = input("Введите фамилию: ")
    with open(filename,'r', encoding='utf-8') as find_file:
        for line in find_file:
            if s_name in line:
                print(line)
                find_file.close
                return           
    print("В справочнике отсутствует такой человек!")
    find_file.close
    return

def import_cont(): #импорт контакта в файл (Домашнее задание)
    s_name = input("Введите фамилию: ")
    with open(filename,'r', encoding='utf-8') as find_file:
        for line in find_file:
            if s_name in line:
                print(f"Найден контакт: {line}")
                find_file.close
                with open('import.txt', "a", encoding='utf-8') as write_file:
                    write_file.write(line+'\n')
                    print('Контакт импортирован!')
                    write_file.close
                return           
    print("Контакт отсутствует, импорт не состоялся!")
    find_file.close
    return

def menu():
    dct = {
        "cr": 'Добавить запись (введите "cr")',
        "sh": 'Вывести справочник (введите "sh")',
        "fn": 'Найти запись (введите "fn")',
        "im": 'Импорт контакта (введите "im")',
        "ex": 'Выйти из программы (введите "ex")',
    }
    print("-", dct["cr"])
    print("-", dct["sh"])
    print("-", dct["fn"])
    print("-", dct["im"])
    print("-", dct["ex"])
    
    cmd = input()
    if cmd not in dct:
        print("Такой команды нет, выбирите другую")
        return -1
    else:
        return cmd
    
while True:
    cmd = menu()
    if cmd == "cr":
        add_tel()
    elif cmd == "sh":
        get_guide()
    elif cmd == "fn":
        find_cont()
    elif cmd == "im":
        import_cont()         
    else:
        exit()
    input('Нажмите enter, чтобы продолжить')