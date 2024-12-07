from collections import Counter
from string import ascii_letters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = count_words(file_contents)
    character_counts = count_characters(file_contents)

    print_report(words, character_counts)

def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    return Counter(c.lower() for c in text if c in ascii_letters)

def print_report(word_count: int, character_counts: Counter) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the book\n")
    for character, count in character_counts.most_common():
        print(f"{character}: {count}")
    print("--- End report of books/frankenstein.txt ---")


main()