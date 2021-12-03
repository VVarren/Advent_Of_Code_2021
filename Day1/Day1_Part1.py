
O = open("numberset.txt","r")
x = O.read()
y = x.split("\n")
O.close()



def final():
    counter = 0
    for depthI in range(len(y)):
        if depthI > 0:
            temp = y[depthI]
            temp1 = y[depthI- 1]
            if int(temp) > int(temp1):
                counter += 1
    print(f"The amount of times it printed is: {counter}")

final()