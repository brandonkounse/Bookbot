from stats import total_word_count, char_count, sorted_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    total_word_count(get_book_text(sys.argv[1]))
    total_chars = char_count(get_book_text(sys.argv[1]))

    sorted_list = sorted_words(total_chars)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

main()