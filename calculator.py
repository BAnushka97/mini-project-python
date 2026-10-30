def addition(n1, n2):
    print("Addition:", n1 + n2)
def subtraction(n1, n2):
    print("Subtraction:", n1 - n2)
def multiplication(n1, n2):
    print("Multiplication:", n1 * n2)
def division(n1, n2):
    if n2 != 0:
        print("Division:", n1 / n2)
    else:
        print("Cannot divide by zero")
while True:
    print("****** Sample Calculator ******")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    option = int(input("Enter your option: "))
    if option == 5:
        print("Exit")
        break
    if option in [1, 2, 3, 4]:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if option == 1:
            addition(n1, n2)
        elif option == 2:
            subtraction(n1, n2)
        elif option == 3:
            multiplication(n1, n2)
        elif option == 4:
            division(n1, n2)
    else:
        print("Invalid option")
