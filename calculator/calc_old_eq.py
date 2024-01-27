from tkinter import *
import tkinter.font as tkfont
import sys, os

# Creates the window.
root = Tk()
rt = True

# Creates the window, including all text and buttons.
# Parameter root is the window in which to create all of the widgets.
def make_gui():
     global root

     ''' making_gui is true from the start of this function to the end of it,
     and is checked at the start of every function call to ensure
     that those functions don't get accidentally called when creating each button.'''
     global making_gui
     making_gui = True

     # Define some color palettes
     black = "#000000"
     white = "#ffffff"
     dark_colors = {
          "bg" : "#21201e",
          "fg" : white,
          "afg": black,
          "op" : "#333231",
          "num": "#3d3b39",
          "eq" : "#a6a5a1",
     }
     light_colors = {
          "bg" : "#f6f2ee",
          "fg" : black,
          "afg": white,
          "op" : "#fbf8f6",
          "num": "#ffffff",
          "eq" : "#413f3d"
     }
     blue_colors = {
          "bg" : "#011f4b",
          "fg" : white,
          "afg": "#011f4b",
          "op" : "#03396c",
          "num": "#005b96",
          "eq" : "#b3cde0"
     }
     sepia_colors = {
          "bg" : "#b38b67",
          "fg" : white,
          "afg": "#634832",
          "op" : "#c89f73",
          "num": "#d9b380",
          "eq" : "#fbe7a1"
     }
     peach_colors = {
          "bg" : "#f6a192",
          "fg" : "#c14b4b",
          "afg": white,
          "op" : "#f6c492",
          "num": "#f6d992",
          "eq" : "#f98787"
     }
     green_colors = {
          "bg" : "#317256",
          "fg" : white,
          "afg": white,
          "op" : "#398564",
          "num": "#419873",
          "eq" : "#52bf90"
     }
     global cp, cps
     cp = dark_colors
     cps = ["dark_colors", "light_colors", "blue_colors",
          "sepia_colors", "peach_colors", "green_colors"]
     for p in cps:
          globals().update({p: eval(p)})

     # Sets the window's title, width, and height
     root.title("Calculator by Tyler")
     global screen_w, screen_h, root_default_w, root_default_h
     screen_w = root.winfo_screenwidth()
     screen_h = root.winfo_screenheight()
     root_default_w, root_default_h = int(screen_w / 6), int(screen_h / 2.25)
     root.geometry(f'{root_default_w}x{root_default_h}') # on a 1920x1080 screen, 320x480
     
     # minsize is the smallest size allowed for the window
     root.minsize(root_default_w, root_default_h)

     # Configure root background color
     root.config(bg=cp["bg"])

     # Configures the rows and columns, allowing the buttons to resize 
     # based on the size of the window
     for i in range(2):
          Grid.rowconfigure(root, i, weight=1, minsize=root_default_h / 8)
     Grid.rowconfigure(root, 2, weight=12, minsize=root_default_h * 3/4)
     for i in range(2):
          Grid.columnconfigure(root, i, weight=1, minsize=root_default_h/8)

     # Define some fonts used
     global button_font, label_font, label_font_small
     button_font = tkfont.Font(family="Product Sans", size=18)
     label_font = tkfont.Font(family="Product Sans", size=32)
     label_font_small = tkfont.Font(family="Product Sans", size=12)

     # Make any window resizing call configure_window(),
     # which is used to resize text based on window size.
     root.bind("<Configure>", configure_window)

     ''' past_text and current_text are special tkinter StringVar variables,
     made to be accessed and set so that every time they change,
     they can update the user-visible text they contain.
     is_ans is a boolean for my own sanity, its use will be apparent later'''
     global past_text, current_text, is_ans
     is_ans = False

     # past_text and current_text display in the current calculator number field
     # and the smaller text above it, respectively.
     past_text = StringVar(root, "")
     current_text = StringVar(root, "")

     ''' Label() widgets (set as variables) just show text.
     Button() widgets are self-explanatory.
     Frame() widgets are containers for other widgets.
     Menu() widgets display a list of options, accessed by
     Menubutton() widgets.
     __variable__.grid() places that widget in a grid
     in the user-facing window (e.g. row 0 col 0 is top left).'''

     # color_palette_button is a button to switch between color palettes.
     global color_palette_button, color_palette_text
     color_palette_text = StringVar(root, "🎨")
     color_palette_button = Menubutton(root, font=button_font, textvariable=color_palette_text,
          bg=cp["bg"], fg=cp["fg"], width=2, cursor="hand2", justify=CENTER, bd=0,
          activebackground=cp["eq"], activeforeground=cp["afg"], direction=RIGHT)
     color_palette_button.grid(row=0, column=0, sticky="nw")
     color_palette_button.menu = Menu(color_palette_button, cursor="hand2", font=label_font_small, tearoff=0,
          bg=cp["bg"], fg=cp["fg"], bd=0, relief=FLAT,
          activebackground=cp["eq"], activeforeground=cp["afg"])
     color_palette_button["menu"] = color_palette_button.menu

     i = 0
     for palette in cps:
          lbl = palette[:palette.index("_")].capitalize()
          p = eval(palette)
          cmd = f'lambda: change_color_palette({i})'; i += 1
          color_palette_button.menu.add_command(label=lbl, command=eval(cmd),
               background=p["bg"], foreground=p["fg"], activebackground=p["eq"], activeforeground=p["afg"])

     # past_label is the secondary, smaller number field.
     global past_label
     past_label = Label(root, font=label_font_small, anchor=E, textvariable=past_text,
          bg=cp["bg"], fg=cp["fg"])
     past_label.grid(row=0, column=1, sticky="new")

     # il_frame just contains input_label, its purpose is to
     # lock the height of input_label, no matter the contents.
     global il_frame
     il_frame= Frame(root, cursor="hand2", height=root_default_h / 8,
          bg=cp["bg"])
     il_frame.grid(row=1, column=0, columnspan=2, padx=0, pady=2, sticky="new")
     il_frame.pack_propagate(0)

     # input_label is the main number field.
     global input_label
     input_label = Label(il_frame, font=label_font, anchor=E, textvariable=current_text,
          bg=cp["bg"], fg=cp["fg"])
     input_label.pack(fill="both")

     # b_frame is a container for all of the math buttons
     global b_frame
     b_frame = Frame(root, cursor="hand2", padx=3, pady=3,
          bg=cp["bg"])
     b_frame.grid(row=2, column=0, columnspan=2, sticky="nesw")

     # As above, configuring root row/cols, configure the frame's rows/cols
     for i in range(4):
          Grid.columnconfigure(b_frame, i, weight=1, minsize=root_default_w/4 - 5)
     for i in range(6):
          Grid.rowconfigure(b_frame, i, weight=1, minsize=root_default_h/8 - 5)

     ''' button_dict is a dict organized as follows:
     "button_name": ["button_text", button_command(), row_index, col_index, button_color, keypress]
     where button_name will become a variable in the local symbols table,
     text displays on the button, command is the function
     that the button calls when pressed, row and column indices
     are where that button is gridded in the user-facing window,
     color is the color of the button, and keypress is 
     the Tkinter-readable key(s) the user must press to 
     activate that button's function (if None, no bound key).

     Comments in button_dict mark an empty spot in that row.
     Each 4 lines are one row of 4 buttons.
     If a group has 5+ lines, that row has hidden buttons.'''
     global button_dict
     button_dict = {
          "button_power": ["𝑥ⁿ", lambda: symbol("^"), 0, 0, 'cp["op"]', "KeyPress-asciicircum"], # Hidden by default
          "button_sq": ["𝑥²", lambda: sq(), 0, 0, 'cp["op"]', None],
          "button_defaults": ["⇪", lambda: alternate("defs"), 0, 1, 'cp["op"]', None], # Hidden by default
          "button_alternates": ["⇧", lambda: alternate("alts"), 0, 1, 'cp["op"]', None],
          "button_clear_entry": ["CE", clr, 0, 2, 'cp["op"]', "Control-KeyPress-BackSpace"], # Hidden by default
          "button_clear": ["C", lambda: clr(-1,True), 0, 2, 'cp["op"]', "Control-Shift-KeyPress-BackSpace"],
          "button_backspace": ["⌫", lambda: clr(1), 0, 3, 'cp["op"]', "KeyPress-BackSpace"],
          
          "button_inverse": ["⅟𝑥", inverse, 1, 0, 'cp["op"]', None], # Hidden by default
          "button_sqrt": ["√", lambda: sq(rt), 1, 0, 'cp["op"]', None],
          "button_open_par": ["(", lambda: symbol("("), 1, 1, 'cp["op"]', "KeyPress-parenleft"],
          "button_close_par": [")", lambda: symbol(")"), 1, 2, 'cp["op"]', "KeyPress-parenright"],
          "button_divide": ["÷", lambda: symbol("÷"), 1, 3, 'cp["op"]', ["KeyPress-slash", "KeyPress-KP_Divide"]],
          
          "button_7": ["7", lambda: button_num(7), 2, 0, 'cp["num"]', ["KeyPress-7", "KeyPress-KP_7"]],
          "button_8": ["8", lambda: button_num(8), 2, 1, 'cp["num"]', ["KeyPress-8", "KeyPress-KP_8"]],
          "button_9": ["9", lambda: button_num(9), 2, 2, 'cp["num"]', ["KeyPress-9", "KeyPress-KP_9"]],
          "button_multiply": ["×", lambda: symbol("×"), 2, 3, 'cp["op"]', ["KeyPress-x", "KeyPress-asterisk", "KeyPress-KP_Multiply"]],
          
          "button_4": ["4", lambda: button_num(4), 3, 0, 'cp["num"]', ["KeyPress-4", "KeyPress-KP_4"]],
          "button_5": ["5", lambda: button_num(5), 3, 1, 'cp["num"]', ["KeyPress-5", "KeyPress-KP_5"]],
          "button_6": ["6", lambda: button_num(6), 3, 2, 'cp["num"]', ["KeyPress-6", "KeyPress-KP_6"]],
          "button_subtract": ["-", lambda: symbol("-"), 3, 3, 'cp["op"]', ["minus", "KP_Subtract"]],
          
          "button_1": ["1", lambda: button_num(1), 4, 0, 'cp["num"]', ["KeyPress-1", "KeyPress-KP_1"]],
          "button_2": ["2", lambda: button_num(2), 4, 1, 'cp["num"]', ["KeyPress-2", "KeyPress-KP_2"]],
          "button_3": ["3", lambda: button_num(3), 4, 2, 'cp["num"]', ["KeyPress-3", "KeyPress-KP_3"]],
          "button_add": ["+", lambda: symbol("+"), 4, 3, 'cp["op"]', ["KeyPress-plus", "KeyPress-KP_Add"]],
          
          "button_negate": ["±", negate, 5, 0, 'cp["op"]', None],
          "button_0": ["0", lambda: button_num(0), 5, 1, 'cp["num"]', ["KeyPress-0", "KeyPress-KP_0"]],
          "button_decimal": [".", lambda: button_num("."), 5, 2, 'cp["op"]', ["KeyPress-period", "KeyPress-KP_Decimal"]],
          "button_equals": ["=", equals, 5, 3, 'cp["eq"]', ["KeyPress-equal", "KeyPress-Return", "KeyPress-KP_Enter", "KeyPress-KP_Equal"]]
     }

     '''kp_dict (keypress_dict) is organized in the same order as
     button_dict, but serves as keypress_handler()'s 
     disambiguation dict. The dict key denotes the keyboard key,
     and the value denotes the function that should be called.
     e.g. pressing 7 on the keyboard calls symbol(7).
     Commented lines denote an unbound button.
     Indented lines denote a button with multiple bound keypresses.'''
     global kp_dict
     kp_dict = {
               "asciicircum": 'symbol("^")',
               # No bound key (Square)
               # No bound key (Defaults)
               # No bound key (Alternates)
               "CE": 'clr()',
               "C": 'clr(-1,True)',
               "Back": 'clr(1)',
               
               # No bound key (Inverse)
               # No bound key (Square root)
               "parenleft": 'symbol("(")',
               "parenright": 'symbol(")")',
               "slash": 'symbol("÷")',
               
               "7": 'button_num(7)',
               "8": 'button_num(8)',
               "9": 'button_num(9)',
               "x": 'symbol("×")',
                    "asterisk": 'symbol("×")',

               "4": 'button_num(4)',
               "5": 'button_num(5)',
               "6": 'button_num(6)',
               "minus": 'symbol("-")',

               "1": 'button_num(1)',
               "2": 'button_num(2)',
               "3": 'button_num(3)',
               "plus": 'symbol("+")',

               # No bound key (Negate)
               "KP_0": 'button_num(0)',
                    "0": 'button_num(0)',
               "period": 'button_num(".")',
                    "KP_Decimal": 'button_num(".")',
               "Return": 'equals()',
                    "equal": 'equals()'
          }
          
     # Grids the buttons (in b_frame)
     for button in button_dict.keys():
          # creates a variable based on the key (button name) in button_dict
          globals().update({button: None})
          # variables for clarity in the next lines
          btext = button_dict[button][0]
          bcommand = button_dict[button][1]
          brow = button_dict[button][2]
          bcol = button_dict[button][3]
          bcolorbg = eval(button_dict[button][4])
          bbind = button_dict[button][5]

          bcolorfg = cp["fg"]
          if bcolorbg == cp["eq"]:
               bcolorfg = cp["afg"]
          ''' globals()[button] translates to var_name for assigning (e.g. --> x <-- = 1).
          I did it this way so I could loop through it.
          Button() widgets are, you guessed it, buttons.
          This line sets the value of the variable for the button created above
          to a button widget with the correct font, cursor on hover, text, and command.'''
          globals()[button] = Button(b_frame, font=button_font, bg=bcolorbg,
               fg=bcolorfg, text=btext, command=bcommand)
          ''' eval(button) essentially tells Python I want the variable with name
          button_name, not the text string "button_name" to be gridded, then
          this line grids it.'''
          eval(button).grid(row=brow, column=bcol, sticky="nesw")

          if button in ["button_power", "button_clear_entry", "button_inverse", "button_defaults"]:
               eval(button).grid_remove()

          ''' If the button's keypress value in button_dict has
          multiple options, loop through them and bind each key
          to the same function.'''
          if isinstance(bbind, list):
               for i in range(len(bbind)):
                    root.bind(f'<{bbind[i]}>', keypress_handler)
          # if the button's keypress value in button_dict has
          # one option, bind it to its function.
          elif isinstance(bbind, str):
               root.bind(f'<{bbind}>', keypress_handler)
          elif bbind is None:
               pass

     # alts is False for default buttons, True for alternates.
     global alts
     alts = False
     # sets making_gui to False to allow the below functions to work.
     making_gui = False

     ''' This function is useful for pyinstaller (.py -> .exe).
     When pyinstaller creates the EXE file, it doesn't include dependencies
     such as images (e.g. the icon at the top left of the window) *in* the exe.
     it creates a temp directory where those files can be accessed.
     This gets that directory, which will be different for different machines.
     '''
     def full_path(rel_path):
          try:
               # PyInstaller creates a temp folder and stores path in _MEIPASS
               base_path = sys._MEIPASS
          except Exception:
               base_path = os.path.abspath(".")
          return os.path.join(base_path, rel_path)

     # Sets the icon for the window
     try:
          root.iconbitmap(full_path("equals_black.ico"))
     except:
          pass
     # root.mainloop() is the backbone; when this line runs, the window pops up.
     root.mainloop()

