def main():
     '''
     Here is a list of cans, where there are three parts to each variable, in order:
     1. radius (cm)
     2. height (cm)
     3. cost per can (USD)
     e.g. [6.83, 10.16, 0.28],
     where 6.83 cm is the radius, 10.16cm is the height, and $0.28 is the cost per can.
     '''
     can_1_p  = [6.83, 10.16, 0.28]
     can_1_t  = [7.78, 11.91, 0.43]
     can_2    = [8.73, 11.59, 0.45]
     can_2_5  = [10.32, 11.91, 0.61]
     can_3_c  = [10.79, 17.78, 0.86]
     can_5    = [13.02, 14.29, 0.83]
     can_6z   = [5.40, 8.89, 0.22]
     can_8z_s = [6.83, 7.62, 0.26]
     can_10   = [15.72, 17.78, 1.53]
     can_211  = [6.83, 12.38, 0.34]
     can_300  = [7.62, 11.27, 0.38]
     can_303  = [8.10, 11.11, 0.42]
     
     eff_can_1_p  = calc(can_1_p)
     eff_can_1_t  = calc(can_1_t)
     eff_can_2    = calc(can_2)
     eff_can_2_5  = calc(can_2_5)
     eff_can_3_c  = calc(can_3_c)
     eff_can_5    = calc(can_5)
     eff_can_6z   = calc(can_6z)
     eff_can_8z_s = calc(can_8z_s)
     eff_can_10   = calc(can_10)
     eff_can_211  = calc(can_211)
     eff_can_300  = calc(can_300)
     eff_can_303  = calc(can_303)

     print(f'\
          #1 Picnic: {eff_can_1_p:.2f}\n\
          #1 Tall: {eff_can_1_t:.2f}\n\
          #2: {eff_can_2:.2f}\n\
          #2.5: {eff_can_2_5:.2f}\n\
          #3 Cylinder: {eff_can_3_c:.2f}\n\
          #5: {eff_can_5:.2f}\n\
          #6Z: {eff_can_6z:.2f}\n\
          #8Z Short: {eff_can_8z_s:.2f}\n\
          #10: {eff_can_10:.2f}\n\
          #211: {eff_can_211:.2f}\n\
          #300: {eff_can_300:.2f}\n\
          #303: {eff_can_303:.2f}')
def calc(can):
     import math
     v = math.pi * (can[0] ** 2) * can[1]
     sa = 2 * math.pi * can[0] * (can[0] + can[1])
     eff = v / sa
     return eff
main()