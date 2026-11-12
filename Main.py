import random
print("")
print("\tGUESS THE NUMBER\t\n")

def guess_game():
    number = random.randint(1,10)
    attempts = 1
    while True:
        try:
            guess = int(input("\nGuess the number between 1 to 10 :"))
            
            if guess > 10:
                print("You can only guess between 1 to 10.")
            elif guess < 1:
                print("You can only guess between 1 to 10.")
            elif guess > number:
                print("Take a lower guess.")
                attempts += 1
            elif guess < number:
                print("Take a bigger guess.")
                attempts += 1
            elif attempts == 1:
                print("\nCongratulations! 🤩")
                print(f"You guessed the correct number in first attempt.\n")
                break
            elif guess == number:
                print("\nCongratulations! 🤩")
                print(f"You guessed the correct number in {attempts} attempts.\n")
                break
            
        except ValueError:
            print("Invalid Input! Please Enter a number.\n")
        except Exception as e:
            print(f"An error occured : {e}\n")

def main():
    while True:
        try:
            play = int(input("Enter 1 to play or 0 to stop : "))
            if play == 0:
                print("See you later 😊")
                break
            elif play == 1:
                guess_game()
            else:
                print("\nPlease Enter 0 or 1\n")
                continue
        except ValueError:
            print("\nInvalid Input! Please Enter a number\n")
if __name__ == "__main__":
    main()


