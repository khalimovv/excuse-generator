from core.favorites import show_favorites
from core.constants import (CATEGORY_OPTIONS,
                            MENU_CATEGORY_TITLE,
                            MENU_LEVEL_TITLE,
                            LEVEL_OPTIONS,
                            INVALID_INPUT_CATEGORY,
                            INVALID_INPUT_LEVEL,
                            EXIT_CHOICES


                            )

def choose_category():
    categories = CATEGORY_OPTIONS
    while True:
        print(MENU_CATEGORY_TITLE)
        for key, (code, label) in categories.items():
                print(f"{key}, {label}")
        print("6. Показать избранные")
        print("q. Выйти\n")

        choice = input("Твой выбор: ").strip().lower()

        if choice in EXIT_CHOICES:
            return None

        if choice == "6":
            show_favorites()
            continue

        if choice in categories:
            return categories[choice][0]
        print(INVALID_INPUT_CATEGORY)

def choose_level():
    while True:
        print(MENU_LEVEL_TITLE)
        for line in LEVEL_OPTIONS:
            print(line)

        choice = input("Твой выбор: ").strip()
        if choice == "1":
            return "light"
        if choice == "2":
            return "hard"

        print(INVALID_INPUT_LEVEL)