# 进制类型    引导符号     例子
# 十进制      无          250
# 二进制      0b或0B      0b10101,0B10101
# 八进制      0o或0O      0o763,0O765
# 十六进制    0x或0X        0x798A,0X798A

# # 整数类型
# num=250
# print(num)
# num=0b1010
# print(num)
# num=0o757
# print(num)
# num=0x456
# print(num)

# # 浮点数类型
# high=170.3
# print(high,type(high))
# x=10
# y=10.0
# print(type(x))# int
# print(type(y))# float
# x=1.99E1413
# print('科学计数法:',x,type(x))
# print(0.1+0.2)# 不确定的尾数问题0.30000000000000004
# print(round(0.1+0.2,1))# ,1 表示的是保留以为小数

# 复数类型的使用
# python中的复数与数学中的复数类型完全一致,由实部和虚部组成
# python中实部用.real表示,虚部用.imag表示
x=132+324j
print(x.real,x.imag)