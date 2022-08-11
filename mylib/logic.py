import wikipedia


def wiki(name="War Goddess", length=1):

    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki

def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """Returns phrases from wikipedia"""

    # page = wiki(name)
    # blob = TextBlob(page)
    pass