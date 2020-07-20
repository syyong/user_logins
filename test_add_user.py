from add_user import add_user, return_user


def test_add_eli_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda *args: "Eli")
    assert return_user() == "Eli"
