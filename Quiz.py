def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, Try Again!")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct Answer is", answer)

score = 0
print("Guess The Animal")
guess1 = input("Which Bear lives at the North Pole?: ")
check_guess(guess1, "Polar Bear")
guess2 = input("Which Is The Fastest Land Animal?: ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the Largest Animal?: ")
check_guess(guess3, "Blue Whale")
guess4 = input("What has to be broken before you can use it?: ")
check_guess(guess4, "Egg")
guess5 = input("I'm tall when I'm young, and I'm short when I'm old. What am I?: ")
check_guess(guess5, "Candle")
guess6 = input("What is full of holes and still holds water?: ")
check_guess(guess6, "sponge")
guess7 = input("What gets wet while drying?: ")
check_guess(guess7, "Towel")
guess8 = input("What can't talk but will reply when spoken to?: ")
check_guess(guess8, "Echo")
guess9 = input("What gets bigger when more is taken from it?: ")
check_guess(guess9, "Hole")
guess10 = input("Where does today come before yesterday?: ")
check_guess(guess10, "Dictionary")
guess11 = input("What invention lets you look right through a wall?: ")
check_guess(guess11, "Window")
guess12 = input("It belongs to you, but other people use it more than you do. What is it?: ")
check_guess(guess12, "Name")
guess13 = input("What has one eye, but can't see?: ")
check_guess(guess13, "Needle")
guess14 = input("What has hands, but can't clap?: ")
check_guess(guess14, "Clock")
guess15 = input("What has legs, but doesn't walk?: ")
check_guess(guess15, "Table")
guess16 = input("What can you catch, but not throw?: ")
check_guess(guess16, "Cold")
guess17 = input("What has many teeth, but can't bite?: ")
check_guess(guess17, "Comb")
guess18 = input("What has words, but never speaks?: ")
check_guess(guess18, "Book")
guess19 = input("What runs all around a backyard, yet never moves?: ")
check_guess(guess19, "Fence")
guess20 = input("What building has the most stories?: ")
check_guess(guess20, "Library")
print("Your Score is " + str(score))