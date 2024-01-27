import datetime
day = datetime.datetime.now().strftime("%w")
subt1 = "{:.2f}".format(float(input("What is your subtotal? ")))
if (day == "2" or day == "3") and float(subt1) >= 50:
     subt2 = "{:.2f}".format(float(subt1) * 0.9)
     disct = "{:.2f}".format(float(subt1) * 0.1)
else:
     subt2 = "{:.2f}".format(float(subt1))
#subt1 = "{:.2f}".format(subt1)
total = "{:.2f}".format(float(subt2) * 1.06)
for_lengths = [str(subt1), str(subt2), str(disct), str(total)]
len_longest = int(float(len(max(for_lengths, key=len))))
print("len_longest = " + str(len_longest))
print_subt1 = " " * (len_longest - len(subt1)) + subt1
print_disct = " " * (len_longest - len(disct)) + disct
print_subt2 = " " * (len_longest - len(subt2)) + subt2
print_total = " " * (len_longest - len(total)) + total
print(print_subt1)
if float(disct) != 0:
     print(f'-{print_disct}\n{len_longest * "-"}\n{print_subt2}')

print(f'{len_longest * "-"}\n{print_total}')