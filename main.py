def get_book_text(path_to_file):
    with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents

def get_word_count(book):
    words = book.split()
    return len(words)

def main():
    print(f"{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document")

main()
