def get_book_text(path_to_file):
    with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents

def get_num_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    lower = book.lower()
    dict = {}
    for char in lower:
        dict[char] = 0 
    for char in lower:
        if char in dict:
            dict[char]+=1
    return dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sorted_dictlist = []
    for keys in dict:
        sorted_dict = {}
        sorted_dict["char"] = keys
        sorted_dict["num"] = dict[keys]
        sorted_dictlist.append(sorted_dict)
    sorted_dictlist.sort(reverse=True, key=sort_on)
    return sorted_dictlist

