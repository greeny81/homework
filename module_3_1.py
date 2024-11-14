calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(inputstr_):
    count_calls()
    ret = (len(inputstr_), inputstr_.upper(), inputstr_.lower())
    return ret

def is_contains(str_, str_list_):
    count_calls()
    lowercase_str = str_.lower()
    lowercase_list = [s.lower() for s in str_list_]
    #print(lowercase_list)
    if lowercase_str in lowercase_list:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)