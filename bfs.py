# Pyamaze is used to generate mazes to test the algorithm effiency in different maze sizes
from pyamaze import maze, agent, COLOR
#This function return the shortest path using breatdh first algorithm
def breadthSearchAlgorithm(m):
    #First we add both of the start path in the frontier and explored and define the bfsPath to store the optimal path
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    while len(frontier)>0:
        currCell = frontier.pop(0)
        if currCell == (1,1):
            break
        for d in "ESNW":
            if m.maze_map[currCell][d] == True:
                if d == "E":
                    childCell = (currCell[0], currCell[1]+1)
                elif d == "W":
                    childCell = (currCell[0], currCell[1]-1)
                elif d == "S":
                    childCell = (currCell[0]+1, currCell[1])
                elif d == "N":
                    childCell = (currCell[0]-1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1,1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell] 
    return fwdPath

m = maze(51,15)
m.CreateMaze()  
path = breadthSearchAlgorithm(m)         
a = agent(m, footprints=True)
m.tracePath({a:path})
m.run()