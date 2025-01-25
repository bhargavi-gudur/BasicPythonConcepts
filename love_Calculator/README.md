# Love Calculator

This is a simple Python program that calculates the "love score" between two individuals based on the occurrences of the letters in the words "true love" in their names.

## How It Works

1. The program prompts the user to enter two names.
2. It combines the names and converts the combined string to lowercase.
3. It counts the occurrences of each letter in the phrase "true love" within the combined string.
4. The counts for the letters in "true" are summed to produce the `true_score`.
5. The counts for the letters in "love" are summed to produce the `love_score`.
6. The `love_percentage` is calculated by concatenating `true_score` and `love_score`.

## Usage

To run the program, simply execute the script in a Python environment:

```python
python love_calculator.py

## Example

```python
What is your name? Alice
What is his/her name? Bob

Your love score is 40.
