# Write code for algorithm 1 below

def count_down(n):

    # base case
    if n == 0:
        return
    
    # recursive case
    else:
        print(n)
        count_down(n-1)

    #test case
    n=5
    count_down(n)
