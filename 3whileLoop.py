# Make a variable isRunning and set it to True
isRunning = True

# If the user types "q" change isRunning to False and quit the while loop
while isRunning:
    print("Do you want to quit")
    i = input()
    if i=="q"or i=="Q":
        isRunning =False


