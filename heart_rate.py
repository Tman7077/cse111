"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
age = input("Please enter your age: ")
ageNum = int(age)
maxRate = 220 - int(age)
print("When you exercise to strengthen your heart, you should keep your heart rate between " + str(round(0.65*maxRate)) + " and " + str(round(0.85*maxRate)) + " beats per minute.")