'''
Copyright (c) Shahibur Rahaman.
Licensed under the MIT License.
'''


import Operations
import time


def main():
    print(
"""
|> Press (Ctrl + C) to exit the program.
|> Choose your operation:

1. Addition
2. Subtraction
3. Multiplication
4. Division
"""
)

    while True:
        try:
            while True:
                try:
                    choice = int(input("Enter your choice: [1, 2, 3, 4] "))
                    if choice > 4 or choice < 1:
                        print("\nPlease enter your choice according to the given operation options!")
                        continue        
                except ValueError:
                    print("\nPlease enter a numerical value only!")
                    continue
                else:
                    break
        
        
            x = float(input("\nEnter the first number: "))
            y = float(input("Enter the second number: ")) 
            
            add = Operations.Operation(x, y).addition()
            sub = Operations.Operation(x, y).subtraction()
            mul = Operations.Operation(x, y).multiplication()
            div = Operations.Operation(x, y).division()

            c = choice

            print("")
            if c == 1:
                print(f"{x} + {y} = {add}")
            elif c == 2:
                print(f"{x} - {y} = {sub}")
            elif c == 3:
                print(f"{x} X {y} = {mul}")
            elif c == 4:
                print(f"{x} / {y} = {div}")
            print("")

        except KeyboardInterrupt:
                print("\nExiting...")
                time.sleep(1)
                break


if __name__ == "__main__":
    main()
    