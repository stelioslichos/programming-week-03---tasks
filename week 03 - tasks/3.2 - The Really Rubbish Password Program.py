# The Really Rubbish Password Program

# This is the stored password for the user
secret_password = "secret"

print("Welcome to NOSA Inc.")
print("Did you know that the Moon is an average of 238,855 miles away from Earth\n")

password = input("Please enter your password:\n")

if password == "secret":
    print("\nAccess Granted!")
else:
    print("\nAccess Denied!")
input("\n\nPress the enter key to exit.")