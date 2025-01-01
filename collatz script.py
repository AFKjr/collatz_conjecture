def collatz(number):
    """Function to perform the Collatz operation on a number."""
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    # Prompt the user to enter a number
    number = int(input("Good morning, enter a number: "))

    # Print the initial number
    print(number)

    # Loop through the numbers until it reaches 1
    while number != 1:
        number = collatz(number)
        print(number)

    # Print the final output
    print("Final number is:", number)

# Standard boilerplate to call the main() function
if __name__ == "__main__":
    main()
