'''
反射
'''

class A:
    def a(self,p1):
        '''
        完成功能a
        :param p1:所需参数
        :return: 返回结果
        '''
        print('完成功能a'+str(p1))
        return 'PASS','相关信息'

    def b(self,p1,p2):
        '''
        完成功能b
        :param p1:
        :param p2:
        :return:
        '''
        print('完成功能b'+str(p1))
        print(p2)
        return 'PASS','相关信息'

    def c(self,p1,p2,p3):
        '''
        完成功能c
        :param p1:
        :param p2:
        :param p3:
        :return:
        '''
        print('完成功能c'+str(p1))
        print(p2)
        print(p3)
        return 'PASS','相关信息'
s='a'
obj=A()
func=getattr(obj,s)#从这个对象里面获取到一个叫a的属性或方法
func('1')#func直接用代表用的变量，如果有小括号代表调的函数
print('-------')
func=getattr(obj,'b')
func('1','2')