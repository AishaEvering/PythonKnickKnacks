import random
import sys

start = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
end = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
allowedAttemptCount = int(sys.argv[3]) if len(sys.argv) >= 4 else 10

attempts = 0
close_range = 3

GAME_INTRO = 'Hello Welcome to the Guessing Game!!!!'
YOU_LOST = 'You Lost: the number is'
OUT_OF_BOUNDS = 'Please enter a valid number with range'
ASK_FOR_VALID_NUMBER = 'Please enter a valid number'
YOU_WIN_MSG = 'Wow you are CORRECT!!!!!! YOU WIN!!!'

print(GAME_INTRO)
correctNum = random.randint(start, end)


def get_range(guess, target_num):
    if guess < target_num:
        return target_num - guess
    elif guess > target_num:
        return guess - target_num

    return 0


def is_out_of_attempts():
    return attempts >= allowedAttemptCount


def is_initial_attempt():
    return attempts == 0


def is_out_of_bounds(answer):
    if answer < start or answer > end:
        print(f"{OUT_OF_BOUNDS} {start} - {end}")


def get_remaining_guesses():
    return allowedAttemptCount - attempts


def is_within_close_range(answer):
    return get_range(answer, correctNum) <= close_range


def guess_number():
    try:
        if is_initial_attempt():
            answer = int(input(
                f'Ready? You have {allowedAttemptCount} guesses.  Guess a Number between {start} - {end}: '))
        else:
            answer = int(input(f'Guess a Number between {start} - {end}: '))

        if is_out_of_bounds(answer):
            return None

        return answer
    except ValueError:
        print(ASK_FOR_VALID_NUMBER)
        return None


def try_again(answer):
    remaining_guesses = allowedAttemptCount - attempts

    if is_within_close_range(answer):
        print(
            f"Ooooo so close. Try Again, you have {remaining_guesses} guesses")
    else:
        print(
            f'Nope, Try Again, you have {remaining_guesses} guesses')


if __name__ == '__main__':
    while True:
        if is_out_of_attempts():
            print(f"{YOU_LOST} {correctNum}")
            break

        ans = guess_number()

        if ans is None:
            continue
        elif ans == correctNum:
            print(YOU_WIN_MSG)
            break

        try_again(ans)

        attempts += 1
