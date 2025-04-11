from stats import num_words, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    book = get_book_text("books/frankenstein.txt")
    char_dict = char_count(book)
    numwords = num_words(book)
    print(f"{numwords} words found in the document")
    print(char_dict)
main()
