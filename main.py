'''
bulls and cows
Bulls and cows is a classic game about guessing a 4-digit number.
You are playing against computer.
If you guessed a digit, but it's not in a proper position you have 1 cow.
If you guessed a digit on its proper position you have 1 bull.
'''
import random


def welcome():
    print("Welcome to a game of bulls and cows!")
    print("In this game you supposed to quess a 4-digit code of computer")
    print("faster than your opponent. You print a random 4 different digits and get")
    print("cows(if you guess a digit but not on its place) and bulls(if")
    print("a digit on it's proper place. You try to guess a code first.")
    print("if you want to finish enter 'q' or 'Q' in terminal")
    print()


def getcode():
    print("Enter a code with 4 different digits")
    code=input(">>> ")
    length=len(code)
    try:
        int(code)
    except:
        print("It must consists of digits")
        code=getcode()
    if length!=4:
        print("Your code hasn't 4 digit")
        code=getcode()
    for i in range(4):
        for j in range(4):
            if i!=j and code[i]==code[j]:
                print("It has to be different digits!")
                code=getcode()
    return code

    
def hint(num,code):
    if (num%3==0) and (num>4):
        print("Want a hint?(Press 'y' to choose")
        h=input(">>> ")
        if h=="y":
            used=True
            print("Choose which digit you want to know")
            try:
                pos=int(input(">>> "))
                print(code[pos-1])
            except:
                print("You missed a chance for hint")

def gen_code():
    code=""
    for i in range(4):
        new_digit=str(random.randrange(0,10))
        while new_digit in code:
            new_digit=str(random.randrange(0,10))
        code+=new_digit
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


def game():
#ask for a code
    user_code=getcode()
    print("Your code was saved\n")
#generate a code for a computer
    comp_code=gen_code()

#start a guessing cycle
    print("Lets start guessing!")
    guessing=True
    bulls_user=cows_user=bulls_comp=cows_user=0
    count_guesses=0
    while guessing:
        #player phase
        hint(count_guesses,comp_code)
        guess=getcode()
        bulls_user,cows_user=guess_result(guess,comp_code)
        #maintain output of info about guesses
        print(f"You have {bulls_user} bulls and {cows_user} cows")
        #computer phase
        bulls_comp,cows_comp=guess_result(gen_code(),user_code)
        #maintain output of info about guesses
        print(f"Computer has {bulls_comp} bulls and {cows_comp} cows\n")
        if bulls_user==4 or bulls_comp==4:
            guessing=False

#when sb guessed exit loop and output winning info
    if bulls_user==4 and bulls_comp==4:
        print("It's draw")
    elif bulls_comp==4:
        print("You lose(")
    else:
        print("You win!")


def main():
#generate a welcoming message
    welcome()
#start a game loop
    game()
    #ask to play again
    print("Want to play again?(Press 'y' or 'Y')")
    resume=input(">>> ")
    if resume =="y" or resume=="Y":
        game()

if __name__=="__main__":
    main()