#Number Guessing Game Objectives:
import random
hard = 5
easy = 10

def cheak_answer(guess, answer,turns):
    if guess > answer:
        print("Too high..")
        return turns -1
    elif guess< answer:
        print("Too low")
        return turns -1
    else:
        print(f"Congratulations.The answer was {answer}")
def set_dificulty():
    level= input("Chosse a dificulty type 'e' for easy and 'h' for hard : ")
    if level == "h":
     return hard
    else:
      return easy
def game():
    print("whelcome to the number guessing game.") 
    turns = set_dificulty()
    
    answer = random.randint(1,100)
    print(f"The answer was {answer}")
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Guess a number from 1 to 100. : "))
        turns = cheak_answer(guess,answer,turns) 
        if turns == 0:
            print("You have out of moves, You looosee..brah")
            return
game()


