while True:
    try:
        character_age = int(input("Enter your age to continue: "))
    except ValueError:
        print("Sorry what did you just said?")
        continue
    else:
        break
if character_age >= 18:
    print(f"Okay so you are {character_age} you must pay 150$")
else:
    print(f"Okay so you are {character_age} you must pay 100$")
    
#note this code is for Python 3.6
