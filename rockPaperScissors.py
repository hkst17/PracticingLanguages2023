import random
r = "rock"
p = "paper"
s = "scissors"
list = [r,p,s]

paperRule = "Paper beats rock! "
scissorRule = "Scissors beats paper! "
rockRule = "Rock beats scissors! "
winState = "Good job, you win. \n"
loseState = "Sorry you lose this round... \n"

i = 0
score = 0

while i < 3:

    randChoice = random.choice(list)
    userChoice = input("Rock? Paper? or Scissors? ")

    print("The PC chose: " + randChoice)
    print("You chose: " + userChoice)

    if userChoice == randChoice:
        print("you are tied. Try again.\n")
    elif userChoice == p and randChoice == r:
        print(paperRule + winState)
        i += 1
        score += 1
    elif userChoice == r and randChoice == p:
        print(paperRule + loseState)
        i += 1
        score -= 1
    elif userChoice == r and randChoice == s:
        print(rockRule + winState)
        i += 1
        score += 1
    elif userChoice == s and randChoice == r:
        print(rockRule + loseState)
        i += 1
        score -= 1
    elif userChoice == s and randChoice == p:
        print(scissorRule + winState)
        i += 1
        score += 1
    elif userChoice == p and randChoice == s:
        print(scissorRule + loseState)
        i += 1
        score -= 1
    else:
        print("Umm.. Something went wrong..")

if score >= 1:
    print("You won out of 3 rounds! ")
else:
    print("You lose out of 3 rounds. ")

#     This code took 2 hours to figure out :) Learned that you can have a guideline of what to do,
#     but issues arise when trying to code and I can solve them on the way. Also learned that I could
#     build on a simple idea whether that is adding additional functionality like playing 3 times
#     or adding a point system to tell if you have won the 3 games or not. Can make aesthetics and
#     accessibility better at the end also.
