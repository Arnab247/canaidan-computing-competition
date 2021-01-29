rows = int(input())
columns = int(input())

valid = False
nextstep = False

data = []

for i in range(rows):
    row = str(input())
    row = row.split(" ")
    for n in range(len(row)):
        row[n] = int(row[n])
    data.append(row)


final = rows * columns

row = rows
column = columns

# For all of the exploring positions find the next values
# Find other points in graph which have the multiplied number and return all of the answers
# For more numbers, import to new list
def explore(options):
    global rows
    global columns
    global data
    new = []
    more = []
    for n in range(len(options)):
        count = 0
        for r in range(rows):
            for c in range(columns):
                # print(data[r][c])
                if data[r][c] == (options[n][0] * options[n][1]):
                    # print('hi')
                    if count == 0:
                        new.append([r+1, c+1])
                    else:
                        more.append([r+1, c+1])
                    count += 1
    
    return new, more

# Define goal
goal = data[0][0]

# Define start position
start = [rows, columns]

# Define exploring
exploring = [[rows, columns]]

# Define explored
explored = [data[rows-1][columns-1]]

# init loop
while True:
    # Explore New Positions
    results = explore(exploring)

    # Check if destination reached
    for n in range(len(exploring)):
        if (exploring[n][0] == 1):
            if exploring[n][1] == 1:
                print('yes')
                exit()

    # Check if the number is visited
    # If visited, remove what is found, and if it was part of the original range remove that point, if not, just remove
    if (len(results[0])) > 0:
        for n in range(len(results[0])):
            if (results[0][n][0]) * (results[0][n][1]) == goal:
                    print('yes')
                    exit()
            if (results[0][n][0] * results[0][n][1]) in explored:
                exploring[n] = []
            else:
                exploring[n] = results[0][n]
                if data[results[0][n][0]-1][results[0][n][1]-1] not in explored:
                    explored.append(data[results[0][n][0]-1][results[0][n][1]-1])

    # remove empty values from exploring list
    for n in reversed(range(len(exploring))):
        if exploring[n] == []:
            exploring.remove(exploring[n])

    # If new exploring values were not found, return false
    if (len(results[0]) + len(results[1])) == 0:
        print('no')
        exit()

    # Update Exploring Values to new positions
    if len(results[1]) > 0:
        for n in range(len(results[1])):
            if (results[1][n][0] * results[1][n][1]) == goal:
                print('yes')
                exit()
            if (results[1][n][0] * results[1][n][1]) in explored:
                continue
            else:
                if results[1][n] not in exploring:
                    exploring.append(results[1][n])
                if data[results[1][n][0]-1][results[1][n][1]-1] not in explored:
                    explored.append(data[results[1][n][0]-1][results[1][n][1]-1])

    # If the exploring list is empty, then return false
    if exploring == []:
        print('no')
        exit()
