import random


def play_roll_the_dice():
    print("-----------------------")
    print("    ROLL THE DICE      ")
    print("-----------------------")
    next_step = "yes"
    points = 0
    while next_step == "yes":
        x = int(input("enter your lucky number 1-6: "))
        print("roll the dice")
        y = random.randint(1, 6)
        print(f"rolled dice number is:{y} ")
        if x == y:
            points = 500
            print("you won")
            points = points + 500
        else:
            points = 0
            print("you lost")
        next_step = input("would you like to play same game again? (yes/no): ")
    print(f"you won {points} points")


def play():
    game_index = int(input("which game you want to play? (1/2/3): "))
    if game_index == 1:
        print("1:ROLL THE DICE")
        play_roll_the_dice()
    elif game_index == 2:
        print("2:TIC TAC TOE")
    elif game_index == 3:
        print("3:LUDO")


if __name__ == "__main__":
    next_step1 = "yes"
    while next_step1 == "yes":
        play()
        next_step1 = (input("would you like to play again? (yes/no): "))
        if next_step1 == 'yes':
          continue