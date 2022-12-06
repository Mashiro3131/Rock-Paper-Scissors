import random



class Counter:
    def __init__(self):
        self.user = 0
        self.computer = 0
        self.rounds = 0

    def add_user(self):
        self.user += 1

    def add_computer(self):
        self.computer += 1

    def add_round(self):
        self.rounds += 1

    def get_user(self):
        return self.user

    def get_computer(self):
        return self.computer

    def get_rounds(self):
        return self.rounds
    
    def __str__(self):
        return f"You: {self.user} | Computer: {self.computer}"
    
    
    

class Game:
    def __init__(self, counter):
        self.counter = counter
        self.computer_choice = random.choice(["rock", "paper", "scissors"])

    def play(self):
        self.counter.add_round()
        user_input = input("Choose rock, paper or scissors : ")
        if user_input in ["rock", "paper", "scissors"]:
            print("The computer chose", self.computer_choice)
        else:
            print("!!! Invalid input, try again !!!")
            self.play()
      
        
        # Tie
        if user_input == self.computer_choice:
            print("Nice try, but it's a tie !")   
        # elif user_input != "rock" and user_input != "paper" and user_input != "scissors":
        #    print("!!! Invalid input, try again !!!") 
        #    self.play()
       
       
       
        # Rock
        elif user_input == "rock":
            if self.computer_choice == "scissors":
                print("You.......... win !!")
                self.counter.add_user()
            else:
                print("well... you lose!")
                self.counter.add_computer()
        
       
        
        # Paper
        elif user_input == "paper":
            if self.computer_choice == "rock":
                print("You win!")
                self.counter.add_user()
            else:
                print("Congratulations, you wi... lose! ")
                self.counter.add_computer()
        
        
        
        # Scissors
        elif user_input == "scissors":
            if self.computer_choice == "paper":
                print("You win!")
                self.counter.add_user()
            else:
                print("You lose!")
                self.counter.add_computer()
        print(self.counter)
        print("")



    def start(self):
        while self.counter.get_rounds() < 5:
            self.play()
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
            print("You're not very good at this game")



# Runs the game
if __name__ == "__main__":
    counter = Counter()
    game = Game(counter)
    game.start()