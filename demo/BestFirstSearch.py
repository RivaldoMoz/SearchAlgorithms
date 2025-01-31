from pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2)) #Mahhatan distance

def BestFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), start))
    aPath = {}
    searchPath = []  
    visited = set()
    
    while not open.empty():
        currCell = open.get()[1]
        if currCell in visited:  # Skip already visited nodes
            continue
        visited.add(currCell)    # Mark as visited
        searchPath.append(currCell)  
        
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                if childCell not in visited:
                    heuristic = h(childCell, m._goal)
                    open.put((heuristic, childCell))
                    if childCell not in aPath:  # Keep first parent found
                        aPath[childCell] = currCell

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return searchPath, aPath, fwdPath

if __name__=='__main__':
    m=maze(20,20)
    m.CreateMaze()

    searchPath,aPath,fwdPath=BestFS(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols)) #1,1 is the goal maze in this case
    c=agent(m,footprints=True,color=COLOR.red)

    m.tracePath({a:searchPath},delay=3)
    m.tracePath({b:aPath},delay=3)
    m.tracePath({c:fwdPath},delay=3)

    l=textLabel(m,'Best First Path Length',len(fwdPath)+1)
    l=textLabel(m,'Best First Search Length',len(searchPath))
    m.run()
