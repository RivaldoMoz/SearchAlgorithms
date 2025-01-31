from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance heuristic

def bestFirst(m):
    start = (m.rows, m.cols)
    goal = (1, 1)
    open_queue = PriorityQueue()
    open_queue.put((h(start, goal), start))
    aPath = {}
    visited = set()

    while not open_queue.empty():
        currCell = open_queue.get()[1]
        if currCell == goal:
            break
        if currCell in visited:
            continue
        visited.add(currCell)

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
                    heuristic = h(childCell, goal)
                    open_queue.put((heuristic, childCell))
                    if childCell not in aPath:
                        aPath[childCell] = currCell

    # Reconstruct path
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath

if __name__ == '__main__':
    m = maze(5, 5)
    m.CreateMaze()
    path = bestFirst(m)

    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path})
    l = textLabel(m, 'Best First Path Length', len(path) + 1)

    m.run()