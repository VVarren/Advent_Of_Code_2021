x,y = 0,0
aim = 0
f = open("input.txt","r")
for line in f:
    line = line.strip()
    long = len(line) - 1
    if "down" in line:
        y += int(line[long])
    elif "up" in line:
        y -= int(line[long])
    else:
        x += int(line[long])
    print(x*y)
f.close()

