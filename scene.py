# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
     start_drawing, draw_line, draw_oval, draw_arc, \
     draw_rectangle, draw_polygon, draw_text, finish_drawing

global pixel_size
global blocks_wide
global blocks_tall
global block_width
global block_height
##################################################
# pixel_size * blocks_wide and pixel_size * blocks_tall must both be >= 6.25.
pixel_size = 6
blocks_wide = 11
blocks_tall = 7
##################################################
block_width = block_height = 16 * pixel_size
def main():
     scene_width = block_width * blocks_wide
     scene_height = block_height * blocks_tall
     canvas = start_drawing("MiNeCrAfT?", scene_width, scene_height)
     # Call your drawing functions such
     # as draw_sky and draw_ground here.
     draw_sky(canvas, scene_width, scene_height)
     draw_ground(canvas, scene_width)
     draw_steve(canvas, 9*block_width, block_height)
     draw_house(canvas, block_width, block_height)
     # Call the finish_drawing function
     # in the draw2d.py library.
     finish_drawing(canvas)
def draw_sky(canvas, scene_x, scene_y):
     draw_rectangle(canvas, 0, 0, scene_x, scene_y, width=0, fill="lightSkyBlue")
     draw_sun(canvas, 0*block_width, 6*block_height)
     draw_cloud(canvas, 1.5*block_width, 6*block_height)
def draw_ground(canvas, scene_x):
     i = 0
     while i < scene_x:
          draw_grass(canvas, i, 0)
          i += block_width
def draw_house(canvas, x0, y0):
     draw_oak_log(canvas, x0 + 1*block_width, y0 + 0*block_height)
     draw_oak_log(canvas, x0 + 1*block_width, y0 + 1*block_height)
     draw_oak_log(canvas, x0 + 1*block_width, y0 + 2*block_height)
     draw_oak_log(canvas, x0 + 5*block_width, y0 + 0*block_height)
     draw_oak_log(canvas, x0 + 5*block_width, y0 + 1*block_height)
     draw_oak_log(canvas, x0 + 5*block_width, y0 + 2*block_height)
     draw_oak_planks(canvas, x0 + 2*block_width, y0 + 0*block_height)
     draw_oak_planks(canvas, x0 + 2*block_width, y0 + 1*block_height)
     draw_oak_planks(canvas, x0 + 2*block_width, y0 + 2*block_height)
     draw_oak_planks(canvas, x0 + 3*block_width, y0 + 0*block_height)
     draw_oak_planks(canvas, x0 + 3*block_width, y0 + 2*block_height)
     draw_oak_planks(canvas, x0 + 4*block_width, y0 + 0*block_height)
     draw_oak_planks(canvas, x0 + 4*block_width, y0 + 1*block_height)
     draw_oak_planks(canvas, x0 + 4*block_width, y0 + 2*block_height)
     draw_stone_bricks(canvas, x0 + 2*block_width, y0 + 3*block_height)
     draw_stone_bricks(canvas, x0 + 3*block_width, y0 + 3*block_height)
     draw_stone_bricks(canvas, x0 + 4*block_width, y0 + 3*block_height)
     draw_stone_brick_stairs_left(canvas, x0 + 0*block_width, y0 + 2*block_height)
     draw_stone_brick_stairs_left(canvas, x0 + 1*block_width, y0 + 3*block_height)
     draw_stone_brick_stairs_right(canvas, x0 + 5*block_width, y0 + 3*block_height)
     draw_stone_brick_stairs_right(canvas, x0 + 6*block_width, y0 + 2*block_height)
     draw_glass(canvas, x0+ 3*block_width, y0 + 1*block_height)
def draw_cloud(canvas, x0, y0):
     draw_cloud_piece(canvas, x0 + 0*block_width, y0 + 0*block_height)
     draw_cloud_piece(canvas, x0 + .5*block_width, y0 + 0*block_height)
     draw_cloud_piece(canvas, x0 + .5*block_width, y0 + .5*block_height)
     draw_cloud_piece(canvas, x0 + 1*block_width, y0 + 0*block_height)
     draw_cloud_piece(canvas, x0 + 1*block_width, y0 + .5*block_height)
     draw_cloud_piece(canvas, x0 + 1.5*block_width, y0 + 0*block_height)
     draw_cloud_piece(canvas, x0 + 1.5*block_width, y0 + .5*block_height)
     draw_cloud_piece(canvas, x0 + 2*block_width, y0 + 0*block_height)

     draw_cloud_piece(canvas, x0 + 4.5*block_width, y0 - 0.5*block_height)
     draw_cloud_piece(canvas, x0 + 5*block_width, y0 - 0.5*block_height)
     draw_cloud_piece(canvas, x0 + 5.5*block_width, y0 - 0.5*block_height)
     draw_cloud_piece(canvas, x0 + 6*block_width, y0 - 0.5*block_height)
