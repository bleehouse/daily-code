import random

memberlist = []
while True:
    member = input("Enter a name :")
    print(member)
    if member:
        memberlist.append(member)
    else:
        break

selectNumber = random.randrange(0, len(memberlist))
print("The winner is..." + memberlist[selectNumber])
