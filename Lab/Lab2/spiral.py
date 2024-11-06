num_pos = int(input())
value_list = []

for _ in range(num_pos):
    position = input()
    position_temp = position.split(" ")
    position_list = list(map(int, position_temp))
    value_list.append(position_list)

for index in range(num_pos):
    y = value_list[index][0]
    x = value_list[index][1]
    if y > x:
        if y % 2 > 0:
            value_list[index] = (y-1)**2 + x
        else:
            value_list[index] = y ** 2 - x + 1
    elif x >= y:
        if x % 2 > 0:
            value_list[index] = x**2 - y + 1
        else:
            value_list[index] = (x-1)**2 + y

for value in value_list:
    print(value)
