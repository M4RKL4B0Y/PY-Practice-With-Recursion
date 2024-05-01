# Write code for algorithm 1 below

def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)
