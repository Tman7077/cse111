from tkinter import *
import tkinter.font as tkfont

def main():
     root = Tk()
     make_gui(root)
     root.mainloop()

def make_gui(root):
     root.title("Calculator by Tyler")
     window_w, window_h = 350, 500
     root.geometry(f'{window_w}x{window_h}')
     root.minsize(window_w, window_h)
     for i in range(2):
          Grid.rowconfigure(root, i, minsize=window_h/20)
     for i in range(2, 8):
          Grid.rowconfigure(root, i, weight=1, minsize=window_h/10)
     for i in range(4):
          Grid.columnconfigure(root, i, weight=1, minsize=window_h/8)
     global display_font
     display_font = tkfont.Font(family="Product Sans", size=14)
     display_font_past = tkfont.Font(family="Product Sans", size=10)

     global past_text, current_text, is_ans
     is_ans = False
     past_text = StringVar(root, "")
     current_text = StringVar(root, "")
     past_label = Label(root, font=display_font_past, anchor=E, textvariable=past_text)
     past_label.grid(row=0, column=0, columnspan=4, sticky=N+E+W)
     input_box = Entry(root, font=display_font, borderwidth=5, justify="right", textvariable=current_text)
     input_box.grid(row=1, column=0, columnspan=4, padx=0, pady=2, sticky=N+E+W)

     button_1 = Button(root, font=display_font, cursor="hand2", text="1",
          command=lambda: button_num(1))
     button_1.grid(row=6, column=0, sticky=N+E+S+W)
     button_2 = Button(root, font=display_font, cursor="hand2", text="2",
          command=lambda: button_num(2))
     button_2.grid(row=6, column=1, sticky=N+E+S+W)
     button_3 = Button(root, font=display_font, cursor="hand2", text="3",
          command=lambda: button_num(3))
     button_3.grid(row=6, column=2, sticky=N+E+S+W)

     button_4 = Button(root, font=display_font, cursor="hand2", text="4",
          command=lambda: button_num(4))
     button_4.grid(row=5, column=0, sticky=N+E+S+W)
     button_5 = Button(root, font=display_font, cursor="hand2", text="5",
          command=lambda: button_num(5))
     button_5.grid(row=5, column=1, sticky=N+E+S+W)
     button_6 = Button(root, font=display_font, cursor="hand2", text="6",
          command=lambda: button_num(6))
     button_6.grid(row=5, column=2, sticky=N+E+S+W)

     button_7 = Button(root, font=display_font, cursor="hand2", text="7",
          command=lambda: button_num(7))
     button_7.grid(row=4, column=0, sticky=N+E+S+W)
     button_8 = Button(root, font=display_font, cursor="hand2", text="8",
          command=lambda: button_num(8))
     button_8.grid(row=4, column=1, sticky=N+E+S+W)
     button_9 = Button(root, font=display_font, cursor="hand2", text="9",
          command=lambda: button_num(9))
     button_9.grid(row=4, column=2, sticky=N+E+S+W)

     button_0 = Button(root, font=display_font, cursor="hand2", text="0",
          command=lambda: button_num(0))
     button_0.grid(row=7, column=1, sticky=N+E+S+W)

     button_negate = Button(root, font=display_font, cursor="hand2", text="±",
          command=negate)
     button_negate.grid(row=7, column=0, sticky=N+E+S+W)
     button_decimal = Button(root, font=display_font, cursor="hand2", text=".",
          command=lambda: button_num("."))
     button_decimal.grid(row=7, column=2, sticky=N+E+S+W)

     button_divide = Button(root, font=display_font, cursor="hand2", text="÷",
          command=lambda: symbol("÷"))
     button_divide.grid(row=3, column=3, sticky=N+E+S+W)
     button_multiply = Button(root, font=display_font, cursor="hand2", text="×",
          command=lambda: symbol("×"))
     button_multiply.grid(row=4, column=3, sticky=N+E+S+W)
     button_subtract = Button(root, font=display_font, cursor="hand2", text="-",
          command=lambda: symbol("-"))
     button_subtract.grid(row=5, column=3, sticky=N+E+S+W)
     button_add = Button(root, font=display_font, cursor="hand2", text="+",
          command=lambda: symbol("+"))
     button_add.grid(row=6, column=3, sticky=N+E+S+W)

     button_backspace = Button(root, font=display_font, cursor="hand2", text="⌫",
          command=lambda: clr(1))
     button_backspace.grid(row=2, column=3, sticky=N+E+S+W)
     button_clear = Button(root, font=display_font, cursor="hand2", text="C",
          command=lambda: clr(-1,"y"))
     button_clear.grid(row=2, column=2, sticky=N+E+S+W)
     button_clear_entry = Button(root, font=display_font, cursor="hand2", text="CE",
          command=clr)
     button_clear_entry.grid(row=2, column=1, sticky=N+E+S+W)
     button_equals = Button(root, font=display_font, cursor="hand2", text="=",
          command=equals)
     button_equals.grid(row=7, column=3, sticky=N+E+S+W)

def button_num(num):
     global is_ans
     if is_ans == True:
          clr()
          is_ans = False
     if str(num).isdigit() or (num == "." and num not in current_text.get()):
          if current_text.get() == "" and num == ".":
               current_text.set("0.")
          elif current_text.get() == "0":
               current_text.set(str(num))
          else:
               current_text.set(current_text.get() + str(num))


def symbol(sym):
     if past_text.get() == "":
          if current_text.get()[-1:] == ".":
               past_text.set(f'{current_text.get()[:-1]} {sym}')
          else:
               past_text.set(f'{current_text.get()} {sym}')
          clr()
     elif current_text.get() == "":
          past_text.set(f'{past_text.get()[:-1]}{sym}')
     else:
          equals()
          symbol(sym)

def negate():
     global is_ans
     if "-" not in current_text.get():
          current_text.set("-" + current_text.get())
     else:
          current_text.set(current_text.get()[1:])
     is_ans = False

def equals():
     past_eq = past_text.get()
     current_num = current_text.get()
     if current_num == "-":
          return
     if past_eq != "":
          eq = f'{past_eq} {current_num}'
     else:
          eq = f'{current_num} + 0'
     eq_parts_preparsed = eq.split(" ")
     
     eq_parts_parsed = []
     for item in eq_parts_preparsed:
          ind = eq_parts_preparsed.index(item)
          eq_parts_preparsed.insert(ind, "abc")
          eq_parts_preparsed.pop(ind + 1)
          if str(item).replace(".","").replace("-","").isdigit():
               eq_parts_parsed.insert(ind, float(item))
          else:
               eq_parts_parsed.insert(ind, item)
     
     operator = eq_parts_parsed[1]

     if operator == "÷":
          if eq_parts_parsed[2] == 0:
               answer = 'Err'
          else:
               answer = eq_parts_parsed[0] / eq_parts_parsed[2]
     elif operator == "×":
          answer = eq_parts_parsed[0] * eq_parts_parsed[2]
     elif operator == "-":
          answer = eq_parts_parsed[0] - eq_parts_parsed[2]
     elif operator == "+":
          answer = eq_parts_parsed[0] + eq_parts_parsed[2]

     if answer == int(answer):
          current_text.set(int(answer))
     else:
          current_text.set(answer)
     
     global is_ans
     is_ans = True
     clr(0, "y")


def clr(amt=-1, past="n"):
     if amt == -1:
          current_text.set("")
     elif amt == 1:
          length = len(current_text.get())
          current_text.set(current_text.get()[:length - 1])
     else:
          pass
     
     if past == "y":
          past_text.set("")

if __name__ == "__main__":
     main()