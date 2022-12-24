import random
randNumber = random.randint(1,100)


userGuess = None
Guesses = 0 

while (randNumber != userGuess):
    userGuess = int(input("Enter your guess : "))
    Guesses += 1
    if randNumber == userGuess :
        print("Your guess was correct.")
    else:
        if randNumber > userGuess :
            print("Your guess was wrong !! Please enter a greater number.")
        else:
            print("Your gurss was wrong !! Please enter a smaller number.")

print(f"The number of guesses you took is {Guesses}")

with open ("hiscore.txt",'r') as f:
    hiscore = int(f.read())
    
if Guesses < hiscore:
    print("You have broken the highscore")
    with open ("hiscore.txt",'w') as f :
        f.write(str(Guesses))
