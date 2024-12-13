my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
cnt = -1
while cnt < len(my_list):
    cnt += 1
    if my_list[cnt] > 0:
        print(my_list[cnt])
        continue
    elif my_list[cnt] == 0:
        continue
    elif my_list[cnt] < 0:
        break

