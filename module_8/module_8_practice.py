def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Result: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Result: {operand_1 - operand_2}')
    if operation == '/':
        print(f'Result: {operand_1 / operand_2}')
    if operation == '//':
        print(f'Result: {operand_1 // operand_2}')
    if operation == '%':
        print(f'Result: {operand_1 % operand_2}')
    if operation == '*':
        print(f'Result: {operand_1 * operand_2}')



    #print(operand_1, operation, operand_2)
cnt = 0
with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as err:
            if 'unpack' in err.args[0]:
                print(f'Error in {cnt} not enough data |{line}|')
            else:
                print(f'Err sym to int |{line}|')
