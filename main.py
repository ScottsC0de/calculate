print("Welcome to Calculate\n")
print("A simple command line calculator application\n")


# calculator functions w/ arithmetic operators in Python
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def remainder(x, y):
    return x % y


def exponent(x, y):
    return x**y


def floor_div(x, y):
    return x // y


print("What would you like to do?\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Check Remainder")
print("6. Exponent")
print("7. Floor Division")


while True:

    def userMath():
        choice = input("Please select the number of your desired action ")

        num_1 = int(input("\nEnter first number "))
        num_2 = int(input("Enter second number "))

        if choice == "1":
            answer = add(num_1, num_2)
            print(f"{num_1} + {num_2} = {answer}\n")

        elif choice == "2":
            answer = subtract(num_1, num_2)
            print(f"{num_1} - {num_2} = {answer}\n")

        elif choice == "3":
            answer = multiply(num_1, num_2)
            print(f"{num_1} x {num_2} = {answer}\n")

        elif choice == "4":
            answer = divide(num_1, num_2)
            print(f"{num_1} ÷ {num_2} = {answer}\n")

        elif choice == "5":
            answer = remainder(num_1, num_2)
            print(f"The remainder of {num_1} ÷ {num_2} is {answer}\n")

        elif choice == "6":
            answer = exponent(num_1, num_2)
            print(f"{num_1} to the {num_2} power is {answer}\n")

        elif choice == "7":
            answer = floor_div(num_1, num_2)
            print(f"{num_1} ÷ {num_2} (floored) = {answer}\n")

    userMath()
