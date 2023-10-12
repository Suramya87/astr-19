#Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

#function f(x)
def f(x):
    #calculation and return values
    return x**3 + 8

#main function
if __name__ == "__main__":
    #declaration of x
    x = 9 
    #declaration of y
    y = f(x)
    #contional 
    if y > 27: 
        #output
        print(y)
        print("YAY!")