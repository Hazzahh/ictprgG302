#!/usr/bin/python3

import math
number = int(input("Enter a number: "))

print(number)

for n in range(1, number + 1):
    print("The number is " + str(n) + ", its square is " + str(int(math.pow(n,2))) + " and its cube is " + str(int(math.pow(n,3)))+".")

