from setup_db import check_if_db_exists


def test_n_to_recreate_db(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda *args: "n")
    assert check_if_db_exists() == 'Not recreating the database'


def test_y_to_recreate_db(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda *args: "y")
    assert check_if_db_exists() == 'Database recreated'


def test_invalid_input_to_recreate(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda *args: "no")
    assert check_if_db_exists() == 'Invalid answer. Please answer y or n.'
