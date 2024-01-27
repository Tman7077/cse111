from tkinter import *
import tkinter.font as tkfont

def main():
     # Creates the window.
     root = Tk()
     # Calls make_gui with root
     make_gui(root)
     # root.mainloop() is just a backbone "make everything work"
     # function req.d for all tkinter windows.
     root.mainloop()

# Creates the window, including all text, fields, and buttons.
# Parameter root references root in line 6, aka the window itself
# in which to create all of the widgets.
def make_gui(root):
     # making_gui is true from the start of this function to the end of it,
     # and is checked at the start of every function call to ensure
     # that those functions don't get accidentally called when creating each button.
     global making_gui
     making_gui = True

     # Sets the window's title, width, and height
     root.title("Calculator by Tyler")
     window_w, window_h = 350, 500
     root.geometry(f'{window_w}x{window_h}')
     
     # minsize is the smallest size allowed for the window
     root.minsize(window_w, window_h)
     
     # configures the rows and columns, allowing the buttons to resize 
     # based on the size of the window
     for i in range(2):
          Grid.rowconfigure(root, i, minsize=window_h/20)
     for i in range(2, 8):
          Grid.rowconfigure(root, i, weight=1, minsize=window_h/10)
     for i in range(4):
          Grid.columnconfigure(root, i, weight=1, minsize=window_h/8)

     # display_font is the font used throughout the program,
     # display_font_past is a smaller version used solely for past_label below
     global display_font
     display_font = tkfont.Font(family="Times New Roman", size=14)
     display_font_past = tkfont.Font(family="Times New Roman", size=10)

     # past_text and current_text are special tkinter StringVar variables,
     # made to be accessed and set so that every time they change,
     # they can update the user-visible text they contain.
     # is_ans is a boolean for my own sanity, its use will be apparent later
     global past_text, current_text, is_ans
     is_ans = False

     # past_text and current_text display in the current calculator number field
     # and the smaller text above it, respectively.
     past_text = StringVar(root, "")
     current_text = StringVar(root, "")

     # Label() widgets (set as variables) just show text (small text that 
     # appears above the calculator number entry). __variable__.grid() places
     # it in a grid of widgets in the user-facing window (e.g. row 0 col 0 is top left)
     past_label = Label(root, font=display_font_past, anchor=E, textvariable=past_text)
     past_label.grid(row=0, column=0, columnspan=4, sticky=N+E+W)

     # Entry() variables take text input from the user -- I used an entry in hopes that
     # I can later take user input from the number keys on their keyboard. This may change
     # because it is currently possible for them to also input letters.
     input_box = Entry(root, font=display_font, borderwidth=5, justify=RIGHT, state=DISABLED, 
               disabledforeground="#000000", textvariable=current_text)
     input_box.grid(row=1, column=0, columnspan=4, padx=0, pady=2, sticky=N+E+W)

     # button_dict is a dict organized as follows:
     # "button_name": ["button_text", button_command(), row_index, col_index]
     # where the name will become a variable in the local symbols table,
     # the text displays on the button, the command is the function
     # that the button calls when pressed, and the row and column indices
     # are where that button is gridded in the user-facing window.

     # Comments in button_dict mark an empty spot in that row
     # (each 4 lines are one row of 4 buttons).
     # It need not be spaced and organized like this, nor even
     # in this or any order, it only is for my sanity.
     button_dict = {
          
          #
          "button_clear_entry": ["CE", clr, 2, 1, "Control-KeyPress-BackSpace"],
          "button_clear": ["C", lambda: clr(-1,True), 2, 2, "Control-Shift-KeyPress-BackSpace"],
          "button_backspace": ["⌫", lambda: clr(1), 2, 3, "KeyPress-BackSpace"],
          
          #
          #
          #
          "button_divide": ["÷", lambda: symbol("÷"), 3, 3, ["KeyPress-slash", "KeyPress-KP_Divide"]],
          
          "button_7": ["7", lambda: button_num(7), 4, 0, ["KeyPress-7", "KeyPress-KP_7"]],
          "button_8": ["8", lambda: button_num(8), 4, 1, ["KeyPress-8", "KeyPress-KP_8"]],
          "button_9": ["9", lambda: button_num(9), 4, 2, ["KeyPress-9", "KeyPress-KP_9"]],
          "button_multiply": ["×", lambda: symbol("×"), 4, 3, ["KeyPress-x", "KeyPress-asterisk", "KeyPress-KP_Multiply"]],
          
          "button_4": ["4", lambda: button_num(4), 5, 0, ["KeyPress-4", "KeyPress-KP_4"]],
          "button_5": ["5", lambda: button_num(5), 5, 1, ["KeyPress-5", "KeyPress-KP_5"]],
          "button_6": ["6", lambda: button_num(6), 5, 2, ["KeyPress-6", "KeyPress-KP_6"]],
          "button_subtract": ["-", lambda: symbol("-"), 5, 3, ["minus", "KP_Subtract"]],
          
          "button_1": ["1", lambda: button_num(1), 6, 0, ["KeyPress-1", "KeyPress-KP_1"]],
          "button_2": ["2", lambda: button_num(2), 6, 1, ["KeyPress-2", "KeyPress-KP_2"]],
          "button_3": ["3", lambda: button_num(3), 6, 2, ["KeyPress-3", "KeyPress-KP_3"]],
          "button_add": ["+", lambda: symbol("+"), 6, 3, ["KeyPress-plus", "KeyPress-KP_Add"]],
          
          "button_negate": ["±", negate, 7, 0, "KeyPress-backslash"],
          "button_0": ["0", lambda: button_num(0), 7, 1, ["KeyPress-0", "KeyPress-KP_0"]],
          "button_decimal": [".", lambda: button_num("."), 7, 2, ["KeyPress-period", "KeyPress-KP_Decimal"]],
          "button_equals": ["=", equals, 7, 3, ["KeyPress-equals", "KeyPress-Return", "KeyPress-KP_Enter", "KeyPress-KP_Equal"]]
     }
     global kp_dict
     kp_dict = {
               #
               "Control-KeyPress-BackSpace": 'clr',
               "Control-Shift_L-KeyPress-BackSpace": 'clr(-1,True)',
               "BackSpace": 'clr(1)',
               
               #
               #
               #
               "KP_Divide": 'symbol("÷")',
                    "slash": 'symbol("÷")',
               
               "KP_7": 'button_num(7)',
                    "7": 'button_num(7)',
               "KP_8": 'button_num(8)',
                    "8": 'button_num(8)',
               "KP_9": 'button_num(9)',
                    "9": 'button_num(9)',
               "KP_Multiply": 'symbol("×")',
                    "x": 'symbol("×")',
                    "asterisk": 'symbol("×")',

               "KP_4": 'button_num(4)',
                    "4": 'button_num(4)',
               "KP_5": 'button_num(5)',
                    "5": 'button_num(5)',
               "KP_6": 'button_num(6)',
                    "6": 'button_num(6)',
               "KP_Subtract": 'symbol("-")',
                    "minus": 'symbol("-")',

               "KP_2": 'button_num(2)',
                    "2": 'button_num(2)',
               "KP_2": 'button_num(2)',
                    "2": 'button_num(2)',
               "KP_3": 'button_num(3)',
                    "3": 'button_num(3)',
               "KP_Add": 'symbol("+")',
                    "Shift_L-equals": 'symbol("+")',

               "backslash": 'negate',
               "KP_0": 'button_num(0)',
                    "0": 'button_num(0)',
               "period": 'button_num(".")',
                    "KP_Decimal": 'button_num(".")',
               "equals": 'equals', 
                    "Return": 'equals',
                    "KP_Enter": 'equals',
                    "KP_Equal": 'equals'
          }
     
     for button in button_dict.keys():
          # creates a variable based on the key (buttton name) in button_dict
          locals().update({button: None})
          # variables for clarity in the next line
          btext = button_dict[button][0]
          bcommand = button_dict[button][1]
          brow = button_dict[button][2]
          bcol = button_dict[button][3]
          # locals()[button] translates to var_name for assigning (e.g. -- x -- = 1).
          # I did it this way so I could loop through it.
          # Button() widgets are, you guessed it, buttons.
          # This line sets the value of the variable for the button created above
          # to a button widget with the correct font, cursor on hover, text, and command.
          locals()[button] = Button(root, font=display_font, cursor="hand2", text=btext, command=bcommand)
          # eval(button) essentially tells Python I want the variable with name
          # button_name, not the text string "button_name" to be gridded, then
          # this line grids it.
          eval(button).grid(row=brow, column=bcol, sticky="nesw")

          bbind = button_dict[button][4]
          if isinstance(bbind, list):
               for i in range(len(bbind)):
                    root.event_add(f'<<press_{button}_key_{i}>>', bbind[i])
          elif isinstance(bbind, str):
               root.event_add(f'<<press_{button}>>', f'<{bbind}>')
          else:
               raise TypeError
          root.bind(f'<<press_{button}>>', keypress_handler)

     # btest = Button(root, font=display_font, cursor="hand2", text="Test", command=lambda: button_num(123))
     # btest.grid(row=3, column=0, sticky="nesw")

     # sets making_gui to False to allow the below functions to work.
     making_gui = False

