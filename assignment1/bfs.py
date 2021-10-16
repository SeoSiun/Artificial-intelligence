
class State:
  def __init__(self, queens, n):
      # queen position
      self.queens = queens
      self.n = n

  def getNextState(self, pos):
      newQueens = self.queens[:]
      newQueens.append(pos)
      return State(newQueens, self.n)

  # goal test
  def isGoal(self):
    for i in range(0, self.n):
      for j in range(i+1, self.n):
        if self.queens[i] == self.queens[j] or abs(self.queens[i]-self.queens[j])==abs(j-i): return False
    return True
  
  def isLeaf(self):
    if len(self.queens)==self.n: return True
    return False

  def toString(self):
      goal = ""
      for i in range(0, self.n):
          goal = goal + str(self.queens[i]+1) + " "
      return goal              
        
def bfs(n):
  queue = []
  queue.append(State([], n))

  while len(queue) > 0:
      state = queue.pop(0)

      # if leaf, goal test
      if state.isLeaf():
        if state.isGoal(): return state.toString()

      # if nonleaf, expand
      else:
        for i in range(0, n):
          queue.append(state.getNextState(i))

  return "no solution"