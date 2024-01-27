from PIL import Image
img_path = "C:/Users/tman/Downloads/School/Programming with Functions/Minecraft Textures (for Draw2D)/sun.png"
image = Image.open(img_path)
y, x = image.size
image_rgb = image.convert("RGB")
img_name = img_path.replace("C:/Users/tman/Downloads/School/Programming with Functions/Minecraft Textures (for Draw2D)/", "")
img_name = img_name.replace(".png", "")
print(img_name)
sun_r0  = []
sun_r1  = []
sun_r2  = []
sun_r3  = []
sun_r4  = []
sun_r5  = []
sun_r6  = []
sun_r7  = []
sun_r8  = []
sun_r9  = []
sun_r10 = []
sun_r11 = []
sun_r12 = []
sun_r13 = []
sun_r14 = []
sun_r15 = []
sun_r16 = []
sun_r17 = []
sun_r18 = []
sun_r19 = []
sun_r20 = []
sun_r21 = []
sun_r22 = []
sun_r23 = []
sun_r24 = []
sun_r25 = []
sun_r26 = []
sun_r27 = []
sun_r28 = []
sun_r29 = []
sun_r30 = []
sun_r31 = []
sun_r32 = []
def rgb_to_hex(rgb):
     return '%02x%02x%02x%02x' % rgb
for row_i in range(x):
     for col_i in range(y):
          coord = (col_i, row_i)
          pixel_rgb = image.getpixel(coord)
          pixel_hex = rgb_to_hex(pixel_rgb)[:6]
          if pixel_hex == '000000':
               pixel_hex = ''
          eval(img_name + '_r' + str(x - row_i)).append(pixel_hex)
     print(f'     {img_name}_r{str(x - row_i - 1)} = ', eval(img_name + '_r' + str(x - row_i)))