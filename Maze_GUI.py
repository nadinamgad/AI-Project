import pygame
import sys
import math
import initialize_array as m
#from Cbutton import button
pygame.init()

class button():
    def __init__(self, x, y, img, text, onclickfunction = None, click = False):
        self.x = x
        self.y = y
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.text = text
        self.onclickfunction = onclickfunction
        self.click = click
        self.button_colors = {
            'default' : '#ffffff',
            'hover' : '#666666',
            'clicked' : '#333333',
        }

    def draw(self):
        canvas.blit(self.img, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                print('clicked !')

            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False


# start_btn = button(114, 48, start_btn, 'start', )
screen_w = 755
screen_h = 900
rows = 9
columns = 9
available_grid_area = 900 - 300
cell_size = 70
black = (0, 0, 0)
white = (255, 255, 255)

fps = 60
fpsClock = pygame.time.Clock()
canvas = pygame.display.set_mode((screen_w, screen_h))
canvas.fill(black)
pygame.display.set_caption("maze problem")
font = pygame.font.SysFont('Arial', 40)
start_btn = pygame.image.load('start_button.png').convert_alpha()
clear_btn = pygame.image.load('clear button.png').convert_alpha()
buttons = []
BLUE=(0,0,255)
RED= (255,0,0)
black= (0,0,0)
click =0;
flag_event=1;
drawing_line = False
margin = 5
row = 0
column = 0
lrectangle = []
lrectangle_row = []
def drawgrid():
    for x in range(10):
         for y in range(10):
            # rect = pygame.Rect((x + 1.5) * cell_size, (y + 2) * cell_size,
            #                    cell_size, cell_size)
            # rect = pygame.rect(((margin + cell_size) * y + margin), ((margin + cell_size) * x + margin)
            #                    , cell_size, cell_size)
            # pygame.draw.rect(canvas, black, rect, 1)
            color = white
            # if m.maze[row][column] == 1:
            #     color = black
            pygame.draw.rect(canvas,
                             color,
                             [(margin + cell_size) * y + margin,
                              (margin + cell_size) * x + margin,
                              cell_size,
                              cell_size])

# def create_grid():
#     for grid_row in range(10):
#         lrectangle_row = []
#         for grid_column in range(10):
#             rect = pygame.Rect((margin + cell_size) * grid_column + margin,
#                                (margin + cell_size) * grid_row + margin,
#                                cell_size,
#                                cell_size)
#             lrectangle_row.append([rect, white])
#         lrectangle.append(lrectangle_row)
#
# def draw_grid():
#     for x in lrectangle:
#         for y in lrectangle_row:
#             rect, color = y
#             pygame.draw.rect(canvas, color, rect)





start = button(51, 792, start_btn, None, None, False)
buttons.append(start)
clear = button(599, 792, clear_btn, None, None, False)
buttons.append(clear)

while True:
    # x, y = pygame.mouse.get_pos()
    # print(x, y)
    # create_grid()
    # print(lrectangle[0][0])
    drawgrid()
    start.draw()
    clear.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            column = mouse_position[0] // (cell_size + margin)
            row = mouse_position[1] // (cell_size + margin)
            print(row, ',', column)
            if event.button==1 :
                X_circle=mouse_position[0]
                Y_circle=mouse_position[1]
            radius = 15
            click+=1
            if click==1:
                #print('hi')
                m.maze[row][column] = 2     #start point
                pygame.draw.circle(canvas, RED, (X_circle, Y_circle), radius) #this is start state
            if click==2:
                m.maze[row][column] = 3   #end point
                pygame.draw.circle(canvas,BLUE,(X_circle,Y_circle),radius) #this is goal state
            if click > 2:
                drawing_line = True
                m.maze[row][column] = 1
            if  event.type == pygame.MOUSEMOTION and drawing_line:
                Xpos_line, Ypos_line = pygame.mouse.get_pos()
                endX, endY = pygame.mouse.get_pos()
                column = Xpos_line // (cell_size + margin)
                row = Ypos_line // (cell_size + margin)
                m.maze[row][column] = 1
                width =50
                pygame.draw.line(canvas, black, (Xpos_line, Ypos_line), (endX, endY), width)
            print(m.maze)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing_line = False
    pygame.display.update()



