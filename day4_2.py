def is_valid(x, y):
    return 0 <= x < cols and 0 <= y < rows

rows = len(grid)
cols = len(grid[0])

pattern = "MAS"

right_search = [(-1,-1), (1,1)]
left_search = [(-1,1), (1,-1)]

count = 0

for x in range(rows):
    for y in range(cols):
            if not is_valid(x, y):
                continue
                
            if grid[y][x] != 'A':
                continue
                pass
            else:
                x1 = x+right_search[0][1]
                y1 = y+right_search[0][0]

                x2 = x+right_search[1][1]
                y2 = y+right_search[1][0]

                x3 = x+left_search[0][1]
                y3 = y+left_search[0][0]

                x4 = x+left_search[1][1]
                y4 = y+left_search[1][0]
                

                if not all(is_valid(x_, y_) for x_, y_ in [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]):
                    continue
                elif (grid[y1][x1] == 'M' and grid[y2][x2] == 'S') or (grid[y1][x1] == 'S' and grid[y2][x2] == 'M'):
                        if (grid[y3][x3] == 'M' and grid[y4][x4] == 'S') or (grid[y3][x3] == 'S' and grid[y4][x4] == 'M'):
                             count += 1
                        else:
                             pass
                else:
                    pass
                     
print(count)