# Called by anything that changes current_text (except sq())
# Parameter text is the text to set current_text to
# Parameter max_size is the maximum allowed font size (32 for default window size)
def resize_text(text, max_size=32):
     global label_font
     # Get current width of window
     root_width = root.winfo_width()
     # Get pixel width of the text to be displayed
     text_width = label_font.measure(text)
     # Get pixel height of the text to be displayed
     text_height = label_font.metrics("linespace")
     # Get the height of the label
     label_height = il_frame.cget("height")
     # Get the current font size
     s = label_font.cget("size")
     # Define a pad width
     pad = int(root_width / 8)
     # Define the smallest allowed text size
     min_size = 10

     # if the text string doesn't fit in the allocated space,
     # and the current text size is larger than the minimum
     too_big = (text_width > root_width - pad and s > min_size) or \
          (text_height > label_height)
     # if the text string fits in the allocated space (with extra space),
     # and the current text size is smaller than the maximum
     too_small = text_width < root_width - 1.5*pad and s < max_size
     if too_big:
          # Make the font size smaller until it fits
          while too_big:
               s -= 1
               label_font.config(size=s)
               text_width = label_font.measure(text)
               text_height = label_font.metrics('linespace')
               too_big = (text_width > root_width - pad and s > min_size) or \
                    (text_height > label_height)
     elif too_small:
          # Make the font size bigger until it fits
          while too_small:
               s += 1
               label_font.config(size=s)
               text_width = label_font.measure(text)
               too_small = text_width < root_width - pad and s < max_size
     else:
          # If it's not too big or too small,
          # it's just right! Don't do anything.
          pass

