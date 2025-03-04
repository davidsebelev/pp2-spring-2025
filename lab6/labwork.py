import math
import time
import os
import shutil
import string
from datetime import datetime



# Task B1: Список директорий, файлов и всех объектов в указанном пути.
def list_directories_and_files(path):
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует.")
        return
    directories = []
    files = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)
    print("Список директорий:")
    for d in directories:
        print(" -", d)
    
    print("\nСписок файлов:")
    for f in files:
        print(" -", f)
    
    print("\nСписок всех объектов:")
    for item in os.listdir(path):
        print(" -", item)

# Task B2: Проверка доступа к указанному пути (существование, чтение, запись, выполнение).
def check_access(path):
    print(f"Проверяем путь: {path}")
    if not os.path.exists(path):
        print("Путь не существует.")
        return
    is_readable = os.access(path, os.R_OK)
    is_writable = os.access(path, os.W_OK)
    is_executable = os.access(path, os.X_OK)
    print("Существует: True")
    print("Доступ на чтение:", is_readable)
    print("Доступ на запись:", is_writable)
    print("Доступ на выполнение:", is_executable)

# Task B3: Разбиение пути на директорию и имя файла.
def split_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print("Путь существует.")
        print("Директория:", directory)
        print("Имя файла:", filename)
    else:
        print("Путь не существует.")

# Task B4: Подсчёт количества строк в текстовом файле.
def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Количество строк в файле '{filename}':", len(lines))
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

# Task B5: Запись списка в файл (каждый элемент с новой строки).
def write_list_to_file(lst, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in lst:
            file.write(str(item) + "\n")
    print(f"Список записан в файл '{filename}'.")

# Task B6: Генерация 26 текстовых файлов с именами A.txt, B.txt, ... Z.txt.
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"This is file {filename}")
    print("Файлы от A.txt до Z.txt созданы.")

# Task B7: Копирование содержимого одного файла в другой.
def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
        print(f"Содержимое файла '{src}' успешно скопировано в '{dst}'.")
    except Exception as e:
        print("Ошибка при копировании файла:", e)

# Task B8: Удаление файла по указанному пути с проверкой доступа и существования.
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Файл '{path}' удалён.")
        else:
            print(f"Нет прав для удаления файла '{path}'.")
    else:
        print(f"Файл '{path}' не существует.")


