#nested pattern
size = int(input("Enter the size of the pattern: "))
row = 1
symbols =["*", "*", "*", "*", "*"]
while row <= size:
    for col in range(size):
        if col == row - 1:
            print(symbols[row], end="")
        else:
            print(symbols[1], end="")
    print()
    row += 1
