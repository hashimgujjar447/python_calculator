

def addition(a,b):
    return a+b


def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def modulus(a,b):
    return a%b






def main():
    while True:

        print("Press 1 Addition of two numbers is: ")
        print("Press 2 Subtraction of two numbers is: ")
        print("Press 3 Multiplication of two numbers is: ")
        print("Press 4 Division of two numbers is: ")
        print("Press 5 Modulus of two numbers is: ")
        print("Press 6 Exit: ")

        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result=addition(a,b)
                print("*" * 70);
                print(f"Addition of {a} and {b} is: {result}")
                print("*" * 70);
               
            case 2:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result=subtraction(a,b)
                print("*" * 70);
                print(f"Subtraction of {a} and {b} is: {result}")
                print("*" * 70);
              
            case 3:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result=multiplication(a,b)
                print("*" * 70);
                print(f"Multiplication of {a} and {b} is: {result}")
                print("*" * 70);
            case 4:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result=division(a,b)
                print("*" * 70);
                print(f"Division of {a} and {b} is: {result}")
                print("*" * 70);
            case 5:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result=modulus(a,b)
                print("*" * 70);
                print(f"Modulus of {a} and {b} is: {result}")
                print("*" * 70);
            case 6:
                break
            case _:
                print("Invalid choice")
                continue





main()