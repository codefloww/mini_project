'''
bulls and cows
Bulls and cows is a classic game about guessing a 4-digit number.
You are playing against computer.
If you guessed a digit, but it's not in a proper position you have +1 cow.
If you guessed a digit on its proper position you have +1 bull.



'''
import random
def welcome():
    print("Welcome to a game of bulls and cows!")
    print("In this game you supposed to quess a 4-digit code of computer")
    print("faster than your opponent. You print a random 4 numbers and get")
    print("cows(if you guess a digit but not on its place) and bulls(if")
    print("a digit on it's proper place. You try to guess a code first.")
    print("if you want to finish enter 'q' or 'Q' in terminal")

def getcode():
    print("Enter a code with 4 digits")
    code=input(">>> ")
    length=len(code)
    try:
        int(code)
    except:
        code=getcode()
    if length!=4:
        print("Your code hasn't 4 digit")
        code=getcode()
    
def main():
#start a game loop
while True:

#generate a welcoming message
    welcome()
#ask for a code
    user_code=getcode()

#generate a code for a computer

#start a guessing cycle
#maintain output of info about guesses
#when sb guessed exit loop and output winning info
#ask to play again
#when sb guessed exit loop and output winning info
if __name__=="__main__":
    main()