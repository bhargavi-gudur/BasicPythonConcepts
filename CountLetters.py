"""
@file CountLetters.py
@author Gandla Bhargavi
@brief Program to count how many times each letter appears in a string.

@date 2025-11-25
"""

def count_letters(text):
    count = {}

    for ch in text:
        if ch.isalpha():                 # count only letters
            ch = ch.lower()              # ignore case
            count[ch] = count.get(ch, 0) + 1

    print("\n--- Letter Count ---")
    for letter, freq in count.items():
        print(f"{letter} : {freq} times")


def main():
    text = input("Enter any sentence: ")
    count_letters(text)


if __name__ == "__main__":
    main()