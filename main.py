from stats import num_words, char_count, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(word_count, char_sorted, book_path):
    print(" BOOKBOT ".center(30, "="))
    print(f"Analyzing book found at {book_path}")
    print(" Word Count ".center(30, "-"))
    print(f"Found {word_count} total words")
    print(" Character Count ".center(30,"-"))
    for char_dict in char_sorted:
        if char_dict["character"].isalpha():
            print(f"{char_dict['character']}: {char_dict['num']}")
    print(" THE END ".center(30,"="))
    
def main():
    book = get_book_text(sys.argv[1])
    char_dict = char_count(book)
    numwords = num_words(book)
    sorted_list = sort_on(char_dict)
    print_report(numwords, sorted_list, sys.argv[1])
try:
    main()
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
