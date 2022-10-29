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

    level = 0
    fringe = []
    visited = []

    def initializeDirections(self):
        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def check_path(self):
        # print('start: ', self.start_x, ', ' , self.start_y)
        # print('starting cell: ' ,self.maze[self.start_x][self.start_y])
        # print('below starting cell:', self.maze[self.start_x + 1][self.start_y])
        # print('above starting cell:', self.maze[self.start_x - 1][self.start_y])
        # print('right starting cell:', self.maze[self.start_x][self.start_y + 1])
        # print('left starting cell:', self.maze[self.start_x][self.start_y - 1])
        # print('child: ', self.start_x + 1, ', ' , self.start_y)
        self.initializeDirections()
        parent = node(self.start_x,self.start_y,None, self.maze[self.start_x][self.start_y],None,None,None,None)
        self.fringe.append(parent)
        if self.maze[self.start_x + 1][self.start_y] != 1:  #check down
            self.down = True
            #print(self.down)
            child = node(self.start_x + 1, self.start_y, None, self.maze[self.start_x + 1][self.start_y],None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.start_x - 1][self.start_y] != 1:  #check up
            self.up = True
            child = node(self.start_x - 1, self.start_y, None, self.maze[self.start_x - 1][self.start_y],None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.start_x][self.start_y + 1] != 1: #right
            self.right = True
            child = node(self.start_x, self.start_y + 1, None, self.maze[self.start_x][self.start_y + 1], None,None,None,None)
            self.fringe.append(child)

        if self.maze[self.start_x][self.start_y - 1] != 1: #left
            self.left = True
            child = node(self.start_x, self.start_y - 1, None, self.maze[self.start_x][self.start_y - 1], None,None,None,None)
            self.fringe.append(child)

        # for i in self.fringe:
        #     print('cell , x: ', i.x, ', y: ', i.y, ', v: ', i.v)
        #     if i.up:
        #         print('up: ', i.up)
        #     if i.down:
        #         print('down: ', i.down)
        #     if i.right:
        #         print('right: ', i.right)
        #     if i.left:
        #         print('left: ', i.left)


    def iterative_deepening(self):
        if self.level > self.limit:
            print('limit exceeded')
            return
        else:
            self.check_path()
            #self.fringe.pop()
            print('fringe before pop')
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

            print('1st cell in fringe: , x: ', self.fringe[0].x, ', y: ', self.fringe[0].y, ', v: ', self.fringe[0].v)
            #print('stack , x: ', self.fringe.pop().x, ', y: ', self.fringe.pop().y, ', v: ', self.fringe.pop().v)
            self.visited.append(self.fringe.pop())
            print('fringe after pop')
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
            print(self.visited[0].v)
            #self.visited.append(LIFO)
            # last_cell = len(self.visited) - 1
            # if self.visited[last_cell] == self.goal and last_cell > -1:
            #     return;
            # else:

            #self.iterative_deepening(self, self.level + 1)



test = Maze(1,1,7,8,1)
test.iterative_deepening()
