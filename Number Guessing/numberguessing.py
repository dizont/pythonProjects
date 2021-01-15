import random
#add comments, add not repeatable hints.
maxRange = 100
theAnswer = random.randint(1,maxRange)
answerIsWrong = True
#print(theAnswer)
global repeatable # in order not to repeat one particular hint
repeatable = True
SCORE = 1024
# hintsInThePast = [] still no implementation of hints in the past

# gives a random hint based on multiples of an answer
def multipleHint(answer):
    listOfHints = []
    global repeatable
    for i in range(2,theAnswer+1):
        if answer%i==0:
            listOfHints.append(i)
    if len(listOfHints)==1:
        repeatable = False
        return "The number is Prime"
    else:
        return "The number is a multiple of %s"%listOfHints[random.randint(1,len(listOfHints)-1)]

# gives more or less hint
def lessOrMoreHint(guess,answer):
    if guess<answer:
        return "The Answer is more"
    elif guess>answer:
        return "The Answer is less"
    
# randomizes which hint to give
def giveRandomHint(guess,answer):
    if random.randint(0,1)==0 and repeatable:
        return multipleHint(answer)
    else:
        return lessOrMoreHint(guess, answer)


print("Try to guess a number from 1 to %s.\nYour Score starts at 1024 and is halved for every wrong answer" %maxRange)
while answerIsWrong:
    theGuess = int(input("Your guess:   "))
    if theGuess==theAnswer:
        answerIsWrong = False
        print("You are correct! Your Final Score is %s"%SCORE)
    else:
        SCORE = SCORE // 2
        print(giveRandomHint(theGuess,theAnswer))
        print("Your Score is %s"%SCORE)
        if SCORE == 1:
            print("Sorry the Game is Over. The answer was %s"%theAnswer)
