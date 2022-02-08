import random

#range 1 - 20
the_number = random.randint(1, 20)

count = 0

while True:
    print('Try to guess the number in between 1 - 20...')
    my_input = input('...')
    count += 1

    try:
        my_guess = int(my_input)
        #print(type(my_guess))

        if my_guess == the_number:
            print("Congratulations! You guessed the muber right!")
            print("It took you only ", count, " tries!")
            break
        
        elif the_number < my_guess:
            print("Nah, the number is smaller than this. ")
        
        elif the_number > my_guess:
            print("No, the number is higher than this one.")
        else:
            print("I have no idea what this is...")


    except:
        print('Please enter a valid number...')

input('Press ENTER to exit...')