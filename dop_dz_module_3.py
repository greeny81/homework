# wer = {'cube': 7, 'drum': 8} # dict
# print(type(wer))
# exit()

data_structure = [[1, 2, 3], # 6
                  {'a': 4, 'b': 5}, # 17
                  (6, {'cube': 7, 'drum': 8}), # 23 , 34, 46
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

summ = 0

def calculate_structure_sum(obj_):
    global summ
    i = 0
    print(f'!Inputobj_: {str(obj_)}')

    #while i <  len(obj_):
    if len(obj_):
        #print(obj_[i], type(obj_[i]))
        if isinstance(obj_[i], list) :
            #print(obj_[i])
            summ += sum(obj_[i])
            del(obj_[i])
            print(f'Summ list: {summ}')

        if isinstance(obj_[i], dict):

            for key in obj_[i]:
                print(f'Input dict {str(obj_[i])}')
                summ += len(key) + obj_[i][key]
                print(f'+dict:{summ}')
            del(obj_[i])

        if isinstance(obj_[i], str):
            print(f'STR: {obj_[i]}')
            summ += len(obj_[i])
            print(f'\nstr:{summ}')
            del(obj_[i])

        if isinstance(obj_[i], tuple):
            tmpLIst = list(obj_[i])
            print(f'TuptoList: {tmpLIst}')
            j = 0
            while j < len(tmpLIst):
                print(f'Tuple {j} {tmpLIst[j]} |{tmpLIst} {type(tmpLIst[j])}|')
                if isinstance(tmpLIst[j], int):
                    summ += tmpLIst[j]
                    del(tmpLIst[j])

                j += 1
            obj_[i] = tuple(tmpLIst)
            if len(obj_[i]):
                calculate_structure_sum(obj_)

        #i += 1
    return summ

result = (calculate_structure_sum(data_structure))
print(result)
print(f'SUMM: {summ}')