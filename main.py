
import sys
from stats import *


# A function that takes a path to a book and returns number of words in the book
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
    return num_words


# A function that takes a path to a book and returns dictionary of how many each character (lower) exists in the book
def get_book_chars(file):
    with open(file) as f:
        file_contents = f.read()
        num_chars = get_num_characters(file_contents)
    return num_chars


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    print(sys.argv[1])

    num_words=get_book_text(book_path)
    num_chars=get_book_chars(book_path)
    num_chars=sort(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in num_chars:
        print(f"{key['char']}: {key['num']}")
    print("============= END ===============")


main()