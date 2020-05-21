import time


class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('*', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()
        print()

    def __eq__(self, other):
        if isinstance(other, list):
            for l in range(len(other)):
                if self.location[0] == other[l].location[0] and self.location[1] == other[l].location[1]:
                    return True
        if isinstance(other, Maze):
            return self.location[0] == other.location[0] and self.location[1] == other.location[1]
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        nexttovisit = []
        r = self.location[0]#|
        c = self.location[1]#--
        ## [Col][row]
        if self.grid[r][c + 1] == " ":
            """E"""
            nexttovisit.append("E")
        if self.grid[r][c - 1] == " ":
            """W"""
            nexttovisit.append("W")

        if self.grid[r + 1][c] == " ":
            """S"""
            nexttovisit.append("S")

        if self.grid[r - 1][c] == " ":
            """N"""
            nexttovisit.append("N")
        return nexttovisit

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        ok = Maze(self.grid, self.location)
        if move == "S":
            if (self.location[0] + 1, self.location[1]) != "X":
                ok.location = (self.location[0] + 1, self.location[1])
        if move == "N":
            if (self.location[0] - 1, self.location[1]) != "X":
                ok.location = (self.location[0] - 1, self.location[1])
        if move == "W":
            if (self.location[0], self.location[1] - 1) != "X":
                ok.location = (self.location[0], self.location[1] - 1)
        if move == "E":
            if (self.location[0], self.location[1] + 1) != "X":
                ok.location = (self.location[0], self.location[1] + 1)
        return ok

class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        prev = {}
        queue = [maze]
        visited = [maze]
        if maze == goal:
            return ""
        while queue:
            path = queue.pop(0)
            if maze == goal:
                return ""
            for i in path.moves():
                copy = path.neighbor(i)
                if copy.__eq__(visited):
                    continue
                if copy == goal:
                    prev[path.location] = [copy.location]
                    queue.clear()
                    break
                if copy.__ne__(visited):
                    if path.location in prev:
                        prev[path.location].append(copy.location)
                    else:
                        prev[path.location] = [copy.location]
                    visited.append(copy)
                    queue.append(copy)
        routefast = []
        inverted = {}
        for x, y in prev.items():
            for r in range(len(y)):
                te = y[r]
                inverted[te] = x
        yoko = inverted.get(goal.location)
        if goal.location not in inverted.keys():
            return ""
        routefast.append(goal.location)
        routefast.append(yoko)
        while inverted:
            if yoko == maze.location:
                break
            cool = inverted[yoko]
            yoko = cool
            routefast.append(yoko)
        routefast.reverse()
        return self.fastestbfs(routefast)

    def fastestbfs(self, lizt):
        fast = []
        for index in range(1, len(lizt)):
            temp = lizt[index]
            tempb = lizt[index - 1]
            if temp[0] > tempb[0]:
                fast.append("S")
            if temp[0] < tempb[0]:
                fast.append("N")
            if temp[1] > tempb[1]:
                fast.append("E")
            if temp[1] < tempb[1]:
                fast.append("W")
        return fast
def main():
    """Create a maze, solve it with BFS, and console-animate."""
    grid =  ["XXXXXXXXXXXXXXXXXXXX",
     "X     X    X       X",
     "X XXXXX XXXX XXX XXX",
     "X       X      X X X",
     "X X XXX XXXXXX X X X",
     "X X   X        X X X",
     "X XXX XXXXXX XXXXX X",
     "X XXX    X X X     X",
     "X    XXX       XXXXX",
     "XXXXX   XXXXXX     X",
     "X   XXX X X    X X X",
     "XXX XXX X X XXXX X X",
     "X     X X   XX X X X",
     "XXXXX     XXXX X XXX",
     "X     X XXX    X   X",
     "X XXXXX X XXXX XXX X",
     "X X     X  X X     X",
     "X X XXXXXX X XXXXX X",
     "X X                X",
     "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()
    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()
