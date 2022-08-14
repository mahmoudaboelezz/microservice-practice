from mylib.logic import wiki, search_wiki


def test_wiki():
    assert "Ahmed Hassan Zewail" in wiki("Ahmed Zewail")


def test_search_wiki():
    assert "Ahmed Hassan Zewail" in search_wiki("Ahmed Zewail")


