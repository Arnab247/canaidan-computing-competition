rows = int(input())
columns = int(input())

valid = False
found = False
nextstep = False

data = []

for i in range(rows):
    row = str(input())
    row = row.split(" ")
    for n in range(len(row)):
        row[n] = int(row[n])
    data.append(row)


start = [rows, columns]
goal = data[0][0]

explored = [[rows, columns]]
exploring = [start]

# print(exploring)

count = 0
max = 0

went = False

length = len(exploring)

# print(exploring)

row = rows
column = columns
# print(length)

expanding = True

while True:
    # print('hi')
    while expanding:
        for n in range(length):
            # print("hi")
            for digit1 in range(rows):
                for digit2 in range(columns):
                    # print(data[digit1][digit2])
                    # print(exploring[n][0] * exploring[n][1])
                    if data[digit1][digit2] == (exploring[n][0] * exploring[n][1]):
                        # print("data: " + str(data[digit1][digit2]))
                        if data[digit1][digit2] == goal:
                            print('yes')
                            exit()
                        # print(explored)
                        # print(exploring)

                        # for testn in range(len(explored)):
                        #     if explored[testn]==([digit1 + 1][digit2 + 1]):
                        #         # print('wow')
                        #         exploring.pop(n)
                        # if exploring == []:
                        #     print('no')
                        #     exit()
                        # print("hi")
                        later1 =digit1+1
                        later2 = digit2+1
                        # explored.append([digit1+1, digit2+1])
                        if count != 0:
                            # print('visited count')
                            exploring.append([digit1+1, digit2+1])
                        else:
                            # print('visited')
                            exploring.append([digit1+1, digit2+1])
                            # exploring[n][0] = digit1 + 1
                            # exploring[n][1] = digit2 + 1
                        count += 1
                        
                        # print("hif")
                        ex1 = exploring[n][0]
                        ex2 = exploring[n][1]

                        # print(count)

                        if len(explored) > count:
                            for value in range(len(explored) - count):
                                if explored[value] == [(exploring[n][0]),(exploring[n][1])]:
                                    print('wow')
                                    exploring.pop(n)
                        if exploring == []:
                            print('no')
                            exit()
                        # print(exploring)
                        # print(explored)
                        went = True
                if went:
                    explored.append([later1, later2])
                    went = False
            for a in range(count):
                exploring.pop(0)
            # print(exploring)
            # print('popped')
            count = 0

        max += len(exploring)
        if max > columns*rows*5:
            print('no')
            exit()
        # print(len(exploring))
        length = len(exploring)
        # print('next')