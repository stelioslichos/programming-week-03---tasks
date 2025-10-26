# Mood Computer
# Demonstrates the elif clause
mood = int(input("Please enter a number between 1 and 3:\n"))

# use elif to print mood lines of the face
if (mood < 1) or (mood > 3):
    print("Illegal mood value!")
else:
    print("Right now I am feeling...\n")

# print the first five lines of the face
    print("""-----------
|         |
| O     O |
|    <    |
|         |""")

    if mood == 1:
        # happy
        print("| .     . |")
        print("|  `...`  |")
    elif mood == 2:
        # neutral
        print("| ------- |")
        print("|         |")
    elif mood == 3:
        # sad
        print("|   .'.   |")
        print("|  '   '  |")
    # print the bottom line of the face
    print("-----------")
    input("\n\nPress the enter key to exit.")