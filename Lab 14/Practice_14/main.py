import math
from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    print("Tasks 1 to 4 below and 5 to exit the program:")
    print("1. Calculate factorial")
    print("2. Calculate exponentiation 2")
    print("3. Calculate exponentiation 3")
    print("4. Calculate the square root")
    print("5. Calculate the cube root")
    print("6. Calculate logarithm")
    print("7. Calculate natural logarithm")
    print("8. Calculate decimal logarithm")
    print("9. EXIT")
    while True:
        try:
            choice = int(input("Select tasks 1 to 8 below or press 9 to exit the program: "))
            if choice == 1:
                while True:
                    try:
                        i = int(input("Enter a natural number: "))
                        if i >= 1:
                            print(f"The factorial of {i} is: {fact(i)}")
                            break
                        else:
                            print("Enter a natural number to calculate factorial!!!")
                    except ValueError:
                        print("Enter a natural number to calculate factorial!!!")

            elif choice == 2:
                while True:
                    try:
                        i = float(input("Enter a number: "))
                        print(f"Square: {exp2(i)}")
                        break
                    except ValueError:
                        print("Enter a number!!!")
                        
            elif choice == 3:
                while True:
                    try:
                        i = float(input("Enter a number: "))
                        print(f"Cube: {exp3(i)}")
                        break
                    except ValueError:
                        print("Enter a number!!!")
                        
            elif choice == 4:
                while True:
                    try:
                        i = float(input("Enter a number: "))
                        print(f"Square root: {root2(i)}")
                        break
                    except ValueError:
                        print("Enter a non-negative number!!!")

            elif choice == 5:
                while True:
                    try:
                        i = float(input("Enter a number: "))
                        print(f"Cube root: {root3(i)}")
                        break
                    except ValueError:
                        print("Enter a number!!!")
                        
            elif choice == 6:
                while True:
                    try:
                        a = float(input("Enter the base a(a>0, a!=1): "))
                        b = float(input("Enter a logarithm number b(b>0): "))
                        log(a, b)
                        if log(a, b) == math.log(b, a):
                            break
                    except ValueError:
                        print("Enter the base a(a>0, a!=1) and a logarithm number b(b>0)!!!")
                print(f"Logarithm: {log(a, b)}")
                        
            elif choice == 7:
                while True:
                    try:
                        b = float(input("Enter a natural logarithm number b(b>0): "))
                        ln(b)
                        if ln(b) == math.log(b):
                            break
                    except ValueError:
                        print("Enter a natural logarithm number b(b>0)!!!")
                print(f"Natural logarithm: {ln(b)}")
                
            elif choice == 8:
                while True:
                    try:
                        b = float(input("Enter a decimal logarithm number b(b>0): "))
                        lg(b)
                        if lg(b) == math.log10(b):
                            break
                    except ValueError:
                        print("Enter a decimal logarithm number b(b>0)!!!")
                print(f"Decimal logarithm: {lg(b)}")
                      
            elif choice == 9:
                print("EXIT!")
                break
            else:
                print("Please enter a number between 1 and 9!!!")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 9!!!")

if __name__ == "__main__":
    main()