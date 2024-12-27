#- Написать функцию которая возвр функцию повторения 2х первых символов n раз
#- создать массив функций и применить поочередно к аргументу
#- применить все функции поочередно к массиву аргументов
animal = 'мишка'
animals= ['зайка', 'мишка', 'бегемотик']

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat

test1 = gen_repeat(1)
test2 = gen_repeat(2)
print(test1(animal))
print(test2(animal))

#-2
repetit = [gen_repeat(n) for n in range(1, 4)]
print(repetit)
result = [func(animal) for func in repetit]
print(result)
#-3
fin_result = [func(x) for func in repetit for x in animals]
print(fin_result)
fin_result = [func(x) for x in animals for func in repetit]
print(fin_result)
