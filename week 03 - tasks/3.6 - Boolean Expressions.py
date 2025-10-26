# DO NOT TOUCH THESE LINES. THEY ARE USED BY THE TESTS
# If you want to test this program, when you hit Run, enter values of True or False via the console
is_raining = bool(int(input()))
no_hat = bool(int(input()))
#######################################################
# You should fix this line to combine is_raining and no_hat to produce the correct result for takes_umbrella.
takes_umbrella = False

if is_raining and no_hat:
    takes_umbrella = True
    print(takes_umbrella)
elif is_raining and not no_hat:
    print(takes_umbrella)
else:
    print(takes_umbrella)