# Called every time something happens in the window (almost)
# Parameter e is unused, but it is passed every time ─ out of my control
def configure_window(e):
     # Get the height of the window. The event (passed on configure)
     # has an attribute .height with this information
     root_height = root.winfo_height()
     # Min and max font sizes (passed to resize_text as max_size)
     min_max_size = 32
     max_max_size = 64

     # Change the height of il_frame to accommodate larger window/text sizes
     global il_frame, root_default_h
     if root_height > root_default_h / 8:
          il_frame.config(height = root_height / 8)
          
     # Get text size based on root height
     text_size = int(root_height / 15)
     if text_size >= min_max_size and text_size <= max_max_size:
          # If it's between the min and max, send it to resize_text
          resize_text(current_text.get(), text_size)
     elif text_size > max_max_size:
          # If it's bigger, send max
          resize_text(current_text.get(), max_max_size)
     elif text_size < min_max_size:
          # If it's smaller, send min
          resize_text(current_text.get(), min_max_size)
     
     
def change_color_palette(pal, r=root):
     if not making_gui:
          global cp, cps
          cp = eval(cps[pal])
          for button in button_dict.keys():
               bg_col = eval(button_dict[button][4])
               fg_col = cp["fg"]
               if bg_col == cp["eq"]:
                    fg_col = cp["afg"]
               eval(button).config(bg=bg_col, fg=fg_col)
          widgets = [color_palette_button, past_label, input_label]
          frames = [b_frame, il_frame]
          bg_col = cp["bg"]
          fg_col = cp["fg"]
          r.config(bg=bg_col)
          for widget in widgets:
               widget.config(bg=bg_col, fg=fg_col)
          color_palette_button.config(activebackground=cp["eq"], activeforeground=cp["afg"])
          for frame in frames:
               frame.config(bg=bg_col)
          
