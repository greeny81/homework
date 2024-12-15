class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, num):
        if self.__is_valid_vin(vin):
            self.__vin = vin
        self.__numbers = num
        self.model = model

    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999:
            return True
        else:
            pass

try:
  first = Car('Model1', 10000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')