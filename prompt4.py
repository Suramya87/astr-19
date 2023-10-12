#Animal class
class being:
    # length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool).
    name = "" # name of the being
    length_of_arm = 0.0 # length of the arms (float)
    length_of_legs = 0.0 # length of the legs (float)
    number_of_eyes = 0 # number of eyes (int)
    tail = False # tail (boolean)
    furry = False # furry (boolean)

if __name__ == '__main__':
    #introduction
    print("greetings mortal, you are required to provide the physical parameters of a being of your liking. Please")
    #gathering the physical parameters(float)
    try:
        being.length_of_arm = float(input("Please enter the lenght of your being's arm in cm: "))
    except ValueError:
        print("Please enter the length of your being's arm in numbers")
    
    try:
        being.length_of_legs = float(input("Please enter the lenght of your being's leg in cm: "))
    except ValueError:
        print("Please enter the length of your being's leg in numbers")

    #gathering the physical parameters(int)
    try:
        being.number_of_eyes = int(input("Please enter the number of eyes your being has: "))
    except ValueError:
        print("Please enter the number of eyes your being has")

    #Gathering the physical parameters (boolean)
    tail = input("does it have a tail? y/n ") 
    fur = input("does it have a fur? y/n ")
    if tail == "y":
        being.tail = True
        tail_info = "does"
    
    if fur == "y":
        being.furry = True
        furry_info = "does"

    #in case of false 
    else:
        tail_info = "does not"
        furry_info = "does not"
    #name cause why not
    being.name = input("What is its name? ")
    #Final output
    print(f"The being of your liking is {being.name} its arms are {being.length_of_arm} cm long and its legs are {being.length_of_legs} cm long. It has {being.number_of_eyes} eyes. It {tail_info} have a tail and it {furry_info} have fur. ")