import random

l=["rock","paper","scissor"]


while True:
    
    r=random.shuffle(l)
    c=random.choice(l)

    print("rock | paper | scissor\nor press 0 for Exit the Game")
    print("----------------------------------------")
    a=input("Enter your choice in word: ") 
    a=a.lower()
    print()

    if a=="0":
        print("Exiting the Game, Thankyou")
        break

    elif a==c:
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("Draw\n")

    elif a=="rock" and c=="paper":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you lose\n")

    elif a=="rock" and c=="scissor":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you win\n")
    
    elif a=="paper" and c=="rock":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you win\n")

    elif a=="paper" and c=="scissor":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you lose\n")

    elif a=="scissor" and c=="rock":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you lose\n")
    
    elif a=="scissor" and c=="paper":
        print(f"your choice: {a}, Opponent Choice: {c}\n")
        print("you win\n")

    else:
        print("Invalid Choice")
        print("Please enter a single word choice\n")