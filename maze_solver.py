from collections import deque

print("Maze Solver")

maze = [
    "#######",
    "#S    #",
    "# ### #",
    "#   #E#",
    "#######",
]

for row in maze:
    print(row)

start=None
end=None

for row_index,row in enumerate(maze):
    for col_index,cell in enumerate(row):
        if cell=="S":
            start=(row_index,col_index)
        elif cell=="E":
            end=(row_index,col_index)

if start is None or end is None:
    print("Maze must contain both S and E.")
    raise SystemExit(1)

print("Start: ",start)
print("End: ",end)

def get_neighbors(position):
    row,col=position
    neighbors=[]

    directions=[
        (-1,0),
        (1,0),
        (0,-1),
        (0,1),
    ]

    for row_change,col_change in directions:
        next_row=row+row_change
        next_col=col+col_change

        if 0<=next_row<len(maze):
            if 0<= next_col<len(maze[next_row]):
                if maze[next_row][next_col]!="#":
                    neighbors.append((next_row,next_col))
    
    return neighbors

print("Start neighbors: ",get_neighbors(start))

def bfs(start,end):
    queue=deque([start])
    visited={start}
    parents={start:None}

    while queue:
        current=queue.popleft()

        if current==end:
            return parents

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor]=current
                queue.append(neighbor)
    return None

parents=bfs(start,end)

if parents is None:
    print("No path found.")
else:
    print("Exit found!")

def reconstruct_path(parents,end):
    path=[]
    current=end

    while current is not None:
        path.append(current)
        current=parents[current]
    
    path.reverse()
    return path

if parents is not None:
    path=reconstruct_path(parents,end)
    print("Path: ",path)
    print("Number of steps: ",len(path)-1)

def display_path(maze,path):
    solved_maze=[list(row) for row in maze]

    for row,col in path:
        if solved_maze[row][col] not in ("S","E"):
            solved_maze[row][col]="."

    for row in solved_maze:
        print("".join(row))

if parents is not None:
    print("Solved maze: ")
    display_path(maze,path)

    