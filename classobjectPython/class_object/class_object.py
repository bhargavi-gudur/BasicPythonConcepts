class Game:
    # self means itself in the class
    def __init__(self, name, sport_type):
        self.name = name
        self.sport_type = sport_type

    def do_work(self):
        if self.sport_type == "outdoor game":
            print(self.name, "plays as game runner")
        elif self.sport_type == "indoor game":
            print(self.name, "plays as chess")

    def speaks(self):
        print(self.name, "says how are you?")

# Creating an object of the Game class
my_game = Game("Alice", "outdoor game")

# Calling the do_work method
my_game.do_work()  # Output: Alice plays as game runner

# Calling the speaks method
my_game.speaks()  # Output: Alice says how are you?