def keypress_handler(event):
     global making_gui, kp_dict
     if not making_gui:
          eval(kp_dict[event.keysym])

# Called by buttons 0-9 and the decimal.
# argument num is the number 0-9 or "." passed by the caller
def button_num(num, event=None):
     # (Same for all button functions:
     # if not making the gui, execute the function,
     # else don't, because it will fail.)
     global making_gui
     if not making_gui:
          # is_ans is a clarifier that determines whether the user's
          # next number input should override what is currently being displayed
          # or should append it. Say you type 1 + 2 =, the calculator displays 3,
          # but if you then press 4, you want it to say 4, not 34. This
          # catches that. 3 is the answer, therefore if they next enter a number
          # instead of an operator (4 instead of +), clear the screen then enter their text.
          global is_ans
          if is_ans == True:
               clr()
               is_ans = False
          # This block should never NOT activate. It's just a confirmation that
          # the argument was passed correctly, so when I make a mistake, the button
          # just does nothing, it doesn't crash instead.
          if str(num).isdigit() or (num == "." and num not in current_text.get()):
               # If there's nothing on the screen and the user presses the decimal,
               # enter "0."
               if current_text.get() == "" and num == ".":
                    current_text.set("0.")
               # If 0 is on the screen and the user presses a number,
               # replace the 0 with that number
               elif current_text.get() == "0":
                    current_text.set(str(num))
               # Otherwise, append the number/decimal.
               else:
                    current_text.set(current_text.get() + str(num))

