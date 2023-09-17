#!/usr/bin/env python3
import calendar as cal

def main():
    cal.setfirstweekday(cal.SUNDAY)
    datasets = [cal.day_name, cal.day_abbr, cal.month_name, cal.month_abbr]
    for calendar_data in datasets:
        print(list(calendar_data))

    print(cal.month(2016, 1))
    cal.prmonth(2017, 3, w=5)

if __name__ == "__main__":
    main()