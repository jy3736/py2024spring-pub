def determine_square_color(column, row):
    if (column + row) % 2 == 0:
        print("BLACK")))
    else:
        print("WHITE")

if __name__ == "__main__":
    column = int(input())
    row = int(input())
    determine_square_color(column, row)
    