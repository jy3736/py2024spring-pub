
def find_closest_distance(a, b, c):
    distance_to_b = abs(a - b)
    distance_to_c = abs(a - c)
    closest_distance = min(distance_to_b, distance_to_c)
    print(closest_distance)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    find_closest_distance(a, b, c)


