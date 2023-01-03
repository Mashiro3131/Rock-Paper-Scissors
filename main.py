import random

class Counter:
    def __init__(self):
        self.user = 0
        self.computer = 0

    def add_user(self):
        self.user += 1

    def add_computer(self):
        self.computer += 1

    def get_user(self):
        return self.user

    def get_computer(self):
        return self.computer

    def __str__(self):
        return f"You: {self.user} | Computer: {self.computer}"

class Game:
    def __init__(self, counter):
        self.counter = counter
        self.results = {
            ("rock", "scissors"): "You win!",
            ("rock", "paper"): "You lose!",
            ("paper", "rock"): "You win!",
            ("paper", "scissors"): "You lose!",
            ("scissors", "paper"): "You win!",
            ("scissors", "rock"): "You lose!",
        }
        self.computer_choice = random.choice(["rock", "paper", "scissors"])

    def play(self):
        while True:
            user_input = input("Choose rock, paper or scissors : ")
            if user_input in ["rock", "paper", "scissors"]:
                break

        result = self.results.get((user_input, self.computer_choice))
        if result:
            print(f"The computer chose {self.computer_choice}, {result}")
            if result.startswith("You win"):
                self.counter.add_user()
            else:
                self.counter.add_computer()
        else:
            print(f"The computer chose {self.computer_choice}, it's a tie!")

        print(self.counter)
        print()

    def start(self):
        counter = 0
        while counter < 5:
            self.play()
            counter += 1
        if self.counter.get_user() > self.counter.get_computer():
            print("""\
                             (_)        | |                                     
 _   _  ___  _   _  __      ___ _ __    | |                                     
| | | |/ _ \| | | | \ \ /\ / / |  _ \   | |                                     
| |_| | (_) | |_| |  \ V  V /| | | | |                                          
 \__, |\___/ \____|   \_/\_/ |_|_| |_|  (_)                                     
  __/ |                                                                         
 |___/                                                                          
                                                                /~\             
                                                               |00 ]            
                              ___                              _\=/_            
                             / []\                       #    /  _  \           
                           _|_____|_                       \\\//|/_\|\\\        
                          |   ===   |                       \/  \_/  ||         
                          |_|  0  |_|                          \___/   #        
                           ||  0  ||                           |   |            
                           ||_____||                           | | |			
                          |~ \___/ ~|                          []|[]            
 @Mashiro3131             /=\ /=\ /=\                          | | |            
__________________________[_]_[_]_[_]_________________________/_]_[_\___________
""")


        else:
            print("You lost :(")

counter = Counter()
game = Game(counter)
game.start()