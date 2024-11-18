# import this
#





exit()
matrix = []
matrix.append([])

while True:
    number = int(input("Input numb: "))
    if number == 0:
        break
    if number % 2  == 0:
        print("num:",number,"четное")
    else:
        print("num:", number,"нечетное")
print("End")
