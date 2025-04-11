def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_words(booktext):
    split = booktext.split()
    numwords = len(split)
    return numwords
    
def main():
    book = get_book_text("books/frankenstein.txt")
    numwords = num_words(book)
    print(f"{numwords} words found in the document")
main()
