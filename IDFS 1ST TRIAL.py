from collections import deque
class node:
    def __init__(self, x, y, g, value, up, down, right, left):
        self.x = x
        self.y = y
        self.g = g
        self.v = value
        self.up = up
        self.down = down
        self.right = right
        self.left = left



class Maze:
    def __init__(self, start_x: object, start_y: object, end_x: object, end_y: object, limit: object) -> object:
       self.M = 10
       self.N = 8
       self.start_x = start_x
       self.start_y = start_y
       self.goal_x = end_x
       self.goal_y = end_y
       # self.up = None
       # self.down = None
       # self.right = None
       # self.left = None
       self.limit = limit
       self.maze = [ [1,2,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,1,1,1,1,1,1,0,1],
                     [1,0,1,0,0,0,0,0,0,1],
                     [1,0,1,0,1,1,1,1,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,2,1] ]
       self.parent = node(self.start_x, self.start_y, None, self.maze[self.start_x][self.start_y], None, None, None, None)
    level = 0
    fringe = []
    visited = []

    def initializeDirections(self):
        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def check_visited(self, parent):
        print('hi')
        if len(self.visited) > 0:
            print('hello')
            if parent in self.visitied:
                return True
        return False
    def PrintFringe(self):
        print('fringe: ')
        for i in self.fringe:
            print('cell , x: ', i.x, ', y: ', i.y, ', v: ', i.v)
            if i.up:
                print('up: ', i.up)
            if i.down:
                print('down: ', i.down)
            if i.right:
                print('right: ', i.right)
            if i.left:
                print('left: ', i.left)

    def PrintVisited(self):
        print('visited:')
        for i in self.visited:
            print('cell , x: ', i.x, ', y: ', i.y, ', v: ', i.v)
            if i.up:
                print('up: ', i.up)
            if i.down:
                print('down: ', i.down)
            if i.right:
                print('right: ', i.right)
            if i.left:
                print('left: ', i.left)
    def expandParent(self):
        #print('hi')
        if self.maze[self.parent.x + 1][self.parent.y] != 1:  #check down
            self.down = True
            #print(self.down)
            child = node(self.parent.x + 1, self.parent.y, None, self.maze[self.parent.x + 1][self.parent.y],None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.parent.x - 1][self.parent.y] != 1:  #check up
            self.up = True
            child = node(self.parent.x - 1, self.parent.y, None, self.maze[self.parent.x - 1][self.parent.y],None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.parent.x][self.parent.y + 1] != 1: #right
            self.right = True
            child = node(self.parent.x, self.parent.y + 1, None, self.maze[self.parent.x][self.parent.y + 1], None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.parent.x][self.parent.y - 1] != 1: #left
            self.left = True
            child = node(self.parent.x, self.parent.y - 1, None, self.maze[self.parent.x][self.parent.y - 1], None,None,None,None)
            self.fringe.append(child)
    def check_path(self):
        # print('start: ', self.start_x, ', ' , self.start_y)
        # print('starting cell: ' ,self.maze[self.start_x][self.start_y])
        # print('below starting cell:', self.maze[self.start_x + 1][self.start_y])
        # print('above starting cell:', self.maze[self.start_x - 1][self.start_y])
        # print('right starting cell:', self.maze[self.start_x][self.start_y + 1])
        # print('left starting cell:', self.maze[self.start_x][self.start_y - 1])
        # print('child: ', self.start_x + 1, ', ' , self.start_y)
        self.initializeDirections()

        self.fringe.append(self.parent)
        #self.check_visited(parent)
        if self.check_visited(self.parent) == False:
            self.expandParent()

    def iterative_deepening(self):
        if self.level > self.limit:
            print('limit exceeded')
            return
        else:
            self.check_path()
            #self.fringe.pop()
            self.PrintFringe()

            print('1st cell in fringe: , x: ', self.fringe[0].x, ', y: ', self.fringe[0].y, ', v: ', self.fringe[0].v)
            #print('stack , x: ', self.fringe.pop().x, ', y: ', self.fringe.pop().y, ', v: ', self.fringe.pop().v)
            self.parent = self.visited.append(self.fringe.pop())
            self.PrintFringe()
            self.PrintVisited()
            #self.visited.append(LIFO)
            # last_cell = len(self.visited) - 1
            # if self.visited[last_cell] == self.goal and last_cell > -1:
            #     return;
            # else:

            #self.iterative_deepening(self, self.level + 1)



test = Maze(1,1,7,8,1)
test.iterative_deepening()
