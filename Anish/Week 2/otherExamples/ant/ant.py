from functools import partial

def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2): 
    return partial(progn,out1,out2)

def prog3(out1, out2, out3):     
    return partial(progn,out1,out2,out3)

def if_then_else(condition, out1, out2):
    out1() if condition() else out2()

class AntSimulator(object):
    direction = ["north","east","south","west"]
    dir_row = [1, 0, -1, 0]
    dir_col = [0, 1, 0, -1]

    def __init__(self, max_moves):
        self.max_moves = max_moves
        self.moves = 0
        self.eaten = 0
        self.routine = None

    def _reset(self):
        self.row = self.row_start 
        self.col = self.col_start 
        self.dir = 1
        self.moves = 0  
        self.eaten = 0
        self.matrix_exc = copy.deepcopy(self.matrix)

    @property
    def position(self):
        return (self.row, self.col, self.direction[self.dir])

    def turn_left(self): 
        print('left')
        self.moves += 1 
        '''if self.moves < self.max_moves:
            self.moves += 1
            self.dir = (self.dir - 1) % 4'''

    def turn_right(self):
        print('right')
        self.moves += 1 
        '''if self.moves < self.max_moves:
            self.moves += 1    
            self.dir = (self.dir + 1) % 4'''

    def move_forward(self):
        print('forward')
        self.moves += 1
        '''if self.moves < self.max_moves:
            self.moves += 1
            self.row = (self.row + self.dir_row[self.dir]) % self.matrix_row
            self.col = (self.col + self.dir_col[self.dir]) % self.matrix_col
            if self.matrix_exc[self.row][self.col] == "food":
                self.eaten += 1
            self.matrix_exc[self.row][self.col] = "passed"'''

    def sense_food(self):
        return False
        '''ahead_row = (self.row + self.dir_row[self.dir]) % self.matrix_row
        ahead_col = (self.col + self.dir_col[self.dir]) % self.matrix_col        
        return self.matrix_exc[ahead_row][ahead_col] == "food"'''

    def if_food_ahead(self, out1, out2):
        return partial(if_then_else, self.sense_food, out1, out2)

    def run(self,routine):
        #self._reset()
        while self.moves < self.max_moves:
            routine()

ant = AntSimulator(1)

ant.routine = ant.if_food_ahead(ant.move_forward, prog3(ant.turn_left, 
                                                  prog2(ant.if_food_ahead(ant.move_forward, ant.turn_right), 
                                                        prog2(ant.turn_right, prog2(ant.turn_left, ant.turn_right))),
                                                  prog2(ant.if_food_ahead(ant.move_forward, ant.turn_left), ant.move_forward)))

'''
(left, (right, (right, (left, right))), (left, forward))()
(left, (right))
progs get replaced with partial obj
'''

ant.routine = prog2(prog2(ant.turn_left, prog2(ant.turn_right, ant.move_forward)), ant.move_forward)


print(ant.routine)
ant.run(ant.routine)