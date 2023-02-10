import random

COLORS = ['R','G','B','Y','W','O']
TRIES = 10
CODE_LENGTH = 4


def game():
    print("Welcome to mastermind")
    print("You have {} tries to guess a combination of 4 colors in their corect positions".format(TRIES))
    print("The valid colors are: ", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = user_guess()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print("Congratulations! You guessed the code in {} tries.".format(TRIES))
            break

        print("Correct positions: {} ~ Incorrect positions: {}".format(correct_pos,incorrect_pos))

    else:
        print('\n')
        print("You ran out of chances, the correct combination of colors was {}".format(code))


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return (code)

def user_guess():
    while True:
        guess = input("Enter you guess: ").upper().split(' ')

        if len(guess) != CODE_LENGTH:
            print("You must choose {} colors".format(CODE_LENGTH))
            continue
        
        for color in guess:
            if color not in COLORS:
                print("Invalid choice: {} \n Try again".format(color))
                break

        else:
            break

    return (guess)

def check_code(guess, answer):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in answer:
        if color not in color_counts:
            color_counts[color] = 0
            color_counts[color] += 1
        
    for guess_col,answer_col in zip(guess, answer):
        if guess_col == answer_col:
            color_counts[color] -= 1
            correct_pos += 1

    for guess_col,answer_col in zip(guess, answer):
        if guess_col in color_counts and color_counts[guess_col] > 0:
            incorrect_pos += 1
            color_counts[guess_col] -= 1

    return (correct_pos, incorrect_pos)
           
if __name__ == "__main__":
    game()