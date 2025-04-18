def num_words(booktext):
    split = booktext.split()
    numwords = len(split)
    return numwords

def char_count(book_text):
    char_dict = {}
    char_set = set()
    for char in book_text.lower():
        if char in char_set:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            char_set.add(char)
    return char_dict
def sort_on(dict):
    dict_list = []
    for entry in dict:
        dict_list.append({'character':entry, "num":dict[entry]})
    def get_num(item):
        return item["num"]
    
    dict_list.sort(reverse=True, key=get_num)
    return dict_list