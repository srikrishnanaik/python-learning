#!/usr/bin/env python3
from car import Car

def main():
    malibu = Car("Chevy", "Malibu")
    miata = Car("Mazda", "Miata")
    mustang = Car("Ford", "Mustang")
    soul = Car("Kia", "Soul")
    print("# of existing cars:", Car.quantity)

    malibu.drive(miles=1000)
    miata.drive(500)
    print(malibu, miata, mustang, soul, sep="\n")
    print("Deleting Malibu")
    del malibu

    print("# of existing cars:", Car.quantity)

if __name__ == "__main__":
    main()

