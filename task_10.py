user = {
    "id": 8,
    "last_name": "Р.",
    "first_name": "Петро",
    "group": "ІПЗс-22-2",
    "books": [],
    "books_history": [],
}


def print_user():
    title = f"=== КАРТА ЧИТАЧА №{user["id"]} ==="
    print(title)
    print(user["first_name"], user["last_name"])
    print(user["group"])
    print("Книги в використанні:", ", ".join(user["books"]) if len(user["books"]) > 0 else "(Пусто)")
    print("Історія користування книгами:",
          ", ".join(user["books_history"]) if len(user["books_history"]) else "(Пусто)")
    print("=" * len(title))


while True:
    print("""
1. Переглянути картку читача
2. Взяти книгу
3. Повернути книгу
0. Вихід""".lstrip())

    option = input(">>> ").strip()

    match option:
        case "0":
            break
        case "1":
            print_user()
        case "2":
            book_name = input("Назва книги: ").strip()
            if book_name not in user["books"]:
                user["books"].append(book_name)
                print(f'Ви взяли книгу "{book_name}" з бібліотеки')
            else:
                print("Книга вже в використанні")
        case "3":
            book_name = input("Назва книги: ").strip()
            if book_name in user["books"]:
                user["books"].remove(book_name)
                user["books_history"].append(book_name)
                print(f'Книга "{book_name}" повернута в бібліотеку')
            else:
                print("У вас не має такої книги")