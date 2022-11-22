import pygame
import sys
import math
#import initialize_array as m
#from Cbutton import button
#from iterative import *
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
#--------------------------------------------------------------------------------------------------------------------------------
class Maze:
    def __init__(self):
        #self.maze = maze
        self.start_x = 0
        self.start_y =0
        self.goal_x = 0
        self.goal_y = 0
        self.X=10
        self.Y=10
        self.limit=20
        #print(self.goal_x)
        self.maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def set_start(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

    def set_goal(self, goal_x, goal_y):
        self.goal_x = goal_x
        self.goal_y = goal_y

    def initialize(self):
        self.maze = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]

    def read_maze(self):
        for x in self.maze:
            for y in x:
                return(y)

    def __getitem__(self, items):
       return items

    def can_pass(self, x, y, d):

        if d == "right":
           # print('hi')
            #print(self.maze[x][y])
            if y == (self.Y - 1):#border always equal 1
                return False
            if self.maze[x][y+1] != 1:  # right
               return True
            else:
                 return False

        elif d == "down":
            if x == (self.X - 1):#border
                return False
            elif self.maze[x+1][y] != 1:  # down
                return True
            else:
                return False

        elif d == "left":

            if y == 0:
                return False
            elif self.maze[x][y-1] != 1:  # left
                self.left = True
            else:
                return False

        elif d == "up":
            if x == 0:
                return False

            elif self.maze[x-1][y] != 1:  # up
                self.up = True
            else:
                return False

m=Maze()
pathL=[]
class Node:
    x = 0
    y = 0
    color = (0,0,0)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cost = 0
        self.parent = None
        self.right = None
        self.down = None
        self.left = None
        self.up = None
        self.heuristic = 0
        self.v=0
        self.width = 70
        #-------------------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------------------------

    def check_equality(self, x, y):
        return x == self.x and y == self.y
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return black
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

class Game:
    pnns = []
    maze = None
    def __init__(self):
        self.maze = m
        #print(self.maze.start_x)
        self.root = self.create_node(self.maze.start_x, self.maze.start_y)
        # print("maze start:")
        # print(self.maze.start_x, self.maze.start_y)


    def create_node(self, x, y):
        node = Node()
        node.x = x
        node.y = y
        node.v = self.maze.maze[x][y]
        #print(node.v)

        #print(node.down)

        #print(node.right)

        self.pnns.append(node)
        if self.maze.can_pass(node.x, node.y,"right"):
            node.right = self.create_node(node.x, node.y + 1)
            node.right.parent = node
        elif self.maze.can_pass(node.x, node.y, "down"):
            node.down = self.create_node(node.x + 1, node.y)
            node.down.parent = node
        elif self.maze.can_pass(node.x, node.y,"left"):
            node.left = self.create_node(node.x, node.y - 1)
            node.left.parent = node
        elif self.maze.can_pass(node.x, node.y,"up"):
            node.up = self.create_node(node.x - 1, node.y)
            node.up.parent = node
        #print(node.v)
        return node





    def clear_parents(self):
        for node in self.pnns:
            node.parent = None


#-------------------------------------------------------------------------



#--------------------------------------------------------------------------

class button_2():
    def __init__(self):
        self.button1_surface=pygame.image.load('gui button.png').convert_alpha()
        self.resize1 = pygame.transform.scale(self.button1_surface,(200,80))
        self.button_rect=self.button1_surface.get_rect(topleft= (185,800) )

        self.font = pygame.font.SysFont("Arial black", 40,bold=True)
        self.text1 = self.font.render('BFS', False, (50,50,0))
        self.text_rect=self.text1.get_rect(center=(285,835))

        self.button2_surface=pygame.image.load('gui2.png').convert_alpha()
        self.resize2=pygame.transform.scale(self.button2_surface,(200,80))
        self.button_rect2=self.button2_surface.get_rect(topleft=(450,800))

        self.text2 = self.font.render('ITD',False,(50,50,0))
        self.text2_rect=self.text2.get_rect(center=(552,835))



