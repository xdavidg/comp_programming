num = int(input().strip())

list_size = int(input().strip())

boolean_list = []

temp_string = input()

bool_string = temp_string.split(" ")

for c in bool_string:
    boolean_list.append(int(c))

return_value = "OUTPUT -1"

for index in range(len(boolean_list) - 1):
    if boolean_list[index] == 1:
        if boolean_list[index + 1] == 0:
            return_value = f"OUTPUT {index}"
            break

print(return_value)
