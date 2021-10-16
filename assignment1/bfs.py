
class State:
  def __init__(self, queens, n):
      # queen position
      self.queens = queens
      self.n = n

  def getNextState(self, pos):
      newQueen = self.queens[:]
      newQueen.append(pos)
      return State(newQueen, self.n)

  # goal test
  def isGoal(self):
    if len(self.queens) < self.n:
      return False

    for i in range(0, self.n):
      for j in range(i+1, self.n):
        if self.queens[i] == self.queens[j] or abs(self.queens[i]-self.queens[j])==abs(j-i): return False
    return True

  def toString(self):
      goal = ""
      for i in range(0, self.n):
          goal = goal + str(self.queens[i]+1) + " "
      return goal              
        
def bfs(n):
  if n==0: return "no solution"

  queue = []
  queue.append(State([], n))

  while len(queue) > 0:
      state = queue.pop(0)

      # if leaf, goal test
      if len(state.queens) == n:
          if state.isGoal(): return state.toString()

      # if nonleaf, expand
      else:
          for i in range(0, n):
              queue.append(state.getNextState(i))

  return "no solution"