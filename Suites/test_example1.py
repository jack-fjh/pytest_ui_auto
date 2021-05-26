import pytest
class Test_S:
    def setup(self):
        '''
        用例级别的初始化
        每一个用例执行前都会去执行setup
        :return:
        '''
        print('用例开始')

    def teardown(self):
        '''
        用例级别的结束
        每一个用例执行后会去执行teardown
        :return:
        '''
        print('用例执行结束')

    def setup_class(self):
        print('所有用例开始前')

    def teardown_class(self):
        print('所有用例执行后')

    @pytest.fixture()
    def mysetup(self):
        '''
        fixture是先于setup执行的
        同理，yield后面的是先于teardown执行的
        :return:
        '''
        print('开始')
        yield
        print('结束')

    def test_01(self,mysetup):
        print('01')

    def test_02(self):
        print('02')

    def test_03(self,mysetup):
        print('03')