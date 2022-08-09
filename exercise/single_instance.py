


'''
1.模块方式
'''
class SingleInstance:
    def __init__(self) -> None:
        pass

single_instance = SingleInstance()

class DBOperator:

    def __init__(self) -> None:
        #connect to db
        pass
db_operator = DBOperator()


# 使用方式
# from single_instance import single_instance

'''
2.new
'''
class SingleInstance1(object):
    
    def __init__(self,name) -> None:
        print("___init____")
        self.name = name
    
    def print_name(self):
        print(self.name)

    def __new__(cls,*args,**kw) :
        print( "__new__" )
        if not hasattr(SingleInstance1, "_instance" ):
            print( " 创建新实例 " )
            SingleInstance1._instance = object.__new__(cls)
        return SingleInstance1._instance


# s1 = SingleInstance1("aaaa")
# s2 = SingleInstance1("bbbb")
# s3 = SingleInstance1("ssss")
# s1.print_name()
# s2.print_name()
# print(id(s1),"=====",id(s2))


'''
3.使用类的方式实现
'''
class SingleInstance2:
    
    @classmethod
    def get_instance(cls,*arg,**kw):
        if not hasattr(SingleInstance2,'_instance'):
            SingleInstance2._instance = SingleInstance2()
        return SingleInstance2._instance

s1 = SingleInstance2.get_instance()
s2 = SingleInstance2.get_instance()
print(id(s1),"=====",id(s2))

'''
4.函数装饰器
'''
_instance = {}
def singleton(cls):
    def _single(*args,**kw):
        print("args",args)
        print("kw:",kw)
        if cls not in _instance:
            print("comein new instance...")
            _instance[cls] = cls(*args,**kw)
        print("_instance:",_instance[cls])
        return _instance[cls]
    return _single


@singleton
class SingleA:
    def __init__(self,name,age) -> None:
        print("__init__")
        self.name = name
        self.age = age
        pass

a1 = SingleA("name",18)
a2 = SingleA("ddd",20)
print(id(a1),id(a2))
print("========================")

'''
类装饰器
'''
class Singleton4:
    def __init__(self,cls) -> None:
        print("__init__")
        self.cls = cls
        self.instance = {}

    def __call__(self) :
        print("__call__")
        if self.cls not in self.instance:
            self.instance[self.cls] = self.cls() 
        return self.instance[self.cls]

@Singleton4
class SingleB:
    def __init__(self) -> None:
        print("SingleB __init__")

a1 = SingleB()
a2 = SingleB()
print(id(a1),id(a2))


class Call1:
    def __init__(self) -> None:
        print("__init__")

    def __call__(self):
        print("__call__")

a=Call1()
a()
        





