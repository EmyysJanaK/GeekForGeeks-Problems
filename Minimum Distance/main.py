def minimum_distance(x1, x2, x3):
    x = sorted([x1, x2, x3])[1]
    
    # Sum of dists
    distance = abs(x1 - x) + abs(x2 - x) + abs(x3 - x)
    
    return distance

x1 = 3
x2 = 2
x3 = 10

print(minimum_distance(x1, x2, x3))  # 6