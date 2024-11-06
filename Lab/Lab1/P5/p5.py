num = int(input())

if num == 0:
    print("empty")

else:
    list_string = input()

    max_list = []

    list_string = list_string.split(" ")

    for c in list_string:
        max_list.append(int(c))

    print(max(max_list))
