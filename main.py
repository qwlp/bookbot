import sys
from stats import get_book_text, get_num_words, count_char, sort_dict

if len(sys.argv) == 2:
    path = sys.argv[1]
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path))} total words")
    print("--------- Character Count -------")

    sorted_dict = sort_dict(count_char(get_book_text(path)))

    for i in sorted_dict:
        for k in i:
            if i["char"].isalpha() == True:
                print(f"{i["char"]}: {i["num"]}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


