text = str(input())
cyclic = str(input())
valid = False

for i in range(len(cyclic)):
    if cyclic in text:
        valid = True
        break
    cyclic = cyclic[-1] + cyclic
    cyclic = cyclic[:-1]

if valid == True:
    print("yes")
else:
    print("no")
