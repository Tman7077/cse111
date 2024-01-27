import calc as c
from calc import *
from tkinter import *
import pytest, random

c.making_gui = False
c.is_ans = False
c.past_text = StringVar(root, "")
c.current_text = StringVar(root, "")
c.label_font = tkfont.Font(family="Product Sans", size=32)
c.il_frame = Frame(root, height=60)
c.button_sq = Button(root)

'''
I talked to Brother Olaveson, and he told me there's not
exactly a good way to test GUIs in Pytest. I don't know of a way either,
so I am omitting the testing of make_gui, configure_window,
color_mode_switch, and keypress_handler, which make or handle the GUI,
except for keypress_handler which just assigns keypresses to call the
functions tested below.
'''

def test_append_text():
     for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "."]:
          c.past_text.set(""); c.current_text.set("")
          append_text(num)
          if isinstance(num, int):
               assert c.current_text.get() == f'{num}'
          else:
               assert c.current_text.get() == '0.'

def test_symbol():
     for _ in range(10):
          r1 = random.uniform(-(2**10), 2**10)

          # Test appending operators
          c.past_text.set(""); c.current_text.set("")
          c.current_text.set(r1)
          symbol("+")
          assert c.past_text.get() == f'{r1} +'
          assert c.current_text.get() == ""

          c.past_text.set("")
          c.current_text.set(r1)
          symbol("-")
          assert c.past_text.get() == f'{r1} -'
          assert c.current_text.get() == ""

          c.past_text.set("")
          c.current_text.set(r1)
          symbol("×")
          assert c.past_text.get() == f'{r1} ×'
          assert c.current_text.get() == ""

          c.past_text.set("")
          c.current_text.set(r1)
          symbol("÷")
          assert c.past_text.get() == f'{r1} ÷'
          assert c.current_text.get() == ""

          # Test replacing operators
          c.current_text.set("")

          c.past_text.set(f'{r1} -')
          symbol("+")
          assert c.past_text.get() == f'{r1} +'
          c.past_text.set(f'{r1} ×')
          symbol("+")
          assert c.past_text.get() == f'{r1} +'
          c.past_text.set(f'{r1} ÷')
          symbol("+")
          assert c.past_text.get() == f'{r1} +'
          
          c.past_text.set(f'{r1} +')
          symbol("-")
          assert c.past_text.get() == f'{r1} -'
          c.past_text.set(f'{r1} ×')
          symbol("-")
          assert c.past_text.get() == f'{r1} -'
          c.past_text.set(f'{r1} ÷')
          symbol("-")
          assert c.past_text.get() == f'{r1} -'

          c.past_text.set(f'{r1} +')
          symbol("×")
          assert c.past_text.get() == f'{r1} ×'
          c.past_text.set(f'{r1} -')
          symbol("×")
          assert c.past_text.get() == f'{r1} ×'
          c.past_text.set(f'{r1} ÷')
          symbol("×")
          assert c.past_text.get() == f'{r1} ×'

          c.past_text.set(f'{r1} +')
          symbol("÷")
          assert c.past_text.get() == f'{r1} ÷'
          c.past_text.set(f'{r1} -')
          symbol("÷")
          assert c.past_text.get() == f'{r1} ÷'
          c.past_text.set(f'{r1} ×')
          symbol("÷")
          assert c.past_text.get() == f'{r1} ÷'

          # Test using multiple operators
          r2 = random.uniform(-(2**10), 2**10)
          c.past_text.set(""); c.current_text.set("")

          c.past_text.set(f'{r1} +'); c.current_text.set(f'{r2}')
          symbol("+")
          assert c.past_text.get() == f'{r1} + {r2} +'
          assert c.current_text.get() == ""

          c.past_text.set(f'{r1} -'); c.current_text.set(f'{r2}')
          symbol("-")
          assert c.past_text.get() == f'{r1} - {r2} -'
          assert c.current_text.get() == ""

          c.past_text.set(f'{r1} ×'); c.current_text.set(f'{r2}')
          symbol("×")
          assert c.past_text.get() == f'{r1} × {r2} ×'
          assert c.current_text.get() == ""

          c.past_text.set(f'{r1} ÷'); c.current_text.set(f'{r2}')
          symbol("÷")
          assert c.past_text.get() == f'{r1} ÷ {r2} ÷'
          assert c.current_text.get() == ""

def test_negate():
     for _ in range(10):
          c.past_text.set("")
          r_neg = random.uniform(-(2**10), 0)
          r_pos = random.uniform(0, 2**10)

          # Test getting rid of negative
          c.current_text.set(r_neg)
          negate()
          assert c.current_text.get() == f'{-r_neg}'

          # Test adding negative
          c.current_text.set(r_pos)
          negate()
          assert c.current_text.get() == f'{-r_pos}'

# def test_equals():
     # equals() is already tested, because it is called in symbol()

def test_clr():
     for _ in range(10):
          r1 = random.uniform(-(2**10), 2**10)
          r2 = random.uniform(-(2**10), 2**10)

          # Test clr(-1, False), aka clr()
          c.current_text.set(r1)
          clr()
          assert c.current_text.get() == ""

          # Test clr(1, False), aka clr(1)
          c.current_text.set(r1)
          clr(1)
          assert c.current_text.get() == f'{r1}'[:-1]

          # Test clr(0, True)
          c.current_text.set(r1)
          c.past_text.set(r2)
          clr(0, True)
          assert c.current_text.get() == f'{r1}'
          assert c.past_text.get() == ""

def test_inverse():
      for _ in range(10):
          r1 = random.uniform(-(2**10), 2**10)

          c.current_text.set(r1)
          inverse()
          assert c.current_text.get() == f'{1 / r1}'

def test_sq():
     for _ in range(10):
          r1 = random.uniform(0, 2**10)

          c.current_text.set(r1)
          sq(False)
          assert c.current_text.get() == f'{r1**2}'

          c.current_text.set(r1)
          sq(True)
          assert c.current_text.get() == f'{r1**0.5}'

pytest.main(["-v", "--tb=line", "-rN", __file__])