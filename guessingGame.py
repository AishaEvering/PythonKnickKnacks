import random
import sys


start = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
end = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
allowedAttemptCount = int(sys.argv[3]) if len(sys.argv) >= 4 else 10

attempts = 0

print('Hello Welcome to the Guessing Game!!!!')
correctNum = random.randint(start, end)


def getRange(guess, targetNum):
    range = 0

    if guess < targetNum:
        range = targetNum - guess
    elif guess > targetNum:
        range = targetNum - guess

    return range


while (True):

    if attempts >= allowedAttemptCount:
        print(f"You Lost: the number is {correctNum}")
        break

    try:
        if attempts == 0:
            ans = int(input(
                f'Ready? You have {allowedAttemptCount} gueses.  Guess a Number between {start} - {end}: '))
        else:
            ans = int(input(f'Guess a Number between {start} - {end}: '))

        if ans < start or ans > end:
            print(f"Please enter a valid number with range {start} - {end}")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue

    if ans == correctNum:
        print('Wow you are CORRECT!!!!!! YOU WIN!!!')
        break

    if (getRange(ans, correctNum) <= 3):
        print(
            f"Ooooo so close. Try Again, you have {allowedAttemptCount - attempts} guesses")
    else:
        print(
            f'Nope, Try Again, you have {allowedAttemptCount - attempts} guesses')

    attempts += 1
