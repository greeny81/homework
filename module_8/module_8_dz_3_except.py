class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, num):
        if self.__is_valid_vin(vin):
            print(self.__is_valid_vin(vin))
            self.__vin = vin
        self.__numbers = num
        self.model = model

    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

try:
  first = Car('Model1', 1000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')