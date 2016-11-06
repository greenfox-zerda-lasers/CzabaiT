import random

def guess_game():
    # initial values for first while loops
    interval = -1
    guess = -1

    print("\n**********  Guess game   *********\n")

    while not (interval == 10 or interval == 100 or interval == 1000):
        try:
            interval = int(input("**********************************\nChoose interval: 10 or 100 or 1000\n"))
        except ValueError:
            print('You did not enter a valid number\n')
            continue
        if not (interval == 10 or interval == 100 or interval == 1000):
            print('You did not enter a valid number\n')


    target = random.randrange(0,interval+1)
    guess_number = 1

    while guess != target:
        guess = -1
        while not (guess >= 0 and guess <= interval):
            try:
                guess = int(input("Guess between 0 and " + str(interval) + ":\n"))
            except ValueError:
                print('You did not enter a valid number\n')
                continue
            if not (guess >= 0 and guess <= interval):
                print('You did not enter a valid number\n')

        if guess == target:
            print('\n**You are an okay guy! You won!**\n*******You guessed ' + str(guess_number) + ' times*******\n')
            repeat_game = "Maybe"
            while repeat_game == "Maybe":
                repeat_game = input("Do you want play again? Yes or No\n")
                if repeat_game == "YES" or repeat_game == "Yes" or repeat_game == "yes" or repeat_game == "Y" or repeat_game == "y":
                    return True
                elif repeat_game == "NO" or repeat_game == "No" or repeat_game == "no" or repeat_game == "N" or repeat_game == "n":
                    return False
                else:
                    repeat_game = "Maybe"

        elif guess > target:
            guess_number += 1
            print("C'mon! Guess lower!")

        else:
            guess_number += 1
            print("C'mon! Guess higher!")


#initial value for first guest_game() running
repeat = True

while repeat == True:
    repeat = guess_game()

print("*********    Bye! =)    *********")

