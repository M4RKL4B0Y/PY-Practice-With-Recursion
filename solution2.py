# Write code for algorithm 2 below
def natural_numbers(x,i=0):  # Added a default value of 0 for the parameter i
    if x == 0:
        return  
    else:
        natural_numbers(x-1,i+1)
        print(i)

natural_numbers(10)  # Calling the function with one argument