#User function Template for python3



#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    # code here
    q = []
    q.append("1")
    result = []
    
    while N > 0 : 
        string = q.pop(0)
        result.append(string)
        q.append(string + "0")
        q.append(string + "1")
        N-=1
    return result