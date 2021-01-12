P = int(input())
N = int(input())
R = int(input())

sum = N
day = 0

while sum <= P:
    N *= R
    sum += N
    day += 1
    # print(sum)

print(day)
