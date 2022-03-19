def E(string):

    global index

    if (string[index]=='a'):
        index+=1
        E_(string)
    
    else:
        print("Error")

def E_(string):

    global index

    if(string[index] == 'b'):
        index+=1
        E_(string)

    elif(string[index] == 'a'):
        index+=1
    
    else:
        print("Error")


string = input()
index = 0

# Parsing start
E(string)

# For termination of string
if(string[index] == "$"):
    print("Successful parsing!")

