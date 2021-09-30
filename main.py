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
    print("faster than your opponent. You print a random 4 different digits and get")
    print("cows(if you guess a digit but not on its place) and bulls(if")
    print("a digit on it's proper place. You try to guess a code first.")
    print("if you want to finish enter 'q' or 'Q' in terminal")

def getcode():
    print("Enter a code with 4 different digits")
    code=input(">>> ")
    length=len(code)
    try:
        int(code)
    except:
        code=getcode()
    if length==4:
        print("Your code was saved")
    else:
        print("Your code hasn't 4 digit")
        code=getcode()
    for i in range(4):
        for j in range(4):
            if i!=j and code[i]==code[j]:
                print("It has to be different digits!")
                code=getcode()
    return code

def gen_code():
    code=""
    for i in range(4):
        code+=random.randrange(0,10)
    return code

def guess_result(guess,code):
    bulls=0
    cows=0
    for i in range(4):
        for j in range(4):
            if i==j and guess[i]==code[j]:
                bulls+=1
            elif i!=j and guess[i]==code[j]:
                cows+=1
    return bulls,cows
def main():


#generate a welcoming message
    welcome()
#start a game loop
    while True:
    #ask for a code
        user_code=getcode()

    #generate a code for a computer
        comp_code=gen_code()
    #start a guessing cycle
        print("Lets start a guessing!")
        guessing=True
        while guessing:
            #player phase
            print("Enter your guess")
            guess=getcode()
            print("You have {0} bulls and {1} cows".format(guess_result(guess,comp_code)))


    #maintain output of info about guesses
    #when sb guessed exit loop and output winning info

    #ask to play again
        print("Want to play again?(if want to exit enter 'q' or 'Q')")
        exit=input(">>> ")
        if exit in "Qq":
            break
    #when sb guessed exit loop and output winning info
if __name__=="__main__":
    main()