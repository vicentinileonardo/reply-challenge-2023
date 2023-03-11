import copy
import time
import argparse

class Snake:
    def __init__(self):
        self.number = None
        self.length = 0
        self.start_x = None
        self.start_y = None
        self.movements = []
        self.skip = False
        self.placed = False

    def move(self, direction):
        self.movements.append(direction)
    
    def out(self):
        if self.skip:
            return ''
        else:
            out_list =  [
                str(self.start_x),
                str(self.start_y), 
            ]

            out_list.extend(self.movements)

            return ' '.join(out_list)
    
    def __repr__(self):
        return f"[{self.number}]: start_x: {self.start_x}, start_y: {self.start_y}, length: {self.length}"

def number_grid(grid):
    tmp_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if tmp_grid[i][j] != '*':
                tmp_grid[i][j] = int(tmp_grid[i][j])
            else:
                tmp_grid[i][j] = -1

    return tmp_grid

def read_input(path):
    with open(path, 'r') as f:
        data = f.read()

    C, R, S = list(map(int, data.split('\n')[0].split(' ')))
    snakes = []
    grid = []
    rows_with_wormholes = []

    snakes_info = data.split('\n')[1].split(' ')
    for i in range(S):
        s = Snake()
        s.number = i
        s.length = int(snakes_info[i])
        snakes.append(s)

    data = data.split('\n')[2:]
    for row in range(R):
        grid.append(data[row].split(' '))

    wormholes = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '*':
                wormholes.append((i,j))
                rows_with_wormholes.append(i)

    return C, R, S, snakes, grid, wormholes, rows_with_wormholes

def output(path, snakes):
    with open(path, 'w') as f:
        f.write('\n'.join([s.out() for s in snakes]))

def output_points(path, input_file, points, time):
    with open(path, 'a') as f:
        f.write(f"[{input_file}]: ")
        f.write(str(points))
        f.write(' - Time elapsed: ')
        f.write(str(time))
        f.write('\n')

def place_snakes():
    last_placed = None
    for row in range(R):
        if row in rows_with_wormholes:
            continue  # skip row
        else:
            for snake in snakes:
                if not snake.placed:
                    # place snake
                    snake.start_x = 0
                    snake.start_y = row

                    # add points of initial position
                    add_points(row, 0)

                    # move snake
                    for i in range(snake.length - 1):
                        # check if next position is still in grid
                        if i + 1 < C:
                            snake.move('R')
                            # add points of all positions occupied by snake
                            add_points(row, i + 1)
                        else:
                            break
                        
                    snake.placed = True
                    last_placed = snake.number
                    break
           
    # loop through snakes not placed starting from last placed
    for snake in snakes[last_placed:]:
        if not snake.placed:
            snake.skip = True

def add_points(i, j):
    global current_points
    current_points += grid[i][j]
    
if __name__ == '__main__':

    INPUT_PATH_0 = './input_files/00-example.txt'
    INPUT_PATH_1 = './input_files/01-chilling-cat.txt'
    INPUT_PATH_2 = './input_files/02-swarming-ant.txt'
    INPUT_PATH_3 = './input_files/03-input-anti-greedy.txt'
    INPUT_PATH_4 = './input_files/04-input-low-points.txt'
    INPUT_PATH_5 = './input_files/05-input-opposite-points-holes.txt'
    INPUT_PATH_6 = './input_files/06-input-reply-running-man.txt'

    OUTPUT_PATH_0 = './output_files/00_out.txt'
    OUTPUT_PATH_1 = './output_files/01_out.txt'
    OUTPUT_PATH_2 = './output_files/02_out.txt'
    OUTPUT_PATH_3 = './output_files/03_out.txt'
    OUTPUT_PATH_4 = './output_files/04_out.txt'
    OUTPUT_PATH_5 = './output_files/05_out.txt'
    OUTPUT_PATH_6 = './output_files/06_out.txt'

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=int, default=0)

    args = parser.parse_args()

    if args.input == 0:
        INPUT_PATH = INPUT_PATH_0
        OUTPUT_PATH = OUTPUT_PATH_0
    elif args.input == 1:
        INPUT_PATH = INPUT_PATH_1
        OUTPUT_PATH = OUTPUT_PATH_1
    elif args.input == 2:
        INPUT_PATH = INPUT_PATH_2
        OUTPUT_PATH = OUTPUT_PATH_2
    elif args.input == 3:
        INPUT_PATH = INPUT_PATH_3
        OUTPUT_PATH = OUTPUT_PATH_3
    elif args.input == 4:
        INPUT_PATH = INPUT_PATH_4
        OUTPUT_PATH = OUTPUT_PATH_4
    elif args.input == 5:
        INPUT_PATH = INPUT_PATH_5
        OUTPUT_PATH = OUTPUT_PATH_5
    elif args.input == 6:
        INPUT_PATH = INPUT_PATH_6
        OUTPUT_PATH = OUTPUT_PATH_6
    else:
        print('Invalid input file')
        exit()

    C, R, S, snakes, grid, wormholes, rows_with_wormholes = read_input(INPUT_PATH)

    #convert grid to numbers
    grid = number_grid(grid)

    print(f"C: {C}, R: {R}, S: {S}")
    #print(f"Snakes: {snakes}")
    #print(f"Grid: {grid}")
    #print(f"Wormholes: {wormholes}")
    #print(f"Rows with wormholes: {rows_with_wormholes}")

    start_time = time.time()
    current_points = 0
    place_snakes()
    
    output(OUTPUT_PATH, snakes)

    print(f"Final points: {current_points}")
    time_elapsed = round(time.time() - start_time, 5)
    print(f"Time elapsed: {time_elapsed} seconds")
    output_points('points.txt', INPUT_PATH, current_points, time_elapsed)
    
#TODO:
# next: find best window in the row to place snake
# next: try columns instead of rows
