#!/usr/bin/env python

print("Enter a year to check is it is leap: ")

year = int (input())

if(year % 4 == 0) or ( (year % 100 == 0) and (year % 400 == 0) ):
    print("The year is Leap year")
else:
    print("The year is not a Leap year")
