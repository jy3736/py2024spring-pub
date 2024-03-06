def check_divisible_by_four(number):
    if number % 4 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    number = int(input())
    check_divisible_by_four(number)
    