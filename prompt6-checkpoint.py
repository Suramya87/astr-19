#imports
import math
#pi
pi = math.pi


#functions
#x and sin(x) 1000 entires
def generate_table1():
    print("x             | sin(x)")
    print("------------------------")
    for i in range(0,1001):
        x = i/159.154943092
        sin_x = math.sin(x)
        print(f"{x:.9f}   | {sin_x:.9f}")
#sin(x) adn cos(x) 1000 entires
def generate_table2():
    print("sin(X)        | cos(x)")
    print("------------------------")
    for i in range(0,1001):
        x = i/159.154943092
        sin_x = math.sin(x)
        cos_x = math.cos(x)
        print(f"{sin_x:.9f}   | {cos_x:.9f}")
#x, sin(x) and cos(x) 1000 entires
def generate_table3():
    print("x             | sin(X)        | cos(x)")
    print("---------------------------------------------")
    for i in range(0,1001):
        x = i/159.154943092
        sin_x = math.sin(x)
        cos_x = math.cos(x)
        print(f"{x:.9f}   | {sin_x:.9f}   | {cos_x:.9f}")
#x, sin(x) and cos(x) 10 entires
def generate_table4():
    print("x             | sin(X)        | cos(x)")
    print("---------------------------------------------")
    for i in range(0,11):
        x = i/1.59154943092
        sin_x = math.sin(x)
        cos_x = math.cos(x)
        print(f"{x:.9f}   | {sin_x:.9f}   | {cos_x:.9f}")
#main
def main():
    generate_table1()
    generate_table2()
    generate_table3()
    generate_table4()
if __name__ == "__main__":
    main()
    
