def draw_area():
    for i in area:
        print(*i)

area = [["*","*","*"], ["*","*","*"], ["*","*","*"]]

for turn in range(1, 10):
    print(f'Xod {turn}')
    if turn % 2 == 0:
        turn_char = "0"
    else:
        turn_char = "X"
    row = int(input("Numb stroki 1,2,3")) - 1
    column = int(input("Numb stolb 1,2,3")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print ("Propusk hoda")
        draw_area()
        continue
    draw_area()
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        print ("Krestiki WIN")
        break

