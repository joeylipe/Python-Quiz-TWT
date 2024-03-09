print("Welcome to my Python quiz!") 

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's start :)")
score = 0 


answer = input("What year was Python first released? ")
if answer == "1991":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was released in 1991.")

answer = input("Did Python get its name from the snake? ").lower()
if answer == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Python got its name from Monty Python's Flying Circus.")

answer = input("Was the creator of Python's name \"Guido van Rossum\"? ").lower()
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is Python older than Java? ").lower()
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Python was released in 1991, while Java was released in 1995.")

answer = input("Does Python have an antigravity easter egg? ").lower()
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Use \"import antigravity\" for a suprise")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")



