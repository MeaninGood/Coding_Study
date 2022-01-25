import sys

n = int(sys.stdin.readline())



def recur(n, s, e, v) :
        
    if n == 0 : 
    	return
 
    print(str(s) + " " + str(e))
    recur(n-1, v, e, s)
    
recur(n, 1, 3, 2)