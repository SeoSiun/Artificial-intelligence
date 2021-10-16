import random

class State:
  def __init__(self, n):
    self.n = n
    # queen position (init random position)
    self.queens = []
    for i in range(0,n):
      self.queens.append(random.randrange(0,n))
    self.h = self.getH(self.queens)
  
  # get num of pairs of queens that are attacking each other
  def getH(self, tmp):
    cnt=0
    for i in range(0, self.n):
        for j in range(i+1, self.n):
            if tmp[i] == tmp[j] or abs(tmp[i]-tmp[j])==abs(j-i):
                cnt = cnt+1
    return cnt

  def getNextState(self):
      minH = self.h
      # coordinate to move
      coord = []

      # find min H
      # if min H is many, select first one
      for i in range(0,self.n):
        for j in range(0,self.n):
          # curruent pos, pass
          if self.queens[i]==j: continue

          # if queen move to (i,j), calculate H
          tmp = self.queens[:]
          tmp[i] = j
          newH = self.getH(tmp)

          # update minH and coord
          if newH < minH :
            minH = newH
            coord = [i,j]

      # if find minH, move queen
      if minH < self.h:
        self.queens[coord[0]] = coord[1]
        self.h = minH

      # stuck
      else: self.h = -1

  def toString(self):
      goal = ""
      for i in range(0, self.n):
          goal = goal + str(self.queens[i]+1) + " "
      return goal   

def hc(n):
  if n==0 or n==2 or n==3 : return "no solution"
  
  while True:
    state = State(n)

    # move until find peak
    while state.h > 0: state.getNextState()
    
    # peak == goal
    if state.h == 0: return state.toString()


