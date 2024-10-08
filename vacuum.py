import random

class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)

    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 1:
            print(f"Cleaning position {self.position}")
            self.grid[x][y] = 0  # Clean the current position
        else:
            print(f"Position {self.position} is already clean")

    def move(self, direction):
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < len(self.grid) - 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < len(self.grid[0]) - 1:
            self.position = (x, y + 1)
        else:
            print("Move not possible")

    def run(self):
        total_cells = len(self.grid) * len(self.grid[0])
        cleaned_cells = 0
       
        while cleaned_cells < total_cells:
            self.clean()
            cleaned_cells += 1
           
            # Move in a simple pattern until all cells are cleaned
            if self.position[1] < len(self.grid[0]) - 1:  # Move right if possible
                self.move('right')
            elif self.position[0] < len(self.grid) - 1:  # Move down if possible
                self.move('down')
            elif self.position[1] > 0:  # Move left if possible
                self.move('left')
            elif self.position[0] > 0:  # Move up if possible
                self.move('up')
            else:
                print("No more moves possible")
                break

        print("Final grid state:")
        for row in self.grid:
            print(row)

    @staticmethod
    def dirty_random_cells(grid, num_dirty_cells):
        cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        random.shuffle(cells)
        for cell in cells[:num_dirty_cells]:
            grid[cell[0]][cell[1]] = 1  # Mark cell as dirty

# Get user input for grid dimensions and number of dirty cells
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
num_dirty_cells = int(input("Enter the number of dirty cells: "))

# Validate the number of dirty cells
if num_dirty_cells > rows * cols:
    print("Number of dirty cells exceeds total cells in the grid. Adjusting to maximum.")
    num_dirty_cells = rows * cols

# Initialize the grid
initial_grid = [[0 for _ in range(cols)] for _ in range(rows)]  # Start with a clean grid
VacuumCleaner.dirty_random_cells(initial_grid, num_dirty_cells)

vacuum = VacuumCleaner(initial_grid)
print("Initial grid state:")
for row in initial_grid:
    print(row)

vacuum.run()
