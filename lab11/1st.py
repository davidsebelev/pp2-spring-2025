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


def create_db_objects():
    """Создает функции и процедуры в базе данных."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE OR REPLACE FUNCTION f_search_phonebook(p_pattern text)
    RETURNS TABLE(id int, name text, phone text) AS $$
    BEGIN
      RETURN QUERY
        SELECT id, name, phone
        FROM phonebook
        WHERE name ILIKE '%' || p_pattern || '%'
           OR phone ILIKE '%' || p_pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """)
    cur.execute("""
    CREATE OR REPLACE PROCEDURE sp_upsert_phonebook_user(p_name text, p_phone text)
    LANGUAGE plpgsql AS $$
    BEGIN
      IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
      ELSE
        INSERT INTO phonebook(name, phone) VALUES(p_name, p_phone);
      END IF;
    END;
    $$;
    """)
    cur.execute("DROP TYPE IF EXISTS phone_error;")
    cur.execute("CREATE TYPE phone_error AS (name text, phone text);")
    cur.execute("""
    CREATE OR REPLACE FUNCTION f_insert_many_phonebook_users(p_names text[], p_phones text[])
    RETURNS SETOF phone_error AS $$
    DECLARE
      arr_length int;
      i int;
      err_rec phone_error;
      valid_pattern text := '^\d{3}-\d{3}-\d{4}$';
    BEGIN
      arr_length := array_length(p_names, 1);
      IF arr_length IS NULL THEN
         RETURN;
      END IF;
      
      FOR i IN 1..arr_length LOOP
        IF p_phones[i] !~ valid_pattern THEN
          err_rec.name := p_names[i];
          err_rec.phone := p_phones[i];
          RETURN NEXT err_rec;
        ELSE
          IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_names[i]) THEN
            UPDATE phonebook SET phone = p_phones[i] WHERE name = p_names[i];
          ELSE
            INSERT INTO phonebook(name, phone) VALUES (p_names[i], p_phones[i]);
          END IF;
        END IF;
      END LOOP;
      RETURN;
    END;
    $$ LANGUAGE plpgsql;
    """)
    cur.execute("""
    CREATE OR REPLACE FUNCTION f_get_phonebook_page(p_limit int, p_offset int)
    RETURNS TABLE(id int, name text, phone text) AS $$
    BEGIN
      RETURN QUERY 
        SELECT id, name, phone
        FROM phonebook
        ORDER BY id
        LIMIT p_limit OFFSET p_offset;
    END;
    $$ LANGUAGE plpgsql;
    """)
    cur.execute("""
    CREATE OR REPLACE PROCEDURE sp_delete_phonebook(p_identifier text)
    LANGUAGE plpgsql AS $$
    BEGIN
      DELETE FROM phonebook WHERE name = p_identifier OR phone = p_identifier;
    END;
    $$;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Объекты базы данных (функции и процедуры) созданы.")

def call_f_search_phonebook():
    pattern = input("Введите шаблон для поиска: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM f_search_phonebook(%s)", (pattern,))
    results = cur.fetchall()
    if results:
        print("Результаты поиска по шаблону:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Записей не найдено.")
    cur.close()
    conn.close()

def call_sp_upsert_phonebook_user():
    name = input("Введите имя для upsert: ").strip()
    phone = input("Введите телефон: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL sp_upsert_phonebook_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Upsert выполнен.")

def call_f_insert_many_phonebook_users():
    names = input("Введите имена, разделенные запятой: ").split(',')
    phones = input("Введите телефоны, разделенные запятой: ").split(',')
    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM f_insert_many_phonebook_users(%s, %s)", (names, phones))
    errors = cur.fetchall()
    if errors:
        print("Найдены некорректные телефоны:")
        for err in errors:
            print(f"Имя: {err[0]}, Телефон: {err[1]}")
    else:
        print("Все контакты вставлены корректно.")
    conn.commit()
    cur.close()
    conn.close()

def call_f_get_phonebook_page():
    try:
        limit = int(input("Введите лимит (кол-во записей): ").strip())
        offset = int(input("Введите смещение: ").strip())
    except ValueError:
        print("Лимит и смещение должны быть числами.")
        return
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM f_get_phonebook_page(%s, %s)", (limit, offset))
    results = cur.fetchall()
    if results:
        print("Страница записей:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Нет записей для данной страницы.")
    cur.close()
    conn.close()

def call_sp_delete_phonebook():
    identifier = input("Введите имя или телефон для удаления: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL sp_delete_phonebook(%s)", (identifier,))
    conn.commit()
    cur.close()
    conn.close()
    print("Записи удалены (если были найдены).")

def menu():
    create_table() 
    while True:
        print("\n=== Телефонная книга ===")
        print("0. Создать объекты БД (функции и процедуры)")
        print("1. Загрузить данные из CSV файла")
        print("2. Добавить контакт через консоль")
        print("3. Обновить данные контакта")
        print("4. Поиск контакта")
        print("5. Удалить контакт (по имени)")
        print("6. Поиск по шаблону (функция f_search_phonebook)")
        print("7. Upsert контакта (процедура sp_upsert_phonebook_user)")
        print("8. Пакетная вставка с проверкой телефона (функция f_insert_many_phonebook_users)")
        print("9. Пагинация записей (функция f_get_phonebook_page)")
        print("10. Удаление контакта по имени или телефону (процедура sp_delete_phonebook)")
        print("11. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            create_db_objects()
        elif choice == "1":
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
            call_f_search_phonebook()
        elif choice == "7":
            call_sp_upsert_phonebook_user()
        elif choice == "8":
            call_f_insert_many_phonebook_users()
        elif choice == "9":
            call_f_get_phonebook_page()
        elif choice == "10":
            call_sp_delete_phonebook()
        elif choice == "11":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
