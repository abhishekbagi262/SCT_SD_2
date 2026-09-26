import random
number = random.randint(1, 100)
attempts = 0
low = 1
high = 100

while True:
    
    try:
        guess = int(input("Enter your Guess:"))

    except ValueError:
        print("Please Enter Only Valid Number.")
        continue

    if guess < low or guess > high:
        print("Please enter a number between",low, "and", high)
        continue
    attempts +=1

    if guess < number:
        low = guess
        print("Too Low")
        print("HINT:Number Is Between", low, "and", high)

    elif guess > number:
        high = guess
        print("Too High.")
        print("Number Is Between", low, "and", high)

    else:
        print("Guessed Number is correct!")
        print("Attempts Taken To Guess Correctly:", attempts)
        break