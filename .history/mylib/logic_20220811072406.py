import imp


import wikipedia


def wiki(name="War Goddess", length=1):
    
    
    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki
