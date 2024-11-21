#import moduls1 as m2 #
#from moduls1 import * #Глобальное обьявление
from moduls1 import say_hi as sh #Глобальное обьявление
#print(dir(m2))
import sys
import math
import tkinter

#print("Привет я из модуля moduls")
#print(m2.a)
#m2.say_hi()
#say_hi()

sh()
for path in sys.path:
    print(path)

