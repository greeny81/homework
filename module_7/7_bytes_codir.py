#ASCII 128 символов
f = 'hello'
print(ord('+'))# В числовое значение unicode
chars = []

for i in f:
    chars.append(ord(i))#[104, 101, 108, 108, 111]
s = ''
#print(chars)

for i in chars:
    s += chr(i)#[104, 101, 108, 108, 111]  ==>> hello
print(s)

# for i in range(1000, 1200):#UNICODE + 2 миллиона символов
#     print(chr(i))
#bytes
print(hex(ord('h')))# h ==>> 104 ==> 0x68
bb = b'\x68' #  0x68 ==> b'\x68'
#print(type(bb))#<class 'bytes'>
print(bb.decode())# hex to sym b'\x68' ==> h



