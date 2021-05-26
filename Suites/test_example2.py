import time

from selenium import webdriver
from Web.webkeys import webkey


class Test_Com:
    def setup_class(self):
        '''
        构造函数，创建对象的时候会执行
        初始化浏览器
        :return:
        '''
        self.web=webkey()
        self.web.openbrowser()


    def test_login(self):

        #打开网站
        self.web.geturl()
        #找到用户名输入框
        self.web.input('//*[@id="username"]','13800138006')#xpath定位
        self.web.input('id=username','13800138006')#id定位
        #输入密码
        self.web.input()
        #点击登录
        self.web.input()
    def test_Userinfo(self):
        '''
        需要先调登录成功的用例
        :return:
        '''
        time.sleep(1)
        self.web.geturl()
        #点击头像图片
        self.web.click()
        #进入iframe
        self.web.intoiframe()
        #上传图片
        #怎么转为相对地址
        self.web.input()
        #点击确定使用
        self.web.click()

    def test_search(self):
        '''
        依赖登录
        :return:
        '''
        time.sleep(1)
        self.web.geturl()
        #输入手机号
        self.web.input()
        #点击搜索
        self.web.click()

    def teardown_class(self):
        '''
        退出
        :return:
        '''
        self.web.quit()
