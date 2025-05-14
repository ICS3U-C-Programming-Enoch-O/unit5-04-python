#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 22, 2025
# The calculate_area() function calculates the area of a triangle


def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number
    elif sign == "%":
        return first_number % second_number


def main():
    sign = input("Enter operation (+, -, *, /, %): ")
    first_number_str = input("Enter first number: ")
    second_number_str = input("Enter second number: ")

    try:
        first_number = float(first_number_str)
        second_number = float(second_number_str)
        if sign == "+" or sign == "-" or sign == "*" or sign == "/" or sign == "%":
            if second_number == 0 and (sign == "/" or sign == "%"):
                print("You can't divide by 0")
            else:
                result = calculate(sign, first_number, second_number)
                print(f"{first_number} {sign} {second_number} = {result}")
        else:
            print(f"'{sign}'Operation is not valid")
    except:
        print("Error: Invalid input")


if __name__ == "__main__":
    main()
