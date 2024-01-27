import csv

def main():
     try:
          products_dict = read_dict("products.csv", key_column_index)
     except FileNotFoundError as nofile_err:
          print(nofile_err)
     except PermissionError as perm_err:
          print(perm_err)
     else:
          try:
               print("Inkom Emporium")
               print()
               with open("request.csv", "rt") as req_csv:
                    req_reader = csv.reader(req_csv)
                    next(req_reader)
                    items, subt = 0, 0
                    for row in req_reader:
                         key = row[key_column_index]
                         try:
                              item = products_dict[key]
                              print(f'{item[name_column_index]}: {row[1]} @ ${item[price_column_index]}')
                              items += int(row[1])

                              quant = int(row[1])
                              price = float(item[price_column_index])
                              subt += quant * price
                         except KeyError:
                              print(f'Product {key} not found. Not applied to total.')

                    subt = round(subt, 2)
                    print()
                    print(f'Number of items: {items}')
                    print(f'Subtotal: {subt}')
                    print(f'Sales Tax: {round(subt * 0.06, 2)}')
                    print(f'Total: {round(subt * 1.06, 2)}')
                    print()
                    print("Thank you for shopping at the Inkom Emporium.")
                    from datetime import datetime
                    dt = datetime.now()
                    print(f"{dt:%A, %B %d, %Y, %I:%M %p}")
          except FileNotFoundError as fnf_err:
               print(fnf_err)
          except PermissionError as perm_err:
               print(perm_err)

key_column_index = 0
name_column_index = 1
price_column_index = 2

def read_dict(filename, key_column_index):
     """Read the contents of a CSV file into a compound
     dictionary and return the dictionary.

     Parameters
          filename: the name of the CSV file to read.
          key_column_index: the index of the column
               to use as the keys in the dictionary.
     Return: a compound dictionary that contains
          the contents of the CSV file.
     """
     return_dict = {}
     with open(filename, "rt") as prod_csv:
          prod_reader = csv.reader(prod_csv)
          next(prod_reader)
          for row in prod_reader:
               return_dict.update({row[key_column_index]:row})
     return return_dict

if __name__ == "__main__":
     main()