# Called by ÷, ×, -, and +
def symbol(sym, event=None):
     global making_gui
     if not making_gui:
          # If there is no equation in past_text,
          # aka this is the first symbol the user has entered
          # in this equation
          if past_text.get() == "":
               # If the last digit the user entered was a decimal,
               # get rid of it and set past text to:
               # the number in current_text, a space (important),
               # and the symbol the user entered.
               if current_text.get()[-1:] == ".":
                    past_text.set(f'{current_text.get()[:-1]} {sym}')
               # Otherwise, do the above but don't get rid of the last character.
               else:
                    past_text.set(f'{current_text.get()} {sym}')
               # Call clr() with no parameters (explained below).
               clr()
          # If there is an equation in past_text, but NOT anything in current text,
          # set past_text to what it was, but change to the symbol pressed,
          # e.g. if past_text == "123 +" and symbol == ×:
          # past_text = "123 ×"
          elif current_text.get() == "":
               past_text.set(f'{past_text.get()[:-1]}{sym}')
          # If there is an equation in past_text AND text in current_text,
          # call equals() (below) then re-call this function with 
          # its original parameter. One of the above ifs will catch it
          # after calling equals, so this will not loop.
          else:
               equals()
               symbol(sym)

# Only called by the ± button
def negate(event=None):
     global making_gui
     if not making_gui:
          global is_ans
          # "-" will only be in CURRENT_text if it is negative.
          # therefore, if "-" is in current_text, get rid of it,
          # if it is not, add it to the beginning.
          if "-" not in current_text.get():
               current_text.set("-" + current_text.get())
          else:
               current_text.set(current_text.get()[1:])
          # In case this button was pressed while the text in
          # current_text was an answer, make it no longer an
          # answer. This isn't strictly necessary, but I chose to add it.
          is_ans = False

