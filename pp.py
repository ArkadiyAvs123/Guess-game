import random
import math

# Taking inputs
lower_bound = int(input("Type in your lower bound - "))
upper_bound = int(input("Type in your upper bound - "))

# Creating a number

x = random.randint(lower_bound, upper_bound)

print("You have only", round(math.log(upper_bound - lower_bound + 1, 2)), "attempts to guess the number.")

# Initializing the number of guesses.
count = 0

while count < math.log(upper_bound - lower_bound + 1, 2):
    count += 1

    # Taking guess as input
    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congrutilations! You guessed right!")

        break;

    elif x < guess:
        print("Your guess too high.")

    elif x > guess:
        print("Your guess too small.")

if count > math.log(upper_bound - lower_bound + 1, 2):
    print("The number is %d" % x)
    print("\tBetter luck for the next time!")

