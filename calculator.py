"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    user_input = ""
    while user_input != "q":
        user_input = raw_input("> ")
        token = user_input.split(" ")
        if token[0] == "+":
            print(arithmetic.add(int(token[1]), int(token[2])))
        if token[0] == "-":
            print(arithmetic.subtract(int(token[1]), int(token[2])))
        if token[0] == "*":
            print(arithmetic.multiply(int(token[1]), int(token[2])))
        if token[0] == "/":
            print(arithmetic.divide(int(token[1]), int(token[2])))
        if token[0] == "square":
            print(arithmetic.square(int(token[1])))
        if token[0] == "cube":
            print(arithmetic.cube(int(token[1])))
        if token[0] == "power":
            print(arithmetic.power(int(token[1]), int(token[2])))
        if token[0] == "mod":
            print(arithmetic.mod(int(token[1]), int(token[2])))
    


if __name__ == '__main__':
    main()
