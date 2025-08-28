


# A function that takes a path to a book and returns number of words in the book
def get_num_words(text):
    return len(text.split())


# A function that takes a path to a book and returns dictionary of how many each character (lower) exists in the book
def get_num_characters(text):
    char_count={}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count



def sort(items):
    temp = []
    for i in items:
        new_dict={}
        new_dict["char"]=i
        new_dict["num"]=items[i]
        temp.append(new_dict)
    return temp