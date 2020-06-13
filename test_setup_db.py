# import unittest.mock

from setup_db import check_if_db_exists


def test_yes_to_recreate_db(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda *args: "y")
    assert check_if_db_exists() == 'yes, recreate'
