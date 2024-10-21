# name = input("input name: ")
# if name == "gg":
#     print("Hi admin")
# if name == "ff":
#         print("hi prepod")
# else:
#     print("Hi ", name)

#or - and
number = int(input("Input numb: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBazz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("no match")
