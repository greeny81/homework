import inspect


class defClass():
    def __init__(self, num):
        self.att_1 = num
        self.att_2 = 'ggwp'

    def def_method(self, value):
        self.att_1 = value


def introspection_info(obj, attrib=''):
    try:
        cur_attr = getattr(obj, attrib)
    except:
        cur_attr = 'no this attr'

    cur_ret = [type(obj), callable(obj), cur_attr, inspect.isclass(obj), isinstance(obj, defClass), dir(obj)]
    return cur_ret

obj = defClass(345)
str = 'first time str'

ret = introspection_info(str)
print(ret)
ret1 = introspection_info(obj, attrib='att_1')
print(ret1)