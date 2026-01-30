print("=== THE CALCULATOR FOR STUDENTS ===")

while True:
    print("\nSelect an arithmetic operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Average")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Exiting the program. Goodbye!")
        break
    l=[1,2,3,4,5,6]

    if choice in l:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = num1 + num2
            print(f"The addition of the two numbers is: {result}")

        elif choice == 2:
            result = num1 - num2
            print(f"The subtraction of the two numbers is: {result}")

        elif choice == 3:
            result = num1 * num2
            print(f"The multiplication of the two numbers is: {result}")

        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"The division of the two numbers is: {result}")
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == 5:
            result = num1 % num2
            print(f"The modulus of the two numbers is: {result}")

        elif choice == 6:
            result = (num1 + num2) / 2
            print(f"The average of the two numbers is: {result}")

    else:
        print("Invalid choice. Please select a number between 1 and 7.")
