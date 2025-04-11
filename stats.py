def num_words(booktext):
    split = booktext.split()
    numwords = len(split)
    return numwords

def char_count(book_text):
    char_dict = {}
    char_set = set()
    for char in book_text:
        if char in char_set:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            char_set.add(char)
    return char_dict
    
   