import random

# 1 -> Snake
# -1 -> Water
# 0 -> Gun

you_Dict = {"s": 1, "w": -1, "g": 0}
reverse_Dict = {1: "Snake", -1: "Water", 0: "Gun"}

your_string = input("Enter your choice\n (s for Snake, w for Water, g for Gun): ").lower()

if your_string not in you_Dict:
    print("Invalid input! Please enter s, w, or g.")
else:
    computer = random.choice([-1, 0, 1])
    you = you_Dict[your_string]

    print(f"Your choice: {reverse_Dict[you]}\nComputer choice: {reverse_Dict[computer]}")

    if (computer == you):
        print("It's a Draw!")
    elif ((computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1)):
        print("You Win!")
    else:
        print("You Lose!")
