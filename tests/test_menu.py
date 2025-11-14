from core import menu


def test_choose_category_returns_sport(monkeypatch):
    inputs = iter(["1"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    category = menu.choose_category()

    assert  category == "sport"

def test_choose_category_quit_returns_none(monkeypatch):
    inputs = iter(["q"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    category = menu.choose_category()

    assert category is None

def test_choose_level_light(monkeypatch):
    inputs = iter(["1"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    level = menu.choose_level()
    assert level == "light"

def test_choose_level_hard(monkeypatch):
    inputs = iter(["2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    level = menu.choose_level()

    assert level == "hard"

def test_choose_level_invalid_then_valid(monkeypatch):
    inputs = iter(["хз", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    level = menu.choose_level()

    assert level == "hard"