"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *
#import string

def main():
    user_input = ""
    while user_input != "q":
        user_input = raw_input("> ")
        token = user_input.split(" ")
        values = token[1:]

        if token[0] not in ["+", "-", "*", "/", "square", "cube", "power", "mod"]:
            print('Please enter a valid operand. "+", "-", "*", "/", "square", "cube", "power", "mod"')
            continue
        
        #unfinished for loop -- check if user_input is a digit
        # for index in values:
        #     for number in index:
        #         if number not in string.digits 


        if token[0] == "+":
            print add(int(token[1]), int(token[2]))
        if token[0] == "-":
            print subtract(int(token[1]), int(token[2]))
        if token[0] == "*":
            print multiply(int(token[1]), int(token[2]))
        if token[0] == "/":
            print divide(int(token[1]), int(token[2]))
        if token[0] == "square":
            print square(int(token[1]))
        if token[0] == "cube":
            print cube(int(token[1]))
        if token[0] == "power":
            print power(int(token[1]), int(token[2]))
        if token[0] == "mod":
            print mod(int(token[1]), int(token[2]))
    


if __name__ == '__main__':
    main()
