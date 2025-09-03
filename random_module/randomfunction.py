import random as rd
def random_number():
    def shuffle_list():
        numbers = list(range(1, 11))
        rd.shuffle(numbers)
        print("Shuffled List:", numbers)
        return numbers

    def choice_list(n=10):
        numbers = list(range(1, n + 1))
        choice = rd.choice(numbers)
        print("Choice List:", numbers, "Random Choice:", choice)
        return choice

    def random_choice():
        choice_list_numbers = list(range(1, 11))
        rd.shuffle(choice_list_numbers)
        random_pick = rd.choice(choice_list_numbers)
        print("Shuffled Choice List:", choice_list_numbers,
              "Random Pick:", random_pick)
        return random_pick

    def uniform_random():
        random_float = rd.uniform(1, 10)
        print("Random Float:", random_float)
        return random_float

    def calling_function():
        shuffle_list()
        choice_list()
        random_choice()
        uniform_random()

    calling_function()


random_number()
