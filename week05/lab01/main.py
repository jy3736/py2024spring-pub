def check_last_digit(number):
    if number % 10 == 7:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    number = int(input())
    check_last_digit(number)
    