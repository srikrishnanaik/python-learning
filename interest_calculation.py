#!/usr/bin/env python3
def main():
    interest()
    interest11()
    data()

def data():
    amount = 45
    monthly = 1.25
    finalamount = amount + 12 * float(monthly) * 10
    print("With data particle: ")
    print("you will get in total ", int(finalamount), "lakh rupees for 10 years")
    print()
    print("If you reinvest data particle monthly amount on yearly basis: ")
    year = 9
    reyamount = 15
    while year != 0:
        year -= 1
        reyamount = reyamount + (reyamount * 0.3)   
    print("Final amount would be: ", int(reyamount + finalamount), "lakh rupees after 10 years")
    print()
    print("If you reinvest data particle monthly amount on monthly basis: ")
    months = 9 * 12 + 11
    yearamount = amount + 12 * 1.25
    remamount = (yearamount  + 1.25) * 0.025
    totalamount = yearamount + remamount
    while months != 0:
        months -= 1
        totalamount =  totalamount + (totalamount * 0.025)
        
    print("Final amount would be: ", int(totalamount), "lakh rupees after 10 years")
    print()

def interest():
    years = 10
    amount = 45
    interest = 0.07
    while years != 0:
        years -= 1
        amount = float(amount) + float(amount * 0.07)
    print()
    print("Hi Atmu")
    print()
    print("With bank FD (interest 7% every year): ")
    print("you will get in total", int(amount), "lakh rupees for 10 years")
    print()

def interest11():
    years = 10
    amount = 45
    interest = 0.07
    while years != 0:
        years -= 1
        amount = float(amount) + float(amount * 0.12)
        
    print()
    print("With bank FD (interest 12% every year): ")
    print("you will get in total", int(amount), "lakh rupees for 10 years")
    print()



if __name__ == "__main__":
    main()

