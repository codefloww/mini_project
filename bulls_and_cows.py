#mini_project.py
"""Bulls and cows is a classic game about guessing a 4-digit number.
You are playing against computer.
If you guessed a digit, but it's not in a proper position you have 1 cow.
If you guessed a digit on its proper position you have 1 bull.
First to guess win.
This game can be played in one player and can be played only via terminal.
"""
import random

def help()->None:
    """Prints a help info about rules and mechanics of game.
    """    
    print("""The goal of game is to guess a code of 
    computer(get four bulls).While you do this computer tries to guess yours
    Firstly you type your code which computer will try to guess. Then every
    move you type a 4-digit code which you think computer have choosed.
    If in this guess there are digits on proper place you will have 1 bull 
    for it. And if you guessed digits but in different places you get cows.
    You get hint every 3 moves if you're not in pro difficulty. Also you can
    exit in any moment by typing 'exit'. 

    """)
def welcome()->None:
    """Prints an introduction to the game.
    """
    print("""=================================================================
     [@@]
    <|##|>
     d  b""")
    print("""Heeey, hello, my name is COB and I'm computer.
            Welcome to my game of bulls and cows!
            In this game you are supposed to guess my 4-digit code
            faster than I guess yours. 
            Firsly, you choose a code for me to guess and I do the 
            same. 
            Then you type a random 4 different digits and get
            cows(if you guess a digit but not on its place) and 
            bulls (if a digit on it's proper place). 
            You try to guess a code first. If you want to finish enter 'exit' 
            in terminal. If something is unclear type 'help'.\n""")


def getcode()->str:
    """Asks and returns a code from user

    Returns:
        str: A 4-different digit code
    """    
    print("Enter a code with 4 different digits")
    code=input(">>> ")
    length=len(code)

    if code=="exit":
        quit()
    elif code=="help":
        help()
        getcode()
    #check correctness of input
    if code.isdecimal():
        if length!=4:
            print("Your code hasn't 4 digits")
            code=getcode()
        
        for i in range(4):
            for j in range(4):
                if i!=j and code[i]==code[j]:
                    print("It has to be 4 different digits!")
                    code=getcode()
        return code
    else:
        print("It must consists of digits")
        code=getcode()
    
def hint(num:int,code:str)->None:
    """Asks for a hint. Not available for difficulty 'pro'.
    
    Args:
        num(int): A number of guesses which were maden
        code(str): A code for which we have a hint
    """
    if (num%3==1) and (num>3):
        print("Want a hint?(Press 'y' to choose)\n")
        h=input(">>> ")

        if h=="exit":
            quit()
        elif h=="y":
            used=True
            print("Choose which digit you want to know")
            try:
                pos=int(input(">>> "))
                print(code[pos-1])
            except:
                print("You missed a chance for hint")
        else:
            print("Okay, you're not searching easy ways")


def gen_code(user_code:str, lev: str )->str:
    """A function that generates a random string of 4 digit(code)

    Args:
        user_code(str): Can be used as generated code
        level(str): Decides which chance for using user_code
        
    Returns:
        str: A code which is used as a guess for comp
    """
    code=""
    for i in range(4):
        new_digit=str(random.randrange(0,10))
        while new_digit in code:
            new_digit=str(random.randrange(0,10))
        code+=new_digit
    chance=0.04 if lev=="b" else 0.08
    lucky_guess=random.random()
    if lucky_guess<chance:
        return user_code
    return code


def guess_result(guess:str, code:str)->int:
    """Gets a guess of code and a code and returns how many digits 
    are guessed on proper place and other places.
    
    Args:
        guess(str):A string of 4 digit from a player
        code(str):A string of 4 digit(starting code) to compare
            with guess
        
    Returns:
        bulls(int):A number of digits on its proper place
        cows(int):A number of digits which are in code but not in
            proper place
    """
    bulls=0
    cows=0
    for i in range(4):
        for j in range(4):
            if i==j and guess[i]==code[j]:
                bulls+=1
            elif i!=j and guess[i]==code[j]:
                cows+=1
    return bulls,cows


def difficulty()->str:
    """A function which prints out difficulty levels and returns 
    chosen by user level
    
    Returns:
        str: A level of difficulry represented by letter
    """
    print("""Choose a difficulty level:
            Pro(press 'p')
            Semi-pro(press 's')
            Beginner(press 'b')""")
    level=input(">>> ")
    if level=="exit":
        quit()
    elif level=="help":
        help()
        difficulty()
    elif (len(level)!=1) or (level not in "psb"):
        print("You failed to choose a difficulty")
        difficulty()
    return level

    
def game(level:str)->None:
    """Maintain process of a single game with certain difficutly
    
    Args:
        level(str):A difficulty level that influence on chance of 
            computer guessing and abbility to have a hint
    """
    #ask for a code
    user_code=getcode()
    print("Your code was saved\n")

    print("Lets start guessing!")
    guessing=True
    bulls_user=cows_user=bulls_comp=cows_user=0
    count_guesses=0

    #generate a code for a computer
    comp_code=gen_code(user_code,level)

    #start a guessing cycle
    while guessing:
        #player phase
        if level!="p":
            hint(count_guesses,comp_code)
        
        user_guess=getcode()
        comp_guess=gen_code(user_code,level)
        count_guesses+=1
        bulls_user,cows_user=guess_result(user_guess,comp_code)

        #maintain output of info about guesses
        print(f"You have {bulls_user} bulls and {cows_user} cows")
        #computer phase
        bulls_comp,cows_comp=guess_result(comp_guess,user_code)
        #maintain output of info about guesses
        print(f"Computer guess is {comp_guess}")
        print(f"Computer has {bulls_comp} bulls and {cows_comp} cows\n")
        if bulls_user==4 or bulls_comp==4:
            guessing=False

    #when sb guessed exit loop and output winning info
    if bulls_user==4 and bulls_comp==4:
        print("You somehow managed to draw this :|")
    elif bulls_comp==4:
        print("Oh nooo, you lose, anyway")
        print(f"A computer code was {comp_code}")
    else:
        print("You win!")

    print(f"There was {count_guesses} guesses")

    #asking for a replay
    print("Want to play again?(Press 'y' or 'Y')")
    resume=input(">>> ")
    if resume =="y" or resume=="Y":
        game(level)


def main()->None:
    """Maintain a full program and its processes
    """
    #generate a welcoming message
    welcome()
    difficulty_level=difficulty()
    #start a game loop
    game(difficulty_level)


if __name__=="__main__":
    main()
    