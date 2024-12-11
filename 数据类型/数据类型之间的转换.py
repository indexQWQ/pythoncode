# int()将x转换为整数类型
# float()将x转换为浮点数类型
# str()将x转成字符串
# chr()将整数 x转换为一个字符
# ord()将一个字符x转换为其对应的整数值
# hex()将一个整数 x转换为一个十六进制字符串
# oct()将一个整数 x转换为一个八进制字符串
# bin()将一个整数 x转换为一个二进制字符串

x=10
y=3
z=x/y# 隐式类型转换
print('%.2f'% z,type(z))
# 将float类型转int类型
print('float类型转int:',int(3.13))
print('float类型转int:',int(3.8))
print('float类型转int:',int(-3.13))
print('float类型转int:',int(-3.8))
# 将int类型转float类型
print(float(9))
# 将str转int
print(int('100')+int('2000'))
