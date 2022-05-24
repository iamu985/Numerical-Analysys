
from time import sleep
import os
from tabulate import tabulate

def calculate_h(xn, x, n):
    return (xn-x)/n

def clrscr():
    return os.system('clear')

def create_table(data):
    print(tabulate(data, headers="keys"))


def eulers_method(xn, x, y, n, h, function, i=0, data={'n':[], 'x':[], 'y':[]}):
    data['n'].append(i)
    data['x'].append(x)
    data['y'].append(y)
    i += 1
    if i > n:
        return data
    else:

        # getting value from the function 
        fvalue = function(x, y)

        # calculate the value of y
        y = y + (h * fvalue) 

        # calculate x
        x = data['x'][0] + (i * h)
        
        # recurse
        print(f"Preparing data: [{round((i/n)*100, 2)}%]")
        sleep(0.05)
        clrscr()

        return eulers_method(xn, x, y, n, h, function, i, data)


def expr_func(x, y):
    return x**2+y

if __name__ == "__main__":
    xn = float(input("Xn: "))
    x0 = float(input("X0: "))
    y0 = float(input("x1: "))
    n = int(input("N: "))
    h = calculate_h(xn, x0, n)

    result = eulers_method(xn, x0, y0, n, h, expr_func)
    usr = input("Do you want to print the table?")
    if usr == 'y':
        create_table(result)
    if usr == 'n':    
        print(f"The result is {result['y'][-1]}")



