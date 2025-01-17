import inspect


class defClass():
    def __init__(self, num):
        self.att_1 = num
        self.att_2 = 'ggwp'

    def def_method(self, value):
        self.att_1 = value


def introspection_info(obj):
    try:
        attr = getattr(obj, 'att_1')
    except:
        attr = 'no this attr'
    cur_ret = [type(obj), callable(obj), attr, inspect.isclass(obj), isinstance(obj, defClass), dir(obj)]
    return cur_ret

obj = defClass(345)
str = 'first time str'

ret = introspection_info(str)
print(ret)
ret1 = introspection_info(obj)
print(ret1)