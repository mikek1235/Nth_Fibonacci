# Michael Karkuszewski
# Fibonacci sequence
# Homework 2

# Gets user input for wich fibonacci number they want.
n = int(input('Input which fibonacci number you want: '))
# Initializes the fibonacci number list with values 0 and 1.
fibs = [0,1]

# Nth fibonacci number function
def fib(n):
    #Loops through the range of the fibonacci number provided and appends fibonacci numbers to it
    for I in range (2,n+1):
       # Calculates and appends fibonnaci numbers
       fibs.append(fibs[I-1]+fibs[I-2])
    return fibs [n]

result = fib (n+1)
print ('The ' + str(n) + 'th fibonacci number is: ' + str(result))