# Called any time a bound key is pressed by the user
# Parameter event is passed by the call itself, via tkinter
def keypress_handler(event):
     if not making_gui:
          ''' Get the symbol of the key pressed,
          e.g. 1, 2, 3, +, -, etc.
          Note: Shift+equals produces "plus",
          just like + on the keypad produces "plus".'''
          keypress = event.keysym
          ''' Backspace is bound in multiple ways:
          Ctrl + Backspace (CE),
          Ctrl + Shift + Backspace (C),
          Backspace (Backspace).
          Thus, it must be filtered because var keypress
          will be "BackSpace" for all three.'''
          if keypress != "BackSpace":
               # Call the function based on the key in kp_dict
               eval(kp_dict[event.keysym])
          else:
               # event.state = modified by control, shift, alt, etc.
               mod = event.state
               # mod 12 is Ctrl + key
               if mod == 12:
                    eval(kp_dict["CE"])
               # mod 12 is Ctrl + Shift + key
               elif mod == 13:
                    eval(kp_dict["C"])
               # mod 8 is key (no mods)
               elif mod == 8:
                    eval(kp_dict["Back"])

# Called by alternate key (⇧/⇪)
# Parameter way is which "way" it's converting:
     # "defs" if converting to default buttons, 
     # "alts" if converting to alternate buttons.
