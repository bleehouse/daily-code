import random

print("Let's play Guess the Number")
level = int(input("Pick a difficulty level (1,2, or 3): "))
end = 1
matchcnt = 0

if level == 1:
    end = 10
elif level == 2:
    end = 100
elif level == 3:
    end = 100

match = random.randrange(1, int(end))
print("match :", match)
question = "I have my number. what's your guess? "
while True:
    matchcnt = matchcnt + 1
    guess = input(question)
    if int(match) == int(guess):
        print("You got it in ", guess, "guesses")
        break
    elif int(guess) > int(match):
        question = "Too high, Guess again :"
    elif int(guess) < int(match):
        question = "Too low, Guess again :"



