def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0]) # since it's a square, shouldn't matter. If it were a different shape then I'd have to rethink it
    
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_pattern(start_x, start_y, dx, dy):
        pattern = "XMAS"
        x, y = start_x, start_y
        
        # Check if first letter matches
        if grid[x][y] != pattern[0]:
            return False
        
        # Continue searching next letters along path
        for letter in pattern[1:]:
            x += dx
            y += dy
            
            # Check if still in grid and letter matches
            if not is_valid(x, y) or grid[x][y] != letter:
                return False
        
        return True
    
    # Try from every position in the grid, add up successes
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_pattern(x, y, dx, dy):
                    count+=1

    return count


# get answer
with open('data/day4.txt','r') as file:
    grid = [list(line) for line in file]

print(find_xmas(grid))