import string
import os
import json

def stemmer(word: str):
    i = len(word)

    if word[:i].endswith("det"):
        i -= 3
    elif word[:i].endswith("et"):
        i -= 2
    elif word[:i].endswith("t"):
        i -= 1
    elif word[:i].endswith("nen"):
        i -= 3
    elif word[:i].endswith("suus"):
        i -= 4
    elif word[:i].endswith("uus"):
        i -= 3
    elif word.endswith("us"):
        i -= 2
    while i >= 1 and word[i - 1] in ("a", "i", "o", "u", "y", "e", u"ä", u"ö", u"å"):
        i -= 1
    word = word[: max(i, 6)]  # Dont shorten under 6 characters

    return word

def load_txt(path: str, filename: str):
    res = [] # return empty list by default
    
    assert isinstance(path, str) and isinstance(filename, str), "invalid input"
    
    path_combined = os.path.join(path, filename)
    
    if os.path.exists(path_combined):
        with open(path_combined, "r") as f:
            res = f.readlines()
        
        res = set(line.strip() for line in res)
    
    else:
        raise FileNotFoundError("file not found, check your path")
        
    return res

def load_json(path: str, filename: str):
    res = [] # return empty list by default
    
    assert filename.endswith("json"), "require a json file"
    
    path_combined = os.path.join(path, filename)
    
    if os.path.exists(path_combined):
        with open(path_combined, "r") as f:
            res = json.load(f)
    else:
        raise FileNotFoundError("file not found, check your path")
        
    return res

def save_json(path: str, filename: str, fp: object):

    assert isinstance(path, str) and isinstance(filename, str), "invalid input"
    assert filename.endswith("json"), "require a json file"

    path_combined = os.path.join(path, filename)

    if not os.path.exists(path):
        os.mkdir(path)
    with open(path_combined, "w") as f:
        json.dump(fp, f)

    return

