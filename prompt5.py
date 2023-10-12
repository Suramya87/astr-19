#imports
import math
#pi
pi = math.pi

#functions
def generate_table():
    print("x       | sin(x)")
    print("------------------")
    for i in range(0,1001):
        x = i/159.154943092
        sin_x = math.sin(x)
        print(f"{x:.3f}   | {sin_x:.3f}")
#main
def main():
    generate_table()

if __name__ == "__main__":
    main()
    print(math.sin(2*math.pi))
