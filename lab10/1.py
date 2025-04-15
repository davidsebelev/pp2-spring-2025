import psycopg2
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def connect():
    return psycopg2.connect(
        dbname="phonebook_db",    
        user="postgres",          
        password="2106",    
        host="localhost"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица phonebook создана.")


def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  
            for row in reader:
                if len(row) >= 2:  
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", row[:2])
                else:
                    print("Неверный формат строки:", row)
        conn.commit()
        print("Данные из CSV успешно загружены.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
    finally:
        cur.close()
        conn.close()


def insert_from_console():
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    if not name or not phone:
        print("Имя и номер телефона не могут быть пустыми!")
        return
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт успешно добавлен.")


def update_contact():
    print("Выберите, что хотите обновить:")
    print("1. Изменить номер телефона")
    print("2. Изменить имя контакта")
    choice = input("Ваш выбор (1/2): ").strip()
    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Введите имя контакта, у которого изменяется номер: ").strip()
        new_phone = input("Введите новый номер телефона: ").strip()
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    elif choice == "2":
        old_name = input("Введите текущее имя контакта: ").strip()
        new_name = input("Введите новое имя контакта: ").strip()
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    else:
        print("Неверный выбор!")
        cur.close()
        conn.close()
        return

   
    if cur.rowcount == 0:
        print("Контакт не найден или данные не изменились.")
    else:
        print("Данные обновлены.")
    conn.commit()
    cur.close()
    conn.close()


def search_contact():
    print("Выберите тип поиска:")
    print("1. По точному совпадению имени")
    print("2. По части имени (LIKE)")
    choice = input("Ваш выбор (1/2): ").strip()
    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Введите полное имя для поиска: ").strip()
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        part = input("Введите часть имени для поиска: ").strip()
        # ILIKE - нечувствительный к регистру поиск
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + part + '%',))
    else:
        print("Неверный выбор!")
        cur.close()
        conn.close()
        return

    results = cur.fetchall()
    if results:
        print("Найденные контакты:")
        for row in results:
            print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    else:
        print("Контакты не найдены.")
    cur.close()
    conn.close()


def delete_contact():
    name = input("Введите имя контакта, который хотите удалить: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    if cur.rowcount == 0:
        print("Контакт не найден!")
    else:
        print("Контакт удалён.")
    conn.commit()
    cur.close()
    conn.close()


def menu():
    create_table() 
    while True:
        print("\n=== Телефонная книга ===")
        print("1. Загрузить данные из CSV файла")
        print("2. Добавить контакт через консоль")
        print("3. Обновить данные контакта")
        print("4. Поиск контакта")
        print("5. Удалить контакт")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            filename = input("Введите имя CSV файла (например, contacts.csv): ").strip()
            insert_from_csv(filename)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
