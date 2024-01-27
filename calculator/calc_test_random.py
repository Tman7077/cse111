from tkinter import *
import tkinter.font as tkf

def main():
     root = Tk()
     
     # root.bind("<KeyPress>", keypress_handler)
     # def keypress_handler(e):
     #      print(e)

     # ans = float(9*(10**15) + 999999999999998)
     # print(ans)
     # print(type(ans))
     
     dumb_font = tkf.Font(family="Product Sans", size=17)
     print(dumb_font.measure('984124542611519548251345687'))

     root.mainloop()

if __name__ == "__main__":
     main()