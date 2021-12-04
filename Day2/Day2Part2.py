x,y = 0,0
aim = 0
f = open("input.txt","r")
for line in f:
    line = line.strip()
    long = len(line) - 1
    if "down" in line:
        aim += int(line[long])
    elif "up" in line:
        aim -= int(line[long])
    else:
        x += int(line[long])
        y += aim * int(line[long])
    print(x,y)
    print(x*y)
f.close()

