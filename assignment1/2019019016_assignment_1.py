import bfs
import hc
import csp

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
            goal = bfs.bfs(N)
        elif algorithm == "hc":
            goal = hc.hc(N)
        elif algorithm == "csp":
            goal = csp.csp(N)

        print(goal)

        # write output file 
        fName = str(N) + "_" + algorithm + "_output.txt"
        fOutput = open(fName,'w')
        fOutput.write(goal)
        fOutput.close()
        
    fInput.close()

if __name__ == "__main__":
    main()
        
            
