'''
知识点：参数化实例

'''
import pytest
def sum(x,y):
    return x+y


class Test_Data:
    '''

    使用方法
        parametrize(argnames,argvalues)
            常用参数：
                argnames:参数名
                argvalues:参数对应值，类型必须为list或元祖
                        当参数个数为一个时,格式：[value]
                        当参数个数大于一个时,格式为[(param_value1,param_value2),(param_value1,param_value2)]
            使用方法:
                @pytest.mark.parametrize(argnmaes,argvalues)
                参数值为n个，测试方法就会运行n次
    '''
    @pytest.mark.parametrize('x,y,z',[
        [1,1,2],
        [1,2,3],
    ])
    def test_sum(self,x,y,z):
        '''
        测试相加
        :return:
        '''
        assert sum(x,y)==z

