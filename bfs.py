# Pyamaze is used to generate mazes to test the algorithm effiency in different maze sizes
from pyamaze import maze, agent, COLOR, textLabel
#This function return the shortest path using breatdh first algorithm
def breadthSearchAlgorithm(m):
    #First we add both of the start path in the frontier and explored and define the bfsPath to store the optimal path
    #This algorithm uses queue as the data structure so to mimic the behaviour of a queue I used a list, as we can implement fifo
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    #Check if frontier is empty. The logic is if frontier is zero the goal is reached
    while len(frontier)>0:
        currCell = frontier.pop(0)
        if currCell == (1,1):
            break
        #This code checks if to append or not in the frontier if the node has not yet been visited
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
    #As the path is reversed this code is to reorder form start to end of the maze 
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell] 
    return fwdPath
#Here is basic use of the pyamaze module 
#Dont be lazy read the Doc
if __name__ == "__main__" :
    m = maze(20,20)
    m.CreateMaze()  
    path = breadthSearchAlgorithm(m)         
    a = agent(m, footprints=True)
    lae =textLabel(m, "The Path of bfs is", len(path)+1)
    m.tracePath({a:path})
    m.run()
