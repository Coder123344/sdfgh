number=int(input("guess a number(between 1-9):"))

while chances < 5:
    if (guess is number):
        print("CONGRATS, AMAZING")
        break

elif(number>4):
    print("nah, way too high")
else:
    print("too low")

if not chances < 5:
    print("Boohoo, ya lose the number was 3")
