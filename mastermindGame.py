import random, os, time

def cls():
    os.system('cls')
def slp(sec):
    time.sleep(sec)

#Copy of the error.
"""
File "U:\Other\mastermindGame.py", line 45, in <module>
    number = int(input("Number: "))
ValueError: invalid literal for int() with base 10: ''
"""

guess = 0
count = 0
digit = 0
number = 0
correct = 0
check = ""


code = []
inputCode = []
place = []

print("Welcome to Code Breaker!")
slp(2)
print("This game is similar to Mastermind (or whatever it's called).")
slp(2)
print("But there are some differences.")
slp(2)
print("A random, 4 digit, code will be generated.")
slp(2)
print("The numbers will always be between 1 and 5 (including those two).")
slp(2)
print("You will have 8 guesses to get the correct code.")
input()
cls()
print("Selecting the code...")

for x in range(0,4):
    digit = random.randint(1,4)
    code.append(digit)
slp(1)

while guess != 8:    
    for i in range(0,4):
        print("Please input a number between 1 and 5.")
        while check == "":
            number = int(input("Number: "))
            if number > 5:
                print("Number is invalid.")
                check = ""
            else:
                inputCode.append(number)
                check = "T"
            slp(0)
        check = ""
        
    for m in range(0,4):
        if code[m] == inputCode[m]:
            correct += 1
            place.append(inputCode[m])
        else:
            slp(1)
            place.append("N")
            
    print("You got ", correct, "right.")
    slp(1)
    print("The correct digits you inputted were...")
    slp(2)
    print(place)

    guess = guess + 1
    input("Continue.")
    cls()

print("You are out of guesses.")
slp(2)
print("The correct code was: ", code)
slp(2)
print("Better luck next time!")
input("Press enter to exit.")
