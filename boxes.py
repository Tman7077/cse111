items = round(float(input("How many items do you need to pack?:")))
ipb = round(float(input("Thanks! How many of your " + str(items) + " items will you put in each box? ")))
import math
boxes = math.ceil(items/ipb)
print("Great. You'll need " + str(boxes) + " boxes.")