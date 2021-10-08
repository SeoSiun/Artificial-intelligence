import random

def H(queen, n):
    cnt=0

    for i in range(0, n):
        for j in range(i+1, n):
            if queen[i] == queen[j] or abs(queen[i]-queen[j])==abs(j-i):
                cnt = cnt+1
    return cnt


class State:
    def __init__(self, n):
        self.queen = []
        for i in range(0,n):
            self.queen.append(random.randrange(0,n))
            
        self.h = H(self.queen,n)
        self.n = n

    def getNextState(self):
        minH = self.h
        coord = []

        # find min H
        # 같은 H값을 갖는게 여러개이면 제일 처음에 나온 좌표 선택
        for i in range(0,self.n):
            for j in range(0,self.n):
                if self.queen[i]==j: continue
                tmp = self.queen.copy()
                tmp[i] = j
                newH = H(tmp, self.n)

                if newH < minH :
                    minH = newH
                    coord = [i,j]

        if minH < self.h:
            self.queen[coord[0]] = coord[1]
            self.h = minH
        else:
            self.h = -1

    def toString(self):
        goal = ""
        for i in range(0, self.n):
            goal = goal + str(self.queen[i]+1) + " "
        return goal   

def hc(n):
    if n==0 : return "no solution"
    state = State(n)

    while state.h > 0:
        state.getNextState()

    if state.h == 0:
        return state.toString()
    elif state.h == -1:
        return "no solution"