# Called by the = button AND by an operator if there is text
# in both past_text and current_text.
def equals(event=None):
     global making_gui
     if not making_gui:
          # set past_eq and current_num to the current values
          # of past_text and current_text. This is necessary because
          # tkinter's StringVar type is not referenceable like
          # regular variables are, this is just a simpler way around it
          # for the purpose of this function.
          past_eq = past_text.get()
          current_num = current_text.get()
          # The user could enter a negative symbol with no numbers,
          # this catches that and essentially disables the button
          # when that is the case
          if current_num == "-":
               return
          # If there is something in past_eq,
          # concatenate it (with a space) with current_num.
          if past_eq != "":
               eq = f'{past_eq} {current_num}'
          # This will only activate if the equals button is pressed after
          # only entering a number and nothing else (e.g. 3 =), and sets
          # the equation to be processed below to number + 0
          # for simplicity.
          else:
               eq = f'{current_num} + 0'

          # Split the equation by its spaces into a three-part list:
          # number, symbol, number (all strings for now).
          eq_parts_preparsed = eq.split(" ")
          
          # Creates an empty list to be appended below.
          eq_parts_parsed = []
          # This loop is necessary in case the first and second numbers
          # are the same. It's convoluted but functional.
          for item in eq_parts_preparsed:
               # Get the index of the item in the list
               ind = eq_parts_preparsed.index(item)
               # Insert string "abc" for disambiguity at the index of item
               eq_parts_preparsed.insert(ind, "abc")
               # pop the original item out of the list.
               eq_parts_preparsed.pop(ind + 1)
               # To this point, eq_parts_preparsed would have gone from
               # ["123", "+", "456"] to ["abc", "+", "456"].

               # If the item without any instances of "." and "-" is a digit,
               # aka if it's not an operator, convert it to a float (incl.
               # negative and decimal) and add it at its appropriate index
               # into eq_parts_parsed.
               if str(item).replace(".","").replace("-","").isdigit():
                    eq_parts_parsed.insert(ind, float(item))
               # If not the above, aka if it is an operator, add it to
               # eq_parts_parsed as a string.
               else:
                    eq_parts_parsed.insert(ind, item)
          
          # Get the operator
          operator = eq_parts_parsed[1]

          if operator == "÷":
               # Account for dividing by zero
               if eq_parts_parsed[2] == 0:
                    answer = 'Err'
               # set answer to first number divided by second number
               else:
                    answer = eq_parts_parsed[0] / eq_parts_parsed[2]
          elif operator == "×":
               # set answer to first number multiplied by second number
               answer = eq_parts_parsed[0] * eq_parts_parsed[2]
          elif operator == "-":
               # set answer to first number minus second number
               answer = eq_parts_parsed[0] - eq_parts_parsed[2]
          elif operator == "+":
               # set answer to first number plus second number
               answer = eq_parts_parsed[0] + eq_parts_parsed[2]

          # If answer is an int, display it as an int,
          # getting rid of the .0 because it's unnecessary
          if answer == int(answer):
               current_text.set(int(answer))
          # If it's a float, display it as a float.
          else:
               current_text.set(answer)
          
          global is_ans
          # This is an answer to an equation, set is_ans accordingly.
          is_ans = True
          # call clr() with parameters (explained below).
          clr(0, True)

# Called in many places, not just buttons.
# Clears one or all characters from current_text
# and/or past_text.
# Parameter amt is the amount of text to clear from current_text.
# Parameter past is whether or not to clear past_text.
def clr(amt=-1, past=False, event=None):
     global making_gui
     if not making_gui:
          # if amt == -1, clear all from current_text.
          if amt == -1:
               current_text.set("")
          # if amt == 1, clear the end character from current_text (backspace).
          elif amt == 1:
               length = len(current_text.get())
               current_text.set(current_text.get()[:length - 1])
          # else (otherwise, if amt == 0), do not clear current_text.
          else:
               pass
          
          # if past == True, clear past_text.
          if past == True:
               past_text.set("")

if __name__ == "__main__":
     main()