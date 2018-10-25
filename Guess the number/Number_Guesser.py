
import roll_dice

actual_number = roll_dice.Roll_Dice(6)
actual_number.roller()
my_guess = input("Enter Your Guess Here and hit enter:")

loop_check = 1

while loop_check == 1:
    if actual_number.results == my_guess:
        print("Thats Right!")
        loop_check = 0
    elif actual_number.results < my_guess:
        print("Lower...")
        my_guess = input("Enter Your Next Guess Here and hit enter:")
    elif actual_number.results > my_guess:
        print("Higher...")
        my_guess = input("Enter Your Next Guess Here and hit enter:")
print("The Actual Dice Roll was...", actual_number.results)
exit()



