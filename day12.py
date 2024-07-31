import random
answer = random.randint(1,100)

def easy():
    choice = 10
    for i in range(choice,0, -1) :
        print(f"You have {i} chances to guess")
        a = int(input("Guess the number :"))
        print(f"you guess:{a}")
        if a < answer :
            print(f"guess too low")
        elif a > answer :
            print(f"guess too high")
            continue
        else :
            print(f"You won! the number is {answer}")
            break
    else:
        print(f"You lost! The number was {answer}.")
    
def hard():
    choice = 5
    for i in range(choice,0,-1) :
        print(f"You have {i} chances to guess")
        b = int(input("Guess the number :"))
        print(f"you guess:{b}")
        if b < answer :
            print(f"guess too low")
        elif b > answer :
            print(f"guess too high")
            continue
        else :
            print(f"You won! the number is {answer}")
            break
    else:
        print(f"You lost! The number was {answer}.")

choice = str(input("You want easy or hard?"))
if choice == "easy" :
    easy()
elif choice == "hard" :
    hard()
else :
    print("invalid")

# Day 13 has no project yet only debugging