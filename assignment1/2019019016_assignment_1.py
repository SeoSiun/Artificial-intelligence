from bfs import bfs  
from hc import hc
from csp import csp

def main():
    fInput = open("input.txt")

    while True:
        input = fInput.readline()
        if not input: break

        N = int(input.split(' ')[0])
        algorithm = input.split(' ')[1].rstrip('\n')

        goal = ""

        # find goal
        if algorithm == "bfs":
            goal = bfs(N)
        elif algorithm == "hc":
            goal = hc(N)
        elif algorithm == "csp":
            goal = csp(N)

        print(goal)

        # write output file 
        fName = str(N) + "_" + algorithm + "_output.txt"
        fOutput = open(fName,'w')
        fOutput.write(goal)
        fOutput.close()
        
    fInput.close()

if __name__ == "__main__":
    main()