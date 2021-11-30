import random

class QLearning:
  def __init__(self, map, sPoint):
    self.map = map
    self.sPoint = sPoint
    self.Q = []
    self.initQ()
    #  Down: +5 | Up: -5 | Right: +1 | Left: -1
    self.ACTION = {'D': 5, 'U': -5, 'R': 1, 'L': -1}
    # S: Start, G: Goal, T: Bonus, B: Bomb, P: Normal Path
    self.REWARD = {'S': 0, 'G': 100, 'T': 10, 'B': -100, 'P': 0}
    self.r = 0.9
  
  # set Q(s,a) = 0 for available (s,a) pair
  def initQ(self):
    for s in range(0,25):
      tmp = {'D': 0, 'U': 0, 'R': 0, 'L': 0}
      # last row
      if int(s / 5) == 4 : del(tmp['D'])
      # first row
      if int(s / 5) == 0 : del(tmp['U'])
      # last col
      if s % 5 == 4 : del(tmp['R'])
      # first col
      if s % 5 == 0 : del(tmp['L'])
      self.Q.append(tmp)

  # Q-Learning
  def learning(self):
    curState = random.randint(0,24)

    for i in range(0,10000):
      # if curState is Bomb or Goal, restart
      while self.map[curState] == 'B' or self.map[curState] == 'G':
        curState = random.randint(0,24)
      
      # select action ramdomly       
      curAction = random.choice(list(self.Q[curState]))
      # s'
      newState = curState + self.ACTION[curAction]
      # r(s,a) : immediate reward
      curReward = self.REWARD[self.map[newState]]
      # Q(s,a) = r(s,a) + r * max((Q(s',a')))
      self.Q[curState][curAction] = curReward + self.r * max(self.Q[newState].values())
      # s = s'
      curState = newState
      
    ##############
    for i in range(0,25):
      print(self.Q[i])
    ##############
    
    self.printOutput()

  # print path and max Q at start point to output.txt
  def printOutput(self):
    fName = "output.txt"
    fOutput = open(fName,'w')
    
    # set start point
    curState = self.sPoint
    # print path
    fOutput.write(str(curState))
    while self.map[curState] != 'G':
      # select action that maximize Q(s,a) and update curState
      curState = curState + self.ACTION[max(self.Q[curState],key = self.Q[curState].get)]
      fOutput.write(" " + str(curState))
    # print max Q(s,a) at start point
    fOutput.write("\n" + str(max(self.Q[self.sPoint].values())))
    
    fOutput.close()

        
def main():
  map = []
  sPoint = []
  
  fInput = open("input.txt")

  # read file and remove '\n'
  input = fInput.read().replace('\n','')
  # convert input to array
  map = list(input)
  # find index of start point
  sPoint = input.find('S')
  
  fInput.close()
  
  q = QLearning(map,sPoint)
  q.learning()
  
if __name__ == "__main__":
  main()