def alternate(way):
     if not making_gui:
          global alts
          if way == "defs":
               for button in ["button_sq", "button_clear", "button_sqrt", "button_alternates"]:
                    eval(button).grid()
               for button in ["button_power", "button_clear_entry", "button_inverse", "button_defaults"]:
                    eval(button).grid_remove()
               alts = False
          elif way == "alts":
               for button in ["button_power", "button_clear_entry", "button_inverse", "button_defaults"]:
                    eval(button).grid()
               for button in ["button_sq", "button_clear", "button_sqrt", "button_alternates"]:
                    eval(button).grid_remove()
               alts = True

# Called by buttons 0-9 and the decimal.
# argument num is the number 0-9 or "." passed by the caller
def button_num(num):
     ''' (Same for all button functions:
     if not making the gui, execute the function,
     else don't, because it will fail.)'''
     if not making_gui:
          ''' is_ans is a clarifier that determines whether the user's
          next number input should override what is currently being displayed
          or should append it. Say you type 1 + 2 =, the calculator displays 3,
          but if you then press 4, you want it to say 4, not 34. This
          catches that. 3 is the answer, therefore if they next enter a number
          instead of an operator (4 instead of +), clear the screen then enter their text.'''
          global is_ans, alts
          if is_ans == True:
               clr()
               is_ans = False
          ''' This block should never NOT activate. It's just a confirmation that
          the argument was passed correctly, so when I make a mistake, the button
          just does nothing, it doesn't crash instead.'''
          if str(num).isdigit() or (num == "." and num not in current_text.get()):
               # If there's nothing on the screen and the user presses the decimal,
               # enter "0."
               if current_text.get() == "" and num == ".":
                    to_set = "0."; resize_text(to_set)
                    current_text.set(to_set)
               # If 0 is on the screen and the user presses a number,
               # replace the 0 with that number
               elif current_text.get() == "0":
                    to_set = str(num); resize_text(to_set)
                    current_text.set(to_set)
               # Otherwise, append the number/decimal.
               else:
                    to_set = current_text.get() + str(num); resize_text(to_set)
                    current_text.set(to_set)

          # Disable the alternate buttons
          alternate("defs")

