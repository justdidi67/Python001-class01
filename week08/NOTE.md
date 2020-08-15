学习笔记

可变序列：
list，bytearray，array.array，collections.deque和memoryview(内存视图)
不可变序列：
tuple，str和bytes

容器序列：
list，tuple和collections.deque这些序列可以存放不同类型的数据
扁平序列：
str，bytes，bytearray，memoryview和array.array，这些序列只能容纳一种类型


函数
函数在Python是第一类对象
第一类对象的特性：
----1.可以被引用
----2.可以当做参数传入
----3.可以当做函数返回值
----4.可以当做容器类型的元素
函数名加括号是调用函数，不加括号是在操作函数，指向内存地址

1，变量作用域：决定了在哪一部分程序可以访问哪个特定的变量名称
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找

2,lambda表达式
冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象
lambda [arg1[,arg2,arg3....argN]]:expression

3，偏函数
functools.partial()
将所要承载的函数作为partial()函数的第一个参数,partial 的第二个参数是原函数的第一个参数


高级函数
常见的高阶函数：map、reduce、filter、apply


装饰器
1、装饰器语法糖
python提供了@符号作为装饰器的语法糖，使用语法糖要求装饰函数必须return一个函数对象。因此我们将上面的func函数使用内嵌函数包裹并return

2、对带参数的函数进行装饰
@decorate
def bar():
    print('i am bar:%s'%(a+b))
bar(1,2)    
等价于：  decorate(target)(1,2)

3,函数参数数量不确定
装饰器内使用变长参数*args和**kwargs

4，装饰器带参数
装饰器带上参数

5，functools.wraps
如果想要保留原函数的属性，就可以用到functools.wraps

