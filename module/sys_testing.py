#!/usr/bin/env python3
import sys

def main():
    print("Script name is: ", sys.argv.pop[0])
    print("Remaining command line arguments: ", sys.argv)

    info = sys.version_info
    print("Python version: ")
    print(info.major, info.minor, info.micro, sep=".")

    print("Python path:")
    for each_path in sys.path:
        print("\t", each_path)
    print()
    
    number = input("Please enter an integer")
    if not number.isdecimal():
        print(number + "is not an integer.")

    print("You entered the number " + number)


if __name__ == "__main__":
    main()