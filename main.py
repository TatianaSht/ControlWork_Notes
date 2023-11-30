import datetime
import json
import sys


def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            my_notes = json.load(file)
    except FileNotFoundError:
        my_notes = []
    return my_notes


def save_notes(my_notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(my_notes, file, indent=4, ensure_ascii=False)


notes = load_notes()


def transition():
    while True:
        agreement = input("Хотите продолжить работу с заметками? Введите Y(да) или N(нет): ")
        if agreement == "Y" or agreement == "y":
            menu_title()
        elif agreement == "N" or agreement == "n":
            print()
            print("Спасибо, что были с нами. До новых встреч!")
            print("""
                  (\___/)
                  (='.'=)
                  (")_(")
            """)
            sys.exit()
        else:
            print("Неверная команда. Попробуйте еще раз.")


def menu_title():
    while True:
        notes_title()

        choice = input("Введите номер команды (число 0-6): ")
        print()
        if choice == "1":
            display_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            display_specific_note()
        elif choice == "4":
            filter_notes_by_date()
        elif choice == "5":
            editing_note()
        elif choice == "6":
            deleting_note()
        elif choice == "0":
            print("Спасибо, что были с нами. До новых встреч!")
            print("""
                (\___/)
                (='.'=)
                (")_(")
            """)
            sys.exit()
        else:
            print("Неверная команда. Попробуйте еще раз.")


def notes_title():
    print()
    glob_title = "Консольное приложение ЗАМЕТКИ"
    print(f"{glob_title:^63}")
    print("=" * 63)
    print("""Доступные команды в приложении:
          [1]  ПРОСМОТР          просмотреть все заметки
          [2]  ДОБАВИТЬ          добавление новой заметки
          [3]  НАЙТИ (id)        поиск заметки по ID
          [4]  НАЙТИ (дата)      поиск заметки по ДАТЕ
          [5]  РЕДАКТИРОВАТЬ     изменение заметки
          [6]  УДАЛИТЬ           удаление заметки
          [0]  ЗАВЕРШИТЬ         завершение работы в приложении
          """)


# Добавление заметки
def add_note():
    if notes:
        last_id = notes[-1]['id']
    else:
        last_id = 0

    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        'id': last_id + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена!")
    print()
    transition()


# Удаление заметки
def deleting_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    print("Удаление заметки с ID: ", note_id)
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            print()
            transition()
            return
    print("Заметка с указанным ID не найдена.")
    print()
    transition()

# Редактирование заметки
def editing_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно изменена.")
            print()
            transition()
            return
    print("Заметка с указанным ID не найдена.")
    print()
    transition()

# Просмотр всех заметок
def display_notes():
    if not notes:
        print("Нет доступных заметок.")
    else:
        print()
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
    print()
    transition()


# Поиск заметок по дате
def filter_notes_by_date():
    date_str = input("Введите дату в формате YYYY-MM-DD: ")
    print("Поиск заметок по дате: ", date_str)
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты!")
        print()
        transition()

    filtered_notes = [note for note in notes if
                      datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == target_date]

    if not filtered_notes:
        print("Заметок на указанную дату нет.")
    else:
        print()
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
    print()
    transition()


# Поиск заметки по ID
def display_specific_note():
    note_id = int(input("Введите ID заметки: "))
    print()
    print("Поиск заметки с ID: ", note_id)
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()
            transition()
    print("Заметка с указанным ID не найдена.")
    print()
    transition()

menu_title()