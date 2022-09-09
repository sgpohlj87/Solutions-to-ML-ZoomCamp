# working with functions

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an arguement
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguements
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# working with condtional statemens

def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print (st)

    # conditional statements let you use "a if c else b"
    st = "x is less than y" if (x<y) else "x is greater than or the same as "

# working with loops

def main():
    x = 0

    # define a while loop
    # while (x<5):
    #   print(x)
    #   x = x+1

    # define a for loop
    for x in range(5, 10):
        print(x)

    # use a for loop over a collection
    




if __name__ == "__main__":
    main()