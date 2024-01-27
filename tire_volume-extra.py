specs = input("Enter your tires' size here, including the first three-digit number to the two-digit number after the R (e.g. 111/22R33): ")
w, a, d = int(specs[:3]), int(specs[4:6]), int(specs[-2:])
import math
v = round((math.pi * w ** 2 * a * (w * a + 2540 * d)) / 1e10, 2)
print ("Your approximate tire volume is " + str(v) + " liters.")
yn = input('Would you like to buy some tires? Input "y" or "n": ')
if yn == "y":
     global phone
     phone = input("Please enter your phone number. ")
import datetime
txt = open("volumes.txt", "a")
txt.write(datetime.datetime.now().strftime("%m/%d/%Y") + ", " + specs + ", " + str(v) + "L")
if yn == "y":
     txt.write(", " + phone)
txt.write("\n")
txt.close()