#checking if clicked
    def check_movement(self, cursor,button_rect,text_rect):
        # print(cursor)
        # check for clicking
        clicked = False
        action = False

        if text_rect.collidepoint(cursor) :
            if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                #print('clicked')
                clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                #print('back')
                clicked = False
                action = False
        return action

    def hover(self, a, b):
        if self.button_rect.x <= a <= self.button_rect.x+200 and self.button_rect.y <= b <= self.button_rect.y + 80:
            #1st button
            bfs = True
            self.text1=self.font.render('BFS',False,(255,255,255))
            self.text_rect=self.text1.get_rect(center=(285,835))


        else:
            self.text1 = self.font.render('BFS', False, (50, 50, 0))
            self.text_rect = self.text1.get_rect(center=(285, 835))

        if self.button_rect2.x <= a <= self.button_rect2.x+200 and self.button_rect2.y <= b <= self.button_rect2.y + 80 :
            itd = True
            self.text2 = self.font.render('ITD', False, (255, 255, 255))
            self.text2_rect = self.text2.get_rect(center=(552, 835))

        else:
            # 2nd button
            self.text2 = self.font.render('ITD', False, (50, 50, 0))
            self.text2_rect = self.text2.get_rect(center=(552, 835))

    def display_buttons(self, screen, cursor, bfs, itd):
        solution = []
        value = self.check_movement(cursor, self.button_rect, self.text_rect)
        if value:
            print('BFS')
            bfs = True
            itd = False
            print(bfs)
            # algorithim
        value2 = self.check_movement(cursor, self.button_rect2, self.text2_rect)
        if value2:
            print('ITD')
            itd = True
            bfs = False
            print(itd)
            solution = iterative_deepening_search()
            # algorithim
            #algo.iterative_deepening_search()

        screen.blit(self.resize1, self.button_rect)
        screen.blit(self.text1, self.text_rect)
        screen.blit(self.resize2, self.button_rect2)
        screen.blit(self.text2, self.text2_rect)
        return bfs, itd,solution

# start_btn = button(114, 48, start_btn, 'start', )
screen_w = 755
screen_h = 900
rows = 9
columns = 9
available_grid_area = 900 - 300
cell_size = 70
black = (0, 0, 0)
white = (255, 255, 255)
medium_pink = '#E8D3DD'
dark_pink = '#DDB7AB'
grey_green = '#9A9B87'
brown = '#AD8E85'
beige = '#F4EEED'
neon_yellow = 'FFFF00'
bfs = False
itd = False
fps = 60
fpsClock = pygame.time.Clock()
canvas = pygame.display.set_mode((screen_w, screen_h))
canvas.fill(beige)
pygame.display.set_caption("maze problem")
font = pygame.font.SysFont('Arial', 40)
start_btn = pygame.image.load('start_button.png').convert_alpha()
clear_btn = pygame.image.load('clear button.png').convert_alpha()

click = 0
flag_event = 1
drawing_line = False
margin = 5
row = 0
column = 0
lrectangle = []
lrectangle_row = []

def draw_grid(itd, solution):
    for row in range(10):
        for column in range(10):
            color = white
            if m.maze[row][column] == 1:
                color = dark_pink
            if m.maze[row][column] == 2:
                color = grey_green
                Maze.set_start(m,row,column)
            if m.maze[row][column] == 3:
                color = brown
                Maze.set_goal(m,row,column)
            # if itd == True:
            #     #for r in range(len(solution)):
            #     r = 1
            #         #print(solution[r])
            #     if m.maze[getattr(solution[r], 'x')][getattr(solution[r], 'y')] == 0:
            #         #print('hi')
            #         color = grey_green
            #         print(solution[r])
            #         print(m.maze[getattr(solution[r], 'x')][getattr(solution[r], 'y')])
            if len(solution) == 0:
                pygame.draw.rect(canvas,
                                 color,
                                 [(margin + cell_size) * column + margin,
                                  (margin + cell_size) * row + margin,
                                  cell_size,
                                  cell_size])
            else:
                for r in range(len(solution)):
                    x = getattr(solution[r], 'x')
                    y = getattr(solution[r], 'y')
                    print(x,y)
                    pygame.draw.rect(canvas, (0, 0, 0), [margin + (cell_size * y) + margin, margin + (cell_size * x) + margin, cell_size, cell_size], 0)



