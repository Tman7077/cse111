specs = input("Enter your tires' size here, including the first three-digit number to the two-digit number after the R (e.g. 111/22R33): ")
w, a, d = int(specs[:3]), int(specs[4:6]), int(specs[-2:])
#output = "w = {}, a = {}, d = {}."
#print(output.format(w, a, d))
import math
v = round((math.pi * w ** 2 * a * (w * a + 2540 * d)) / 1e10, 2)
print ("Your approximate tire volume is " + str(v) + " liters.")