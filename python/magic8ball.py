import random

answers = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later"
]

match = random.randrange(0, 4)

print(answers[match])
