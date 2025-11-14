from core import favorites as fav_module

def test_load_favorites_when_file_not_exist_returns_empty_list(tmp_path, monkeypatch):
    test_file = tmp_path / "excuses_favorites.json"
    monkeypatch.setattr(fav_module, "FAV_FILE", test_file)

    favorites = fav_module.load_favorites()

    assert favorites == []

def test_favorites_file_saves_and_loads_correctly(tmp_path, monkeypatch):
    test_file = tmp_path / "excuses_favorites.json"
    monkeypatch.setattr(fav_module, "FAV_FILE", test_file)

    data = [
        {"category": "sport", "level": "light", "text": "тестовое оправдание"}
    ]

    fav_module.save_favorites(data)
    loaded = fav_module.load_favorites()

    assert loaded == data

def test_show_favorites_prints_items(tmp_path, monkeypatch, capsys):
    test_file = tmp_path / "excuses_favorites.json"
    monkeypatch.setattr(fav_module, "FAV_FILE", test_file)

    data = [
        {"category": "life", "level": "hard", "text": "еще одно тестовое ужасное оправдание"}
    ]
    fav_module.save_favorites(data)

    fav_module.show_favorites()
    captured = capsys.readouterr()

    assert "Избранные оправдания" in captured.out
    assert "еще одно тестовое ужасное оправдание" in captured.out
