#TODO add runners throw again (inside loop at line 43), add dice color to the output

import random

class Player:

    __brains = 0
    
    def __init__(self, name):
        self.__name = name

    def add_brains(self, n):
        self.__brains += n

    def get_brains(self):
        return self.__brains

    def get_name(self):
        return self.__name 
        

    def play_turn(self):

        print_line()
        for p in players:
            print(f"{p.get_name()} has currently {p.get_brains()} brains")
        print_line()
        #reset the dice cup, draw dice and gunshots
        gunshots = 0
        brains = 0
        drawn_dice = []
        dice_cup = []
        for i in range(6): dice_cup.append(Die("green"))
        for i in range(4): dice_cup.append(Die("yellow"))
        for i in range(3): dice_cup.append(Die("red"))

        #throw dice loop
        while True:            
            #draw the dice
            drawn_dice = self.draw_dice(dice_cup)
            #throw the dice 
            for d in drawn_dice: d.throw()
            print(f"\n{self.get_name()} threw the dice and got: ")
            for d in drawn_dice: print(f"\t{d.get_color()} - {d.get_result()}")
            gunshots += [d.get_result() for d in drawn_dice].count("SHOTGUN")
            brains += [d.get_result() for d in drawn_dice].count("BRAINS")
            print(f"gunshots = {gunshots}")
            if gunshots < 3:
            #check/update stats loop
                while True:
                    answer = input("Do you wish to throw again?\n")
                    if answer.lower() in "no":
                        self.add_brains(brains)
                        return
                    elif answer.lower() in "yes":
                        #reinsert each runner die into the dice cup
                        for d in drawn_dice: 
                            if d.get_result() == "RUNNER":
                                dice_cup.append(d) 
                        #reset the result each throw                        
                        result = []                        
                        break
                    else:
                        print("Please enter YES or NO")
        
            else:   
                print(f"You got shot {gunshots} times!  You lose your turn!")
                input("Press a key to continue...")
                break

                    

        

    def draw_dice(self, cup):
        drawn = []
        for i in range(3): drawn.append(cup.pop(random.randint(0,len(cup)-1)))
        return drawn


class Die:

    def __init__(self, color):

        self.__color = color        
        if color == "green":
            self.__faces = ("BRAINS","BRAINS","BRAINS","SHOTGUN","RUNNER","RUNNER")
        elif color == "yellow":
            self.__faces = ("BRAINS","BRAINS","SHOTGUN","SHOTGUN","RUNNER","RUNNER")
        else:
            self.__faces = ("BRAINS","SHOTGUN","SHOTGUN","SHOTGUN","RUNNER","RUNNER")

    def get_color(self):
        return self.__color

    def get_faces(self):
        return self.__faces

    def get_result(self):
        return self.__result

    def throw(self):
        self.__result = self.__faces[random.randint(0,5)]

def print_line():
    for i in range(80): print("_", end="")
    print()
    

def main():
    
    global players
    players = []    

    print("""
Welcome to...

▒███████▒ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓▓█████    ▓█████▄  ██▓ ▄████▄  ▓█████ 
▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▓█   ▀    ▒██▀ ██▌▓██▒▒██▀ ▀█  ▓█   ▀ 
░ ▒ ▄▀▒░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▒███      ░██   █▌▒██▒▒▓█    ▄ ▒███   
  ▄▀▒   ░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▒▓█  ▄    ░▓█▄   ▌░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
▒███████▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░░▒████▒   ░▒████▓ ░██░▒ ▓███▀ ░░▒████▒
░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░░ ▒░ ░    ▒▒▓  ▒ ░▓  ░ ░▒ ▒  ░░░ ▒░ ░
░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░ ░ ░  ░    ░ ▒  ▒  ▒ ░  ░  ▒    ░ ░  ░
░ ░ ░ ░ ░░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░       ░ ░  ░  ▒ ░░           ░   
  ░ ░        ░ ░         ░    ░       ░     ░  ░      ░     ░  ░ ░         ░  ░
░                                  ░                ░          ░               

by BlueMan2903
    """)

    while True:
        n = input("Type the number of players that are going to play: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("\nYou have not entered a valid number.") 

    for i in range(n):
        name = input(f"Enter a name for Player number {i+1}: ")
        p = Player(name)
        players.append(p)

    #main game loop
    while True:

        for p in players:
            p.play_turn()
            if p.get_brains() >= 13:
                print(f"Congratulations, {p.get_name()}!! You won the game!!")
                return

if __name__ == "__main__":

    main()
    
