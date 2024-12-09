# 命名规则
# 可以是字符(中文,英文),下划线“_”和数字，而且第一个字符不能是数字
# 不能使用python中的保留字
# 标识符严格区分大小写
# 以下划线开头的标识符有特殊的意义，一般避免使用相似的标识符
# 允许使用中文作为标识符但不建议

# 命名规范
# 模块名尽量短小，并且全部使用小写字母，可以使用下划线分割多个字母 例如：grame_main
# 包名尽量短小，并且全部使用小写字母，不推荐使用下划线 例如：com.python,不推荐com_python
# 类名采用首字母大写的风格(pascal风格)。例如：MyClass
# 模块内部的类采用'_'+pascal风格的类名组成，例如：在MyClass中的内部类_lnnerMyClass
# 函数,类的属性和方式的命名，全部使用小写字母，多个字母之间使用下划线分割
# 常量的命名采用全部大写字母，可以使用下划线
# 使用单下划线'_'开头的模块变量或函数是手保护的，在使用"from xxx import*"语句从模块导入时，这些模块变量或函数不能被导入
# 使用双下划线'__'开头的实例变量或方法是类私有的
# 以双下划线开头和结尾的是python的专用标识，例如：__init__()表示初始化函数