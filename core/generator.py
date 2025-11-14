import random
from data.excuses import EXCUSES

def generate_excuse(category: str, level: str) -> str:
    """Вернуть случайное оправдание по категории и уровню абсурда"""
    options = EXCUSES.get(category, {}).get(level, [])
    if not options:
        return "Кажется, у меня нет оправданий на такой случай. Это уже прогресс."
    return random.choice(options)
