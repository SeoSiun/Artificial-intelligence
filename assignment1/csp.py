def constraintCheck(queen, var, value):
    queen[var] = value
    for i in range(0, len(queen)):
        if queen[i] == -1: continue
        for j in range(i+1, len(queen)):
            if queen[j] == -1: continue
            if queen[i] == queen[j] or abs(queen[i]-queen[j])==abs(j-i):
                return False
    return True

class State:
    def __init__(self, n):
        self.queen = [-1 for i in range(0,n)]
        self.n = n

    def getNextState(self, var, value):
        self.queen[var] = value

    def toString(self):
        goal = ""
        for i in range(0, self.n):
            goal = goal + str(self.queen[i]+1) + " "
        return goal              
        
def csp(n):
    if n==0: return "no solution"

    state = State(n)

    return recursiveCSP(state, 0)

def recursiveCSP(state, var):
    if var >= state.n: return state.toString()

    for i in range(0,state.n):
        if constraintCheck(state.queen.copy(),var,i):
            state.getNextState(var, i)
            result = recursiveCSP(state, var+1)
            if result != "no solution":
                return result
            state.getNextState(var,-1)
    return "no solution"
        
            
            
