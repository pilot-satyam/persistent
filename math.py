#addition
def add(x,y):
    return x+y
#subtraction
def sub(x,y):
    return x-y #on master branch
#multiplication
def mul(x,y):
    return x*y #on bug456
#division
def div(x,y):
    if y==0:       #on master branch
        return divide_by_0_error
    else:
        return x/y
def square(x):
    return x*x
#Just to check the working of the directory using github
def tri(x):
    return x*x*x

#For checking branch bug123
def quad(x):
    x*x*x*x