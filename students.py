import csv

def main():
     students_dict = read_dict("students.csv")
     inp = input("Input an I-Number: ")
     inp = inp.strip()
     if not inp.isdigit():
          inum = inp[:2]
          inp = inp[2:]
          sep = inp[:1]
          inp = inp.replace(sep,"")
          inum += inp
     else:
          inum = inp
     if inum in students_dict.keys():
          print(f'"{inum}": {students_dict[inum]}')
     else:
          print("No such student")



def read_dict(filename):
     """Read the contents of a CSV file into a
     dictionary and return the dictionary.

     Parameters
          filename: the name of the CSV file to read.
     Return: a dictionary that contains
          the contents of the CSV file.
     """
     with open(filename, "rt") as csv_file:
          return_dict = {}
          reader = csv.reader(csv_file)
          next(reader)
          for row in reader:
               return_dict.update({row[0]:row[1]})
     return return_dict

if __name__ == "__main__":
     main()