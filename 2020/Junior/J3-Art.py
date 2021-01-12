paintDrops = int(input())

bottomleft = [100, 100]
topright = [0, 0]

for i in range(paintDrops + 1):
    if i != 0:
        cordinate = str(input())
        cordinate = cordinate.split(",")
        cordinate1 = int(cordinate[0])
        cordinate2 = int(cordinate[1])
        if cordinate1 <= bottomleft[0]:
            bottomleft[0] = cordinate1 - 1
        if cordinate2 <= bottomleft[1]:
            bottomleft[1] = cordinate2 - 1
        if cordinate1 >= topright[0]:
            topright[0] = cordinate1 + 1
        if cordinate2 >= topright[1]:
            topright[1] = cordinate2 + 1

print(str(bottomleft[0]) + "," + str(bottomleft[1]))
print(str(topright[0]) + "," + str(topright[1]))
