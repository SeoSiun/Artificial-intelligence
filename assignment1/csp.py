class State:
    def __init__(self, variables, n, varCnt):
      # keep track remaining legal value for unassinged variables
      # if assigned, keep assigned value
      self.variables = variables
      self.n = n
      # num of assigned variable
      self.varCnt = varCnt

    def getNextState(self, value):
      # deep copy
      newVariables = []
      for _ in range(0,self.n):
        newVariables = [var[:] for var in self.variables]

      # assign value
      newVariables[self.varCnt] = [value]

      # remove new illegal value
      for i in range(self.varCnt+1, self.n):
        newVariables[i] = [var for var in newVariables[i] 
        if var != value 
        and var != value+(i-self.varCnt) 
        and var != value-(i-self.varCnt)]

      return State(newVariables, self.n, self.varCnt+1)
    
    # check value is legal
    def isLegalValue(self, value):
      if self.variables[self.varCnt].count(value) > 0: return True
      return False 
    
    def isEmptyVariable(self):
      if len(self.variables[self.varCnt]) ==0 : return True
      return False
    
    def isGoal(self):
      if self.varCnt == self.n: return True
      return False

    def toString(self):
      goal = ""
      for i in range(0, self.n):
        goal = goal + str(self.variables[i][0]+1) + " "
      return goal  
         
        
def csp(n):
    stack = []
    stack.append(State([[i for i in range(0,n)] for i in range(0,n)], n, 0))

    while len(stack) > 0:
      state = stack.pop()

      # if all variable is assigned, return result
      if state.isGoal(): return state.toString()

      # if variable has no leagal value, terminate
      if state.isEmptyVariable(): continue

      for i in range(0,n):
        # if value is not legal, assign value 
        if state.isLegalValue(n-1-i): 
          stack.append(state.getNextState(n-1-i))

    return "no solution"