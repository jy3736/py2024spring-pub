def sort_three_numbers(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b <= a and b <= c:
        if a <= c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:  # c is the smallest
        if a <= b:
            print(c, a, b)
        else:
            #print(c, c, c)
            print(c, b, a)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    sort_three_numbers(a, b, c)
    