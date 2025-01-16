
class defClass():
    def __init__(self, num):
        self.att_1 = num
        self.att_2 = 'ggwp'

    def def_method(self, value):
        self.att_1 = value


def introspection_info(obj):
    cur_ret = [type(obj), dir(obj), callable(obj)]
    return cur_ret

obj = defClass(345)
str = 'first time str'

ret = introspection_info(str)
print(ret)
ret1 = introspection_info(obj)
print(ret1)