user_input = int(input("Please enter a number: \n"))

if user_input % 3 == 0:
    if user_input % 5 == 0:
        print("Your number is divisible by 3 and 5.")
    elif user_input % 5 != 0:
        print("Your number is divisible by 3 and NOT 5.")
elif user_input % 3 != 0:
    if user_input % 5 == 0:
        print("Your number is NOT divisible by 3 and is divisible by 5.")
    else:
        print("Your number is NOT divisible by 3 and 5.")