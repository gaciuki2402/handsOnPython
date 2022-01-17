#input=number
#random because the comp will have to guess
#comp guess(1,10)
#tries=5
import random
tries=0
while tries<5:
    num=eval(input("Enter a number"))
    guess=random.randint(1,10)
    if num==guess:
        print("You guessed correctly")
        break
    else:
        print(f"Wrong guess!")
    tries+=1
