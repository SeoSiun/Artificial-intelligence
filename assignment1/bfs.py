
class State:
    def __init__(self, queen, n):
        self.queen = queen
        self.n = n

    def getNextState(self, pos):
        newQueen = self.queen.copy()
        newQueen.append(pos)

        return State(newQueen, self.n)

    def isGoal(self):
        if len(self.queen) < self.n:
            return False

        for i in range(0, self.n):
            for j in range(i+1, self.n):
                if self.queen[i] == self.queen[j] or abs(self.queen[i]-self.queen[j])==abs(j-i):
                    return False
                else: continue

        return True

    def toString(self):
        goal = ""
        for i in range(0, self.n):
            goal = goal + str(self.queen[i]+1) + " "
        return goal              
        
def bfs(n):
    if n==0: return "no solution"
    queue = []
    queue.append(State([], n))

    while len(queue) > 0:
        state = queue.pop(0)

        if len(state.queen) == n:
            if state.isGoal():
                return state.toString()
        else:
            # expand
            for i in range(0, n):
                queue.append(state.getNextState(i))

    return "no solution"
            
