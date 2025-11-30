"""
@file RepeatedWords.py
@author Gandla
@brief Program to count how many times each word appears in a sentence.

@date 2025-11-30
"""

def count_words(sentence):
    words = sentence.lower().split()     # split into words + lowercase
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\n--- Word Frequency ---")
    for word, count in frequency.items():
        print(f"{word} : {count} times")


def main():
    sentence = input("Enter a sentence: ")
    count_words(sentence)


if __name__ == "__main__":
    main()