def draw_grass(canvas, x0, y0):
     grass_r15 =  ['74b44a', '76b64c', '73b349', '66a63c', '66a63c', '6faf45', '5f9f35', '6cac42',\
           '7ebe54', '76b64c', '6aaa40', '67a73d', '69a93f', '61a137', '509026', '6dad43']
     grass_r14 =  ['75b54b', '6cac42', '8ab95a', '81b051', '83b253', '593d29', '68a83e', '62a238',\
           '5f9f35', '93c263', '90bf60', '73b349', '61a137', '6cac42', '67a73d', '6bab41']
     grass_r13 =  ['8dbc5d', '593d29', '9ccb6c', '64a43a', '69a93f', '593d29', '70b046', '593d29',\
           '74b44a', '7fbf55', '92c162', '97c667', '593d29', '57972d', '60a036', '593d29']
     grass_r12 =  ['593d29', '6c6c6c', '593d29', '593d29', '71b147', '593d29', '593d29', '593d29',\
           '5f9f35', '593d29', '6dad43', '593d29', '79553a', '593d29', '593d29', '79553a']
     grass_r11 =  ['966c4a', '79553a', '966c4a', 'b9855c', '593d29', '966c4a', '79553a', '79553a',\
           '593d29', '593d29', '593d29', '6c6c6c', '79553a', '966c4a', '593d29', '79553a']
     grass_r10 =  ['79553a', '593d29', '966c4a', '966c4a', '79553a', '966c4a', '593d29', '593d29',\
           '593d29', '79553a', '79553a', '593d29', '79553a', '79553a', '79553a', 'b9855c']
     grass_r9  =  ['b9855c', '79553a', '79553a', '79553a', '878787', '79553a', '79553a', 'b9855c',\
           'b9855c', '79553a', 'b9855c', 'b9855c', '79553a', '966c4a', '79553a', '966c4a']
     grass_r8  =  ['79553a', '79553a', 'b9855c', 'b9855c', '966c4a', '966c4a', '79553a', '79553a',\
           '966c4a', '593d29', '966c4a', '966c4a', '79553a', '79553a', '966c4a', '966c4a']
     grass_r7  =  ['966c4a', '79553a', '79553a', '966c4a', '79553a', '966c4a', '79553a', '593d29',\
           '79553a', '966c4a', '966c4a', '79553a', '79553a', '79553a', '593d29', '79553a']
     grass_r6  =  ['79553a', '966c4a', '593d29', '79553a', '79553a', '593d29', '593d29', '79553a',\
           '79553a', '79553a', '79553a', '79553a', 'b9855c', 'b9855c', '79553a', '966c4a']
     grass_r5  =  ['79553a', '966c4a', '79553a', 'b9855c', 'b9855c', '79553a', 'b9855c', '966c4a',\
           '593d29', 'b9855c', 'b9855c', '593d29', '966c4a', '966c4a', '878787', '79553a']
     grass_r4  =  ['966c4a', '79553a', '79553a', '966c4a', '966c4a', 'b9855c', '79553a', '966c4a',\
           '6c6c6c', '966c4a', '966c4a', '79553a', '593d29', '966c4a', '79553a', '593d29']
     grass_r3  =  ['79553a', '593d29', '966c4a', '79553a', '966c4a', '966c4a', 'b9855c', '79553a',\
           '79553a', '79553a', '79553a', '79553a', '79553a', '79553a', 'b9855c', 'b9855c']
     grass_r2  =  ['79553a', '966c4a', '79553a', '79553a', '745844', '79553a', '966c4a', '966c4a',\
           '79553a', '593d29', 'b9855c', '593d29', '79553a', 'b9855c', '966c4a', '966c4a']
     grass_r1  =  ['966c4a', '79553a', '593d29', 'b9855c', '79553a', '593d29', '79553a', '593d29',\
           'b9855c', 'b9855c', '79553a', '966c4a', '79553a', '79553a', '966c4a', '966c4a']
     grass_r0  =  ['966c4a', '79553a', 'b9855c', '966c4a', '966c4a', '79553a', '878787', '79553a',\
           '966c4a', '966c4a', '79553a', '79553a', '966c4a', '966c4a', '79553a', '593d29']
     for row_i in range(16):
          for col_i in range(16):
               row = "grass_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_steve(canvas, x0, y0):
     steve_r31 =  ['', '', '', '', '2f200d', '2b1e0d', '2f1f0f', '281c0b',\
           '241808', '261a0a', '2b1e0d', '2a1d0d', '', '', '', '']
     steve_r30 =  ['', '', '', '', '2b1e0d', '2b1e0d', '2b1e0d', '332411',\
           '422a12', '3f2a15', '2c1e0e', '281c0b', '', '', '', '']
     steve_r29 =  ['', '', '', '', '2b1e0d', 'b6896c', 'bd8e72', 'c69680',\
           'bd8b72', 'bd8e74', 'ac765a', '342512', '', '', '', '']
     steve_r28 =  ['', '', '', '', 'aa7d66', 'b4846d', 'aa7d66', 'ad806d',\
           '9c725c', 'bb8972', '9c694c', '9c694c', '', '', '', '']
     steve_r27 =  ['', '', '', '', 'b4846d', 'ffffff', '523d89', 'b57b67',\
           'bb8972', '523d89', 'ffffff', 'aa7d66', '', '', '', '']
     steve_r26 =  ['', '', '', '', '9c6346', 'b37b62', 'b78272', '6a4030',\
           '6a4030', 'be886c', 'a26a47', '805334', '', '', '', '']
     steve_r25 =  ['', '', '', '', '905e43', '965f40', '774235', '774235',\
           '774235', '774235', '8f5e3e', '815339', '', '', '', '']
     steve_r24 =  ['', '', '', '', '6f452c', '6d432a', '815339', '815339',\
           '7a4e33', '83553b', '83553b', '7a4e33', '', '', '', '']
     steve_r23 =  ['009e9e', '00a8a8', '00afaf', '00a8a8', '009999', '009e9e', '815339', 'a26a47',\
           '815339', '815339', '009e9e', '009e9e', '00a8a8', '00afaf', '00a8a8', '009e9e']
     steve_r22 =  ['00afaf', '00a8a8', '00afaf', '009e9e', '00a8a8', '00a8a8', '009e9e', '815339',\
           '815339', '009e9e', '00afaf', '00afaf', '009e9e', '00afaf', '00a8a8', '00afaf']
     steve_r21 =  ['00a8a8', '00afaf', '00afaf', '00afaf', '00afaf', '00afaf', '00a8a8', '009e9e',\
           '009999', '00a8a8', '00afaf', '00afaf', '00afaf', '00afaf', '00afaf', '00a8a8']
     steve_r20 =  ['009e9e', '00afaf', '00afaf', '009e9e', '00afaf', '00afaf', '00afaf', '009e9e',\
           '009999', '00afaf', '00afaf', '00afaf', '009e9e', '00afaf', '00afaf', '009e9e']
     steve_r19 =  ['aa7d66', 'aa7d66', 'aa7d66', 'aa7d66', '009999', '009999', '00afaf', '00afaf',\
           '009999', '00afaf', '009999', '009999', 'aa7d66', 'aa7d66', 'aa7d66', 'aa7d66']
     steve_r18 =  ['aa7d66', '966f5b', 'aa7d66', 'aa7d66', '009999', '009999', '00afaf', '00a8a8',\
           '009999', '00afaf', '00a8a8', '009999', 'aa7d66', 'aa7d66', '966f5b', 'aa7d66']
     steve_r17 =  ['aa7d66', '966f5b', 'aa7d66', '966f5b', '009999', '00afaf', '00afaf', '009999',\
           '00a8a8', '00afaf', '00a8a8', '009999', '966f5b', 'aa7d66', '966f5b', 'aa7d66']
     steve_r16 =  ['aa7d66', 'aa7d66', 'aa7d66', '966f5b', '009999', '00afaf', '00afaf', '009999',\
           '00a8a8', '00afaf', '00a8a8', '009999', '966f5b', 'aa7d66', 'aa7d66', 'aa7d66']
     steve_r15 =  ['aa7d66', 'aa7d66', 'aa7d66', '966f5b', '00afaf', '00afaf', '00afaf', '009999',\
           '00a8a8', '00afaf', '00afaf', '009999', '966f5b', 'aa7d66', 'aa7d66', 'aa7d66']
     steve_r14 =  ['aa7d66', 'aa7d66', 'aa7d66', 'aa7d66', '009999', '009999', '009999', '00a8a8',\
           '00afaf', '00a8a8', '00afaf', '009999', 'aa7d66', 'aa7d66', 'aa7d66', 'aa7d66']
     steve_r13 =  ['aa7d66', 'aa7d66', '966f5b', 'aa7d66', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '3a3189', '00afaf', '009999', 'aa7d66', '966f5b', 'aa7d66', 'aa7d66']
     steve_r12 =  ['966f5b', 'aa7d66', '966f5b', '966f5b', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '3a3189', '009999', '966f5b', '966f5b', 'aa7d66', '966f5b']
     steve_r11 =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r10 =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r9  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r8  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r7  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r6  =  ['', '', '', '', '463aa5', '3a3189', '3a3189', '463aa5',\
           '463aa5', '3a3189', '3a3189', '463aa5', '', '', '', '']
     steve_r5  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r4  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r3  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r2  =  ['', '', '', '', '463aa5', '463aa5', '463aa5', '463aa5',\
           '463aa5', '463aa5', '463aa5', '463aa5', '', '', '', '']
     steve_r1  =  ['', '', '', '', '6b6b6b', '6b6b6b', '6b6b6b', '6b6b6b',\
           '6b6b6b', '6b6b6b', '6b6b6b', '6b6b6b', '', '', '', '']
     steve_r0  =  ['', '', '', '', '6b6b6b', '6b6b6b', '6b6b6b', '6b6b6b',\
           '6b6b6b', '6b6b6b', '6b6b6b', '6b6b6b', '', '', '', '']
     for row_i in range(32):
          for col_i in range(16):
               row = "steve_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_oak_log(canvas, x0, y0):
     oak_log_r15 =  ['745a36', '4c3d26', '917142', '745a36', '745a36', '382b18', '917142', '745a36',\
           '745a36', '382b18', '745a36', '917142', '4c3d26', '917142', '745a36', '5f4a2b']
     oak_log_r14 =  ['745a36', '4c3d26', '987849', '5f4a2b', '745a36', '382b18', '987849', '5f4a2b',\
           '745a36', '382b18', '745a36', '917142', '4c3d26', '745a36', '745a36', '5f4a2b']
     oak_log_r13 =  ['745a36', '382b18', '5f4a2b', '5f4a2b', '745a36', '382b18', '987849', '5f4a2b',\
           '745a36', '4c3d26', '745a36', '4c3d26', '4c3d26', '745a36', '745a36', '5f4a2b']
     oak_log_r12 =  ['917142', '382b18', '745a36', '5f4a2b', '745a36', '4c3d26', '745a36', '5f4a2b',\
           '745a36', '5f4a2b', '745a36', '382b18', '4c3d26', '745a36', '917142', '5f4a2b']
     oak_log_r11 =  ['917142', '4c3d26', '745a36', '5f4a2b', '745a36', '382b18', '745a36', '5f4a2b',\
           '987849', '5f4a2b', '745a36', '5f4a2b', '745a36', '4c3d26', '917142', '745a36']
     oak_log_r10 =  ['917142', '745a36', '4c3d26', '745a36', '917142', '4c3d26', '745a36', '4c3d26',\
           '987849', '5f4a2b', '917142', '4c3d26', '745a36', '4c3d26', '917142', '745a36']
     oak_log_r9  =  ['5f4a2b', '745a36', '4c3d26', '745a36', '917142', '5f4a2b', '5f4a2b', '745a36',\
           '917142', '745a36', '917142', '745a36', '745a36', '4c3d26', '917142', '745a36']
     oak_log_r8  =  ['5f4a2b', '745a36', '382b18', '745a36', '917142', '745a36', '5f4a2b', '917142',\
           '745a36', '745a36', '917142', '5f4a2b', '745a36', '5f4a2b', '917142', '745a36']
     oak_log_r7  =  ['745a36', '4c3d26', '382b18', '987849', '745a36', '745a36', '5f4a2b', '917142',\
           '745a36', '5f4a2b', '917142', '5f4a2b', '917142', '5f4a2b', '917142', '745a36']
     oak_log_r6  =  ['745a36', '745a36', '4c3d26', '987849', '745a36', '745a36', '5f4a2b', '745a36',\
           '745a36', '5f4a2b', '917142', '4c3d26', '917142', '745a36', '382b18', '745a36']
     oak_log_r5  =  ['745a36', '745a36', '745a36', '917142', '745a36', '5f4a2b', '745a36', '382b18',\
           '745a36', '5f4a2b', '745a36', '4c3d26', '917142', '745a36', '382b18', '745a36']
     oak_log_r4  =  ['745a36', '4c3d26', '745a36', '917142', '745a36', '5f4a2b', '745a36', '382b18',\
           '987849', '745a36', '745a36', '382b18', '987849', '745a36', '4c3d26', '745a36']
     oak_log_r3  =  ['987849', '4c3d26', '745a36', '745a36', '917142', '5f4a2b', '917142', '382b18',\
           '987849', '5f4a2b', '745a36', '382b18', '745a36', '745a36', '5f4a2b', '745a36']
     oak_log_r2  =  ['987849', '745a36', '4c3d26', '745a36', '917142', '745a36', '745a36', '4c3d26',\
           '917142', '5f4a2b', '745a36', '4c3d26', '745a36', '745a36', '745a36', '745a36']
     oak_log_r1  =  ['917142', '745a36', '4c3d26', '917142', '745a36', '745a36', '917142', '382b18',\
           '745a36', '4c3d26', '745a36', '4c3d26', '4c3d26', '917142', '745a36', '745a36']
     oak_log_r0  =  ['917142', '745a36', '4c3d26', '917142', '4c3d26', '745a36', '917142', '4c3d26',\
           '745a36', '4c3d26', '745a36', '745a36', '4c3d26', '917142', '745a36', '5f4a2b']
     for row_i in range(16):
          for col_i in range(16):
               row = "oak_log_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_oak_planks(canvas, x0, y0):
     oak_planks_r15 =  ['b8945f', 'af8f55', 'b8945f', 'c29d62', 'c29d62', 'c29d62', 'c29d62', 'c29d62',\
           'b8945f', 'c29d62', 'c29d62', 'c29d62', 'c29d62', 'c29d62', 'b8945f', '967441']
     oak_planks_r14 =  ['b8945f', 'b8945f', 'af8f55', 'af8f55', '967441', '9f844d', 'af8f55', 'b8945f',\
           'b8945f', 'b8945f', 'af8f55', 'af8f55', 'b8945f', 'b8945f', '9f844d', '9f844d']
     oak_planks_r13 =  ['af8f55', 'b8945f', 'b8945f', 'b8945f', 'af8f55', 'b8945f', 'af8f55', '9f844d',\
           '9f844d', '9f844d', '9f844d', 'af8f55', 'af8f55', 'b8945f', 'b8945f', '967441']
     oak_planks_r12 =  ['967441', '7e6237', '7e6237', '967441', '967441', '7e6237', '67502c', '67502c',\
           '7e6237', '7e6237', '67502c', '7e6237', '67502c', '67502c', '7e6237', '67502c']
     oak_planks_r11 =  ['b8945f', 'c29d62', '9f844d', 'c29d62', 'c29d62', 'c29d62', 'c29d62', '9f844d',\
           'c29d62', 'c29d62', 'c29d62', 'b8945f', 'af8f55', 'af8f55', '9f844d', 'b8945f']
     oak_planks_r10 =  ['af8f55', 'b8945f', 'b8945f', 'af8f55', '9f844d', 'af8f55', '9f844d', '967441',\
           '9f844d', 'af8f55', 'af8f55', 'b8945f', 'b8945f', 'b8945f', 'b8945f', 'af8f55']
     oak_planks_r9  =  ['9f844d', '9f844d', 'af8f55', 'b8945f', 'af8f55', 'af8f55', 'af8f55', '967441',\
           'b8945f', 'b8945f', 'b8945f', 'af8f55', 'af8f55', '9f844d', '9f844d', '9f844d']
     oak_planks_r8  =  ['67502c', '67502c', '7e6237', '7e6237', '967441', '7e6237', '67502c', '67502c',\
           '67502c', '67502c', '7e6237', '7e6237', '7e6237', '967441', '7e6237', '67502c']
     oak_planks_r7  =  ['b8945f', 'c29d62', 'c29d62', 'b8945f', 'af8f55', 'af8f55', 'c29d62', 'c29d62',\
           'c29d62', 'c29d62', 'c29d62', 'c29d62', 'c29d62', 'c29d62', 'b8945f', '9f844d']
     oak_planks_r6  =  ['b8945f', 'af8f55', 'b8945f', 'b8945f', 'b8945f', 'b8945f', 'af8f55', '9f844d',\
           '9f844d', '9f844d', 'af8f55', '9f844d', 'af8f55', '9f844d', '9f844d', '967441']
     oak_planks_r5  =  ['c29d62', 'b8945f', 'af8f55', 'af8f55', '9f844d', '9f844d', '9f844d', '9f844d',\
           'af8f55', 'af8f55', 'af8f55', 'af8f55', '9f844d', '9f844d', 'b8945f', '9f844d']
     oak_planks_r4  =  ['67502c', '67502c', '7e6237', '967441', '967441', '7e6237', '67502c', '67502c',\
           '67502c', '7e6237', '967441', '7e6237', '7e6237', '67502c', '67502c', '67502c']
     oak_planks_r3  =  ['c29d62', '9f844d', 'b8945f', 'c29d62', 'c29d62', 'b8945f', 'b8945f', '9f844d',\
           'c29d62', 'c29d62', 'c29d62', '9f844d', 'c29d62', 'b8945f', 'c29d62', 'c29d62']
     oak_planks_r2  =  ['af8f55', 'af8f55', 'b8945f', 'b8945f', '9f844d', '9f844d', 'af8f55', '9f844d',\
           '9f844d', 'b8945f', 'b8945f', 'af8f55', 'b8945f', 'af8f55', 'af8f55', 'af8f55']
     oak_planks_r1  =  ['af8f55', '9f844d', '9f844d', 'af8f55', 'b8945f', 'af8f55', '9f844d', '967441',\
           'b8945f', 'b8945f', 'af8f55', '9f844d', '9f844d', '9f844d', '9f844d', '9f844d']
     oak_planks_r0  =  ['67502c', '7e6237', '7e6237', '67502c', '67502c', '7e6237', '967441', '967441',\
           '967441', '7e6237', '67502c', '7e6237', '67502c', '67502c', '67502c', '67502c']
     for row_i in range(16):
          for col_i in range(16):
               row = "oak_planks_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_stone_bricks(canvas, x0, y0):
     stone_bricks_r15 =  ['8b898b', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c',\
           '9c999c', '9c999c', '9c999c', '9c999c', '8b898b', '8b898b', '8b898b', '5a595a']
     stone_bricks_r14 =  ['9c999c', '7f7f7f', '8b898b', '7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b',\
           '8b898b', '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f', '8b898b', '5a595a']
     stone_bricks_r13 =  ['9c999c', '8b898b', '7f7f7f', '8b898b', '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f',\
           '7f7f7f', '7f7f7f', '8b898b', '8b898b', '787678', '7f7f7f', '7f7f7f', '5a595a']
     stone_bricks_r12 =  ['9c999c', '7f7f7f', '787678', '7f7f7f', '8b898b', '8b898b', '7f7f7f', '787678',\
           '7f7f7f', '8b898b', '7f7f7f', '787678', '7f7f7f', '787678', '787678', '5a595a']
     stone_bricks_r11 =  ['9c999c', '787678', '6a6d6a', '787678', '787678', '7f7f7f', '8b898b', '7f7f7f',\
           '7f7f7f', '787678', '787678', '7f7f7f', '787678', '6a6d6a', '7f7f7f', '5a595a']
     stone_bricks_r10 =  ['8b898b', '787678', '6a6d6a', '7f7f7f', '7f7f7f', '787678', '787678', '787678',\
           '787678', '7f7f7f', '8b898b', '787678', '6a6d6a', '7f7f7f', '787678', '5a595a']
     stone_bricks_r9  =  ['6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a',\
           '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '5a595a']
     stone_bricks_r8  =  ['636363', '636363', '5a595a', '5a595a', '636363', '636363', '5a595a', '5a595a',\
           '5a595a', '636363', '636363', '636363', '636363', '636363', '636363', '636363']
     stone_bricks_r7  =  ['9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '8b898b', '5a595a',\
           '8b898b', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c']
     stone_bricks_r6  =  ['787678', '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f', '7f7f7f', '5a595a',\
           '9c999c', '8b898b', '7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f']
     stone_bricks_r5  =  ['8b898b', '7f7f7f', '7f7f7f', '8b898b', '7f7f7f', '7f7f7f', '787678', '5a595a',\
           '9c999c', '7f7f7f', '787678', '8b898b', '787678', '8b898b', '7f7f7f', '7f7f7f']
     stone_bricks_r4  =  ['7f7f7f', '8b898b', '8b898b', '7f7f7f', '7f7f7f', '787678', '6a6d6a', '5a595a',\
           '9c999c', '787678', '7f7f7f', '787678', '7f7f7f', '7f7f7f', '7f7f7f', '8b898b']
     stone_bricks_r3  =  ['7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f', '787678', '7f7f7f', '787678', '5a595a',\
           '8b898b', '787678', '787678', '7f7f7f', '8b898b', '7f7f7f', '787678', '787678']
     stone_bricks_r2  =  ['787678', '787678', '6a6d6a', '787678', '6a6d6a', '6a6d6a', '787678', '5a595a',\
           '8b898b', '7f7f7f', '7f7f7f', '787678', '787678', '7f7f7f', '7f7f7f', '787678']
     stone_bricks_r1  =  ['6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '5a595a',\
           '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a']
     stone_bricks_r0  =  ['636363', '636363', '636363', '636363', '636363', '636363', '5a595a', '5a595a',\
           '5a595a', '5a595a', '636363', '636363', '636363', '636363', '636363', '636363']
     for row_i in range(16):
          for col_i in range(16):
               row = "stone_bricks_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_stone_brick_stairs_left(canvas, x0, y0):
     stone_brick_stairs_left_r15 =  ['', '', '', '', '', '', '', '',\
           '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '8b898b']
     stone_brick_stairs_left_r14 =  ['', '', '', '', '', '', '', '',\
           '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f', '8b898b', '7f7f7f', '9c999c']
     stone_brick_stairs_left_r13 =  ['', '', '', '', '', '', '', '',\
           '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f', '8b898b', '7f7f7f', '8b898b', '9c999c']
     stone_brick_stairs_left_r12 =  ['', '', '', '', '', '', '', '',\
           '787678', '7f7f7f', '8b898b', '8b898b', '7f7f7f', '787678', '7f7f7f', '9c999c']
     stone_brick_stairs_left_r11 =  ['', '', '', '', '', '', '', '',\
           '7f7f7f', '8b898b', '7f7f7f', '787678', '787678', '6a6d6a', '787678', '9c999c']
     stone_brick_stairs_left_r10 =  ['', '', '', '', '', '', '', '',\
           '787678', '787678', '787678', '7f7f7f', '7f7f7f', '6a6d6a', '787678', '8b898b']
     stone_brick_stairs_left_r9  =  ['', '', '', '', '', '', '', '',\
           '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a']
     stone_brick_stairs_left_r8  =  ['', '', '', '', '', '', '', '',\
           '5a595a', '5a595a', '636363', '636363', '5a595a', '5a595a', '636363', '636363']
     stone_brick_stairs_left_r7  =  ['9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '8b898b',\
           '5a595a', '8b898b', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c']
     stone_brick_stairs_left_r6  =  ['7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f', '8b898b', '9c999c',\
           '5a595a', '7f7f7f', '7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b', '787678']
     stone_brick_stairs_left_r5  =  ['7f7f7f', '7f7f7f', '8b898b', '787678', '8b898b', '787678', '7f7f7f', '9c999c',\
           '5a595a', '787678', '7f7f7f', '7f7f7f', '8b898b', '7f7f7f', '7f7f7f', '8b898b']
     stone_brick_stairs_left_r4  =  ['8b898b', '7f7f7f', '7f7f7f', '7f7f7f', '787678', '7f7f7f', '787678', '9c999c',\
           '5a595a', '6a6d6a', '787678', '7f7f7f', '7f7f7f', '8b898b', '8b898b', '7f7f7f']
     stone_brick_stairs_left_r3  =  ['787678', '787678', '7f7f7f', '8b898b', '7f7f7f', '787678', '787678', '8b898b',\
           '5a595a', '787678', '7f7f7f', '787678', '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f']
     stone_brick_stairs_left_r2  =  ['787678', '7f7f7f', '7f7f7f', '787678', '787678', '7f7f7f', '7f7f7f', '8b898b',\
           '5a595a', '787678', '6a6d6a', '6a6d6a', '787678', '6a6d6a', '787678', '787678']
     stone_brick_stairs_left_r1  =  ['6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a',\
           '5a595a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a']
     stone_brick_stairs_left_r0  =  ['636363', '636363', '636363', '636363', '636363', '636363', '5a595a', '5a595a',\
           '5a595a', '5a595a', '636363', '636363', '636363', '636363', '636363', '636363']
     for row_i in range(16):
          for col_i in range(16):
               row = "stone_brick_stairs_left_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_stone_brick_stairs_right(canvas, x0, y0):
     stone_brick_stairs_right_r15 =  ['8b898b', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r14 =  ['9c999c', '7f7f7f', '8b898b', '7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r13 =  ['9c999c', '8b898b', '7f7f7f', '8b898b', '7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r12 =  ['9c999c', '7f7f7f', '787678', '7f7f7f', '8b898b', '8b898b', '7f7f7f', '787678',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r11 =  ['9c999c', '787678', '6a6d6a', '787678', '787678', '7f7f7f', '8b898b', '7f7f7f',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r10 =  ['8b898b', '787678', '6a6d6a', '7f7f7f', '7f7f7f', '787678', '787678', '787678',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r9  =  ['6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r8  =  ['636363', '636363', '5a595a', '5a595a', '636363', '636363', '5a595a', '5a595a',\
           '', '', '', '', '', '', '', '']
     stone_brick_stairs_right_r7  =  ['9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '8b898b', '5a595a',\
           '8b898b', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c', '9c999c']
     stone_brick_stairs_right_r6  =  ['787678', '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f', '7f7f7f', '5a595a',\
           '9c999c', '8b898b', '7f7f7f', '8b898b', '8b898b', '8b898b', '8b898b', '7f7f7f']
     stone_brick_stairs_right_r5  =  ['8b898b', '7f7f7f', '7f7f7f', '8b898b', '7f7f7f', '7f7f7f', '787678', '5a595a',\
           '9c999c', '7f7f7f', '787678', '8b898b', '787678', '8b898b', '7f7f7f', '7f7f7f']
     stone_brick_stairs_right_r4  =  ['7f7f7f', '8b898b', '8b898b', '7f7f7f', '7f7f7f', '787678', '6a6d6a', '5a595a',\
           '9c999c', '787678', '7f7f7f', '787678', '7f7f7f', '7f7f7f', '7f7f7f', '8b898b']
     stone_brick_stairs_right_r3  =  ['7f7f7f', '7f7f7f', '7f7f7f', '7f7f7f', '787678', '7f7f7f', '787678', '5a595a',\
           '8b898b', '787678', '787678', '7f7f7f', '8b898b', '7f7f7f', '787678', '787678']
     stone_brick_stairs_right_r2  =  ['787678', '787678', '6a6d6a', '787678', '6a6d6a', '6a6d6a', '787678', '5a595a',\
           '8b898b', '7f7f7f', '7f7f7f', '787678', '787678', '7f7f7f', '7f7f7f', '787678']
     stone_brick_stairs_right_r1  =  ['6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '5a595a',\
           '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a', '6a6d6a']
     stone_brick_stairs_right_r0  =  ['636363', '636363', '636363', '636363', '636363', '636363', '5a595a', '5a595a',\
           '5a595a', '5a595a', '636363', '636363', '636363', '636363', '636363', '636363']
     for row_i in range(16):
          for col_i in range(16):
               row = "stone_brick_stairs_right_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_glass(canvas, x0, y0):
     glass_r15 =  ['d0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9',\
           'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'd0eae9', 'a8d0d9']
     glass_r14 =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', 'a8d0d9']
     glass_r13 =  ['d0eae9', '', '', '', 'd0eae9', '', '', '',\
           '', '', '', '', '', '', '', '7baeb7']
     glass_r12 =  ['d0eae9', '', '', 'd0eae9', '', '', '', '',\
           '', '', '', '', '', '', '', '7baeb7']
     glass_r11 =  ['d0eae9', '', 'a8d0d9', '', '', '', '', '',\
           '', '', '', '', '', '', '', '7baeb7']
     glass_r10 =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r9  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '7baeb7']
     glass_r8  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r7  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r6  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r5  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r4  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', '8bc1cd']
     glass_r3  =  ['a8d0d9', '', '', '', '', '', '', '',\
           '', '', '', '', '', 'd0eae9', '', '8bc1cd']
     glass_r2  =  ['d0eae9', '', '', '', '', '', '', '',\
           '', '', '', '', 'd0eae9', '', '', '8bc1cd']
     glass_r1  =  ['a8d0d9', '', '', '', '', '', '', '',\
           '', '', '', '', '', '', '', 'a8d0d9']
     glass_r0  =  ['a8d0d9', 'a8d0d9', '8bc1cd', 'a8d0d9', '8bc1cd', '8bc1cd', '8bc1cd', '8bc1cd',\
           '8bc1cd', '8bc1cd', '8bc1cd', '8bc1cd', '8bc1cd', '8bc1cd', 'a8d0d9', 'a8d0d9']
     for row_i in range(16):
          for col_i in range(16):
               row = "glass_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_sun(canvas, x0, y0):
     sun_r15 =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r14 =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r13 =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r12 =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r11 =  ['', '', '', '', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', '', '', '', '']
     sun_r10 =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r9  =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r8  =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r7  =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r6  =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffd9', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r5  =  ['', '', '', '', 'ffd54a', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffffaa', 'ffd54a', '', '', '', '']
     sun_r4  =  ['', '', '', '', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', 'ffd54a', '', '', '', '']
     sun_r3  =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r2  =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r1  =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     sun_r0  =  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     for row_i in range(16):
          for col_i in range(16):
               row = "sun_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_cloud_piece(canvas, x0, y0):
     cloud_r7  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r6  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r5  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r4  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r3  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r2  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r1  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     cloud_r0  =  ['ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ffffff']
     for row_i in range(8):
          for col_i in range(8):
               row = "cloud_r" + str(row_i)
               color = "#" + eval(row)[col_i]
               draw_pixel(canvas, x0 + col_i * pixel_size, y0 + row_i * pixel_size, color)
def draw_pixel(canvas, x0, y0, color):
     if color == "#":
          color = ''
     draw_rectangle(canvas, x0, y0, x0 + pixel_size, y0 + pixel_size, width=0, fill=color)
main()