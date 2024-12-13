from random import randint


def say_hi():
    from random import randint
    print("Hi Я из функции во 2м модуле")
    print(randint(10, 20))

#randint # ERR т.к. импорт внутри функции

def main():
    a = 5
    b = 10
    print("я moduls1")


if __name__ == '__main__':
    main()