# Called by ÷, ×, -, +, and x^n buttons
def symbol(sym):
     if not making_gui:
          # Cancel following actions if current_text and past_text are empty
          if current_text.get() == "" and past_text.get() == "":
               return
          ''' If there is no equation in past_text,
          aka this is the first symbol the user has entered
          in this equation.'''
          if past_text.get() == "":
               ''' If the last digit the user entered was a decimal,
               get rid of it and set past text to:
               the number in current_text, a space (important),
               and the symbol the user entered.'''
               if current_text.get()[-1:] == ".":
                    past_text.set(f'{current_text.get()[:-1]} {sym}')
               # Otherwise, do the above but don't get rid of the last character.
               else:
                    past_text.set(f'{current_text.get()} {sym}')
               # Call clr() with no parameters (explained below).
               clr()
          elif current_text.get() == "":
               ''' If there is an equation in past_text, but NOT anything in current text,
               set past_text to what it was, but change to the symbol pressed,
               e.g. if past_text == "123 +" and symbol == ×:
               past_text = "123 ×".'''
               past_text.set(f'{past_text.get()[:-1]}{sym}')
               # Disable the alternate buttons
               alternate("defs")
          else:
               ''' If there is an equation in past_text AND text in current_text,
               call equals() (below) then re-call this function with 
               its original parameter. One of the above ifs will catch it
               after calling equals, so this will not loop.'''
               equals()
               symbol(sym)

# Called by the ± button
def negate():
     if not making_gui:
          global is_ans, alts
          ''' "-" will only be in CURRENT_text if it is negative.
          therefore, if "-" is in current_text, get rid of it,
          if it is not, add it to the beginning.'''
          if "-" not in current_text.get():
               to_set = "-" + current_text.get(); resize_text(to_set)
               current_text.set(to_set)
          else:
               to_set = current_text.get()[1:]; resize_text(to_set)
               current_text.set(to_set)
          ''' In case this button was pressed while the text in
          current_text was an answer, make it no longer an
          answer. This isn't strictly necessary, but I chose to add it.'''
          is_ans = False

          # Disable the alternate buttons
          alternate("defs")

