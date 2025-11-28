from stats import total_word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    total_word_count(get_book_text("./books/frankenstein.txt"))
    total_chars = char_count(get_book_text("./books/frankenstein.txt"))
    print(total_chars)

main()