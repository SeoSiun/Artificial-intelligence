
class State:
    def __init__(self, queen):
        self.queen = queen

    def getNextState(self, pos):
        newQueen = self.queen.copy()
        newQueen.append(pos)

        return State(newQueen)

    def isGoal(self, n):
        if len(self.queen) < n:
            return False

        for i in range(0, n):
            for j in range(i+1, n):
                print("(",i,",",self.queen[i],") (",j,",",self.queen[j],")")
                if self.queen[i] == self.queen[j] or abs(self.queen[i]-self.queen[j])==abs(j-i):
                    return False
                else: continue

        return True

    def toString(self, n):
        goal = ""
        for i in range(0, n):
            goal = goal + str(self.queen[i]+1) + " "
        return goal
            
            
        

def solve(n):
    if n==0: return "no solution"
    queue = []
    queue.append(State([]))

    while len(queue) > 0:
        state = queue.pop(0)

        if len(state.queen) == n:
            if state.isGoal(n):
                print("find goal!!")
                return state.toString(n)
        else:
            print("expand")
            # expand
            for i in range(0, n):
                queue.append(state.getNextState(i))

    return "no solution"
            
