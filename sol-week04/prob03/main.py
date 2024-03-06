def check_one_even(num1, num2):
    if (num1 % 2 == 0) ^ (num2 % 2 == 0):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    check_one_even(num1, num2)
    