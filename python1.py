
import random
#We'll often import libraries like this that provide important functionality.

x = input("Pick a number between 1 and 100: ")
# Utilize the built-in input function to ask the user a question.
# Set the value of x to the user typed value

y = random.randint(1,100)
# Utilize the random function to generate a random number between 1-100
# Save this value to the variable y

print("You picked " + x + " and the number " + str(y) + " was generated")
# Print tht two values using a regular string

print(f"You picked {x} and the number generated was {y}".format(x,y))
# Print the two values using an fstring this time

if int(x) < y:
    print("Too Low!")
if int(x) > y:
    print("Too High")
if int(x) == y:
    print ("Correct!")
