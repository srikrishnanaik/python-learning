#!/usr/bin/env python3
def main():
    total = 0
    msg = "Please enter a number, 'end' to quit: "
    while True:
        value = input(msg)
        if value == "end":
            break
        try:
            total += int(value)
        except ValueError:
            print("Invalid input, Please try again")
        
    print("Total is:", total)

if __name__ == "__main__":
    main()