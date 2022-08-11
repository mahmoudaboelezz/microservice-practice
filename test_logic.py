from mylib.logic import wiki, search_wiki, phrase


def test_wiki():
    assert "Ahmed Hassan Zewail" in wiki("Ahmed Zewail")

def test_search_wiki():
    assert "Ahmed Hassan Zewail" in search_wiki("Ahmed Zewail")
    
def test_phrase():
    assert "Ahmed Hassan Zewail" in phrase("Ahmed Zewail")
