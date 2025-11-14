from core.menu import choose_category, choose_level
from core.generator import generate_excuse
from core.favorites import maybe_save_favorite
from core.constants import (APP_TITLE,APP_SUBTITLE,GOODBYE_MSG,
                            EXCUSE_TITLE,ANOTHER_ONE_EXCUSE,NO_MORE_MSG)

def main():
    print(APP_TITLE)
    print(APP_SUBTITLE)

    while True:
        category = choose_category()
        if category is None:
            print("\n" + GOODBYE_MSG)
            break

        level = choose_level()
        excuse = generate_excuse(category, level)

        print("\n" + EXCUSE_TITLE)
        print(f">{excuse}\n")

        maybe_save_favorite(category, level, excuse)

        cont = input(ANOTHER_ONE_EXCUSE).strip().lower()
        if cont not in("y", "д", "да", "yes"):
            print("\n" + NO_MORE_MSG)
            break

if __name__  == "__main__":
    main()