new_buttons = button_2()
solution = []
drag = False
while True:
    for event in pygame.event.get():
        curser = pygame.mouse.get_pos()
        new_buttons.hover(curser[0], curser[1])
        status = new_buttons.display_buttons(canvas, curser, bfs, itd)
        if event.type == pygame.QUIT:
            pygame.quit()
            #iterative_deepening_search()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            new_buttons.hover(mouse_position[0], mouse_position[1])
            #status = new_buttons.display_buttons()
            column = mouse_position[0] // (cell_size + margin)
            row = mouse_position[1] // (cell_size + margin)
            #print(row, ',', column)
            if mouse_position[1] < 750 and mouse_position[1] > 0:
                drag = True
                click += 1
                if click == 1:
                    m.maze[row][column] = 2
                if click == 2:
                    m.maze[row][column] = 3
                # if click > 2:
                #     m.maze[row][column] = 1

            # if click == 1 and status[0] == False and status[1] == False:
            #     m.maze[row][column] = 2
            # elif click == 2 and status[0] == False and status[1] == False:
            #     m.maze[row][column] = 3
                # print(status[0])
                # print(status[1])


            print(mouse_position)
            print(m.maze)
        if event.type == pygame.MOUSEMOTION and drag == True:
            mouse_position2 = pygame.mouse.get_pos()
            column = mouse_position2[0] // (cell_size + margin)
            row = mouse_position2[1] // (cell_size + margin)
            if click > 2:
                m.maze[row][column] = 1
        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
    status = new_buttons.display_buttons(canvas, curser, bfs, itd)
    if len(status[2]) > 0:
        solution = status[2]
    print('status: ', solution)
    draw_grid(status[1], solution)

    #------------------------------------------------------------------------------------
    game = Game()
    fringe = []
    visited = []


    def iterative_deepening_search():
        game.clear_parents()
        solution = ids()
        return solution


    def ids():
        goal_state = None
        solution = []
        expanded_nodes = []
        depth = -1
        f = 1

        while goal_state is None and depth <= game.maze.limit:
            depth += 1
            fringe.clear()
            visited.clear()
            # print(game.root)
            fringe.append(game.root)
            expanded_nodes.append("On depth " + str(depth) + ":")

            while len(fringe) > 0:
                pop_index = len(fringe) - 1
                current_node = fringe.pop(pop_index)

                visited.append(current_node)
                # for m in visited:
                # print(m)

                if is_goal(current_node):
                    goal_state = current_node
                    break
                parent = current_node
                # print(current_node.v)

                for i in range(depth):
                    if parent is None:
                        parent = parent
                    else:
                        parent = parent.parent

                if parent is None:
                    f = 0
                    add_to_fringe(current_node, f)

            for node in visited:
                expanded_nodes.append(node)

        if goal_state is None:
            print("No goal state found.")
            return

        current = goal_state

        while current is not None:
            solution.insert(0, current)
            current = current.parent

        results(solution, expanded_nodes)
        itd = True
        return solution


    def add_to_fringe(current_node, f):
        nodes_to_add = []
        if current_node.right is not None and not is_in_visited(current_node.right):
            # print("right")
            nodes_to_add.append(set_parent(current_node, current_node.right, f))

        if current_node.down is not None and not is_in_visited(current_node.down):
            # print("down")
            nodes_to_add.append(set_parent(current_node, current_node.down, f))

        if current_node.left is not None and not is_in_visited(current_node.left):
            nodes_to_add.append(set_parent(current_node, current_node.left, f))
            # print("left")

        if current_node.up is not None and not is_in_visited(current_node.up):
            nodes_to_add.append(set_parent(current_node, current_node.up, f))
            # print("up")

        # print(nodes_to_add)
        for i in nodes_to_add:
            fringe.append(i)
        # for x in fringe:
        # print(x)


    def set_parent(parent_node, child_node, f):
        if child_node.parent is None or f == 0:
            child_node.parent = parent_node
            return child_node


    def is_in_visited(node):
        if node in visited:
            return True
        return False

    def is_goal(node):
        # print(game.maze.goal_x)

        if game.maze.goal_x == node.x and game.maze.goal_y == node.y:
            print("-*----------------------------------------------*-")
            print("THE GOAL HAS REACHED ;)")
            # print(game.maze.goal_x,game.maze.goal_y)
            return True

        else:
            return False

    def results(solution, expanded_nodes):
        itd = True
        print(("# of nodes in solution path is :  " + str(len(solution))))
        print("Solution path is :", end=" ")
        for i in solution:
            print(i, end=" ")
        print()
        print("(" + str(len(expanded_nodes)) + ")" + " Nodes have been expanded")

        for i in range(len(expanded_nodes) - 1):
            if type(expanded_nodes[i + 1]) == str:
                print(expanded_nodes[i])
            else:
                print(expanded_nodes[i], end=" ")

        print("\n")


    def BFS():
        solution = []

        if len(fringe) == 0:
            fringe.append(game.root)

        while (len(fringe) > 0):
            current_node = fringe.pop(0)

            if current_node not in visited:
                visited.append(current_node)

            if is_goal(visited[len(visited) - 1]):
                break

        parent = current_node



    # if goal_state is None:
    #     print("No goal state found.")
    #     return
    #
    # current = goal_state
    #
    # while current is not None:
    #     solution.insert(0, current)
    #     current = current.parent
    #
    # results(solution, expanded_nodes)

    pygame.display.update()



