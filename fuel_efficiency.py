def main():
     # Get an odometer value in U.S. miles from the user.
     start_mi = float(input("What did your odometer start at? "))
     # Get another odometer value in U.S. miles from the user.
     end_mi = float(input("What did your odometer end at? "))
     # Get a fuel amount in U.S. gallons from the user.
     gal = float(input("How much fuel did you use? "))
     # Call the miles_per_gallon function and store
     # the result in a variable named mpg.
     mpg = f_mpg(start_mi, end_mi, gal)
     # Call the lp100k_from_mpg function to convert the
     # miles per gallon to liters per 100 kilometers and
     # store the result in a variable named lp100k.
     lp100k = f_lp100k(mpg)
     # Display the results for the user to see.
     print(f'{mpg:.2f} mpg\n{lp100k:.2f} L per 100 k\nHappy driving!')
def f_mpg(start_miles, end_miles, amount_gallons):
     return (end_miles - start_miles) / amount_gallons
def f_lp100k(mpg):
     return 235.215/mpg
main()