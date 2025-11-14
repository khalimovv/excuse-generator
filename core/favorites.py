import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STORAGE_DIR = BASE_DIR / "storage"
STORAGE_DIR.mkdir(exist_ok=True)

FAV_FILE = STORAGE_DIR / "excuses_favorites.json"


def load_favorites():
    if not FAV_FILE.exists():
        return []
    try:
        data = json.loads(FAV_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_favorites(favorites):
    try:
        FAV_FILE.write_text(
            json.dumps(favorites, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    except OSError:
        print("Не удалось сохранить избранные оправдания.")

def show_favorites():
    favorites = load_favorites()
    if not favorites:
        print("\nУ тебя пока нет избранных оправданий.\n")
        return
    print("\nИзбранные оправдания:")
    for i, item in enumerate(favorites, start=1):
        category = item.get("category", "?")
        level = item.get("level", "?")
        text = item.get("text", "")
        print(f"{i}, [{category}, {level}] {text}")
    print()

def maybe_save_favorite(category: str, level: str, text: str):
    answer = input("Сохранить в избранное? (y/n): ").strip().lower()
    if answer in("y", "д", "да", "yes"):
        favorites = load_favorites()
        favorites.append(
            {
                "category": category,
                "level": level,
                "text": text
            }
        )
        save_favorites(favorites)
        print("Сохранено в избранное.\n")
    else:
     print("Не сохранено в избранное.\n")
