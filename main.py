from stats import get_num_words, get_char_count, get_sorted_chars
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    num_words = get_num_words(book_file_path)
    sorted_char_list = get_sorted_chars(book_file_path)

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for char in sorted_char_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


    
    # print(f"{num_words} words found in the document")
    # count_dict = get_char_count("books/frankenstein.txt")
    # print(count_dict)




main()
    