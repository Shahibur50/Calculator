import Operations
import time


'''
MIT License
Copyright (c) 2020 Shahibur Rahaman
'''

def main():
    print(
"""
Calculator version 2.9.10.20

Copyright (c) Shahibur Rahaman
Licensed under the MIT License.

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
                        print("\nPlease enter your choice according to the given operation options only!")
                        continue        
                except ValueError:
                    print("\nPlease enter a numerical value only!")
                    continue
                else:
                    break
        
            while True:
                try:
                    x = float(input("\nEnter the first number: "))
                    y = float(input("Enter the second number: ")) 
                except ValueError:
                    print("\nPlease enter numerical values only!\n")
                else:
                    break

            add = Operations.Operation(x, y).addition()
            sub = Operations.Operation(x, y).subtraction()
            mul = Operations.Operation(x, y).multiplication()
            div = Operations.Operation(x, y).division()

            c = choice

            print("\n-----------------------------")
            if c == 1:
                print(f"{x} + {y} = {add}")
            elif c == 2:
                print(f"{x} - {y} = {sub}")
            elif c == 3:
                print(f"{x} X {y} = {mul}")
            elif c == 4:
                print(f"{x} / {y} = {div}")
            print("-----------------------------\n")

        except KeyboardInterrupt:
                print("\nExiting...")
                time.sleep(1)
                break


if __name__ == "__main__":
    main()
    
