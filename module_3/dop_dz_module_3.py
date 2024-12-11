# wer = {'cube': 7, 'drum': 8} # dict
# print(type(wer))
# exit()

data_structure = [[1, 2, 3], # 6
                  {'a': 4, 'b': 5}, # 17
                  (6, {'cube': 7, 'drum': 8}), # 23 , 34, 46
                  "Hello", # 51
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

summ = 0

def calculate_structure_sum(obj_):
    global summ
    i = 0
    print(f'\n!!!!! Input-obj_: {str(obj_)} {type(obj_)}')

    if len(obj_):

        if isinstance(obj_[i], list) :
            print(f'Input List block {str(obj_[i])}')
            summ += sum(obj_[i])
            del(obj_[i])
            print(f'Summ list: {summ}')
            print(f'Out LIST {str(obj_)}')
            calculate_structure_sum(obj_)

        if isinstance(obj_[i], dict):
            print(f'Input dict block {str(obj_[i])}')

            for key in obj_[i]:

                summ += len(key) + obj_[i][key]
                print(f'Summ+dict:{summ}')
            print(f'After dict {str(obj_[i])} Summ: {summ}')
            del(obj_[i])
            print(f'Out DICT {str(obj_)}')
            calculate_structure_sum(obj_)

        if isinstance(obj_[i], str):
            print(f'Input STR block: {obj_[i]}')
            summ += len(obj_[i])
            print(f'\nstr:{summ}')
            del(obj_[i])
            print(f'Out STR {str(obj_)}')
            calculate_structure_sum(obj_)

        if isinstance(obj_[i], tuple):
            tmpLIst = list(obj_[i])
            print(f'Input Tuple block: {tmpLIst}')
            j = 0
            while j < len(tmpLIst):
                print(f'Tuple obj_{j}={tmpLIst[j]} | <--- {tmpLIst} {type(tmpLIst[j])} {len(tmpLIst[j])} |')
                if isinstance(tmpLIst[j], int):
                    summ += tmpLIst[j]
                    del(tmpLIst[j])
                if isinstance(tmpLIst[j], tuple):
                    for key, val in tmpLIst[j].items():
                        if isinstance(key, str):
                            summ += len(key)




                print('Tuple after DEL:' + str(tmpLIst))
                j += 1
                obj_[i] = tuple(tmpLIst)
                print(f'Summ tuple: {summ}')

            if len(obj_[i]):
                print('NOW obj_[i]: ' + str(obj_[i]))
                print('NOW obj_: ' + str(obj_))
            #else:
                calculate_structure_sum(obj_)

        #i += 1
    return summ

result = (calculate_structure_sum(data_structure))
print(result)
print(f'SUMM: {summ}')