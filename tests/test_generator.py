from core.generator import generate_excuse
from data.excuses import EXCUSES

def test_generate_excuse_valid_category_and_level():
    category = "sport"
    level = "light"

    excuse = generate_excuse(category, level)

    assert isinstance(excuse, str)
    assert excuse != ""
    assert excuse in EXCUSES[category][level]

def test_generate_excuse_with_unknown_category_returns_default_message():
    excuse = generate_excuse("unknown_category", "light")
    assert "Кажется, у меня нет оправданий на такой случай. Это уже прогресс." in excuse
