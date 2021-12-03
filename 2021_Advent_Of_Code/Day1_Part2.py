
O = open("numberset.txt","r")
x = O.read()
y = x.split("\n")
O.close()

new = []

def final():
    counter = 0
    for depthI in range(len(new)):
        if depthI > 0:

            temp = new[depthI]
            temp1 = new[depthI- 1]
            if int(temp) > int(temp1):
                counter += 1
    print("The amount of times it printed is: " + counter)

def adder():
    for i in range(0,len(y), 1):
        if i >= 1998:
            final()
        else:
            letter1 = y[i]
            letter2 = y[i+1]
            letter3 = y[i+2]
            total = int(letter1) + int(letter2) + int(letter3)
            new.append(total)

adder()

