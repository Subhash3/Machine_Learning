squares = open("squares.csv", 'w')

for i in range(100) :
    squares.write(str(i) + ", " + str(i**2) + "\n")

