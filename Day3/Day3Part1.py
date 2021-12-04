def compare(a):
    zeros, ones = 0,0
    for i in a:
        if i == '1':
            ones += 1
            
        else:
            zeros += 1
    if ones > zeros:
        return 1
    else:
        return 0
def compareyourmom(a):
    l = ""
    for i in a:
        if i == "1":
            l += "0"
        else:
            l += "1"
    return l

f = open("input.txt","r")
file = f.read().split("\n")


values = 0
mode = []
binary = ''
for l in range(len(file[0])):
    for line in file:
        temp = line[values]
        mode.append(temp)
    binary += str(compare(mode))
    mode = []
    values += 1
gamma = int(binary,2)
epsilon = int(compareyourmom(binary),2)
print(epsilon * gamma)
f.close()
#every time the for loop loops over the entire file, add one to values
#0th index in median. Find the median. Reset the list