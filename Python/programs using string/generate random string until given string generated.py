# Python Program to generate random string until given string is generates

target_string = input("Enter the Target String: ")
print(f"The target string is: '{target_string}'")

while True:
    user_input = input("Enter a random string: ")

    if user_input == target_string:
        print(f"Congratulations! You entered the target string '{target_string}'.")
        break
    else:
        print("Incorrect string. Try again.")