# Called by the = button AND by an operator if there is text
# in both past_text and current_text.
def equals(eq=None):
     def simple(eq):
          # Split the equation by its spaces into a three-part list:
          # number, symbol, number (all strings for now).
          eq_parts_preparsed = eq.split(" ")
          
          # Creates an empty list to be appended below.
          eq_parts_parsed = []
          for item in eq_parts_preparsed:
               # If the item is only digits (not scientific or operator), 
               # convert it to a float and append it to eq_parts_parsed.
               if item.replace(".","").replace("-","").isdigit() or\
                    "e+" in item or "e-" in item:
                    eq_parts_parsed.append(float(item))
               # If scientific
               # elif 1 == 1:
                    # pass
               # If not the above, aka if it is an operator, add it to
               # eq_parts_parsed as a string.
               else:
                    eq_parts_parsed.append(item)

          '''for item in eq_parts_parsed:
               i = eq_parts_parsed.index(item)
               eq_parts_parsed[i] = item.replace("÷", "/").replace("×", "*").replace("^", "**")'''
          # Get the operator
          operator = eq_parts_parsed[1]

          if operator == "÷":
               # Account for dividing by zero
               if eq_parts_parsed[2] == 0:
                    answer = 'err (div/0)'
               # set answer to first number divided by second number
               else:
                    answer = eq_parts_parsed[0] / eq_parts_parsed[2]
          elif operator == "×":
               # set answer to first number multiplied by second number
               try:
                    answer = eq_parts_parsed[0] * eq_parts_parsed[2]
               except OverflowError:
                    answer = "err (too large)"
          elif operator == "-":
               # set answer to first number minus second number
               answer = eq_parts_parsed[0] - eq_parts_parsed[2]
          elif operator == "+":
               # set answer to first number plus second number
               try:
                    answer = eq_parts_parsed[0] + eq_parts_parsed[2]
               except OverflowError:
                    answer = "err (too large)"
          elif operator == "^":
               # set answer to first number to the power of second number
               try:
                    answer = eq_parts_parsed[0] ** eq_parts_parsed[2]
               except OverflowError:
                    answer = "err (too large)"

          # "Handle" complex numbers
          if isinstance(answer, complex):
               answer = "err (complex)"

          # if answer is a number
          if isinstance(answer, float) or isinstance(answer, int):
               # Set current_text to the appropriate value
               # If it should be displayed in scientific notation, do so, else don't
               if answer > 10 ** 12 or answer < -(10 ** 16) or\
                    answer < 10 ** -4 and answer > -(10 ** -4):
                    to_set = float(answer); resize_text(to_set)
                    current_text.set(to_set)
               else:
                    # If the answer is an int, display it as an int
                    if answer == int(answer):
                         to_set = int(answer); resize_text(to_set)
                         current_text.set(to_set)
                    # or if answer is a float
                    else:
                         to_set = answer; resize_text(to_set)
                         current_text.set(to_set)
          # If div/0, too large, or complex, answer is a string (f'err {reason}')
          elif isinstance(answer, str):
               to_set = answer; resize_text(to_set)
               current_text.set(to_set)
     
     def parenthetical():
          pass

     if not making_gui:
          if eq is None:
               # If there is nothing in current_text, cancel the following actions
               if current_text.get() == "":
                    return
               if current_text.get() == "-":
                    ''' The user could enter a negative symbol with no numbers,
                    this catches that and essentially disables the button
                    when that is the case.'''
                    return
               # If there is something in past_text,
               # concatenate it (with a space) with current_text.
               if past_text.get() != "":
                    eq = f'{past_text.get()} {current_text.get()}'
               else:
                    ''' This will only activate if the equals button is pressed after
                    only entering a number and nothing else (e.g. 3 =), and sets
                    the equation to be processed below to number + 0
                    for simplicity.'''
                    eq = f'{current_text.get()} + 0'
                    
               simple(eq)

          global is_ans
          # This is an answer to an equation, set is_ans accordingly.
          is_ans = True
          # call clr() with parameters (explained below).
          clr(0, True)

# Called in many places. Clears one or all characters from current_text and/or past_text.
# Parameter amt is the amount of text to clear from current_text.
# Parameter past is whether or not to clear past_text.
def clr(amt=-1, past=False):
     if not making_gui:
          # if amt is -1, clear all from current_text.
          if amt == -1:
               to_set = ""; resize_text(to_set)
               current_text.set(to_set)
          # if amt is 1, clear the end character from current_text (backspace).
          elif amt == 1:
               # length = len(current_text.get())
               to_set = current_text.get()[:-1]; resize_text(to_set)
               current_text.set(to_set)
          # else (otherwise, if amt == 0), do not clear current_text.
          else:
               pass
          
          # if past is True, clear past_text.
          if past == True:
               past_text.set("")

          # Disable the alternate buttons
          alternate("defs")

# Called by ⅟𝑥
def inverse():
     if not making_gui:
          # if there are numbers in current_text,
          # utilize equals() to inverse the number
          if current_text.get().replace("-", "").replace(".", "") != "":
               past_text.set("1 ÷")
               equals()

# Called by 𝑥² and √
# Parameter rt is True for sqrt, False for sq (sneakily set in line 7 lol)
def sq(rt=False):
     if not making_gui:
          # if there are numbers in current_text
          if current_text.get().replace("-", "").replace(".", "") != "":
               # Call symbol with ^ to set past_text to f'{current_text} ^'
               symbol("^")
               # If squaring, set current_text to 2
               if not rt:
                    current_text.set(2)
               # If square rooting, set current_text to 0.5
               if rt:
                    current_text.set(0.5)
               # Call equals to get answer
               equals()

if __name__ == "__main__":
     make_gui()

'''     TO-DO     '''
# Handle parentheses
# Handle complex numbers?