from selenium import webdriver
'''
下面就是关键字驱动
'''
class webkey:
    def __init__(self):
        self.driver=None

    def openbrowser(self,br='gc'):
        '''
        打开浏览器
        :param br:gc=谷歌浏览器；ff=firefox浏览器；ie=IE浏览器
        :return:
        '''
        if br=='gc':
            self.driver=webdriver.Chrome()
        elif br=='ff':
            self.driver=webdriver.Firefox()
        elif br=='ie':
            self.driver=webdriver.Ie()
        else:
            print('浏览器暂不支持')
        #默认隐式等待10s
        self.driver.implicitly_wait(10)

    def geturl(self,url=None):
        '''
        打开网站
        :param url:网站地址
        :return:
        '''
        self.driver.get(url)

    def __find_ele(self,locator=''):
        '''
        八种定位方式
        :param locator:
        :return:
        '''
        pass


    def click(self,locator=None):
        '''
        找到，并点击元素
        :param locator:定位器，默认xpath
        :return:
        '''
        self.driver.find_element_by_xpath(locator).click()
    def input(self,locator=None,value=None):
        '''
        找到元素，并完成输入
        :param locator:定位器，默认xpath
        :param value:需要输入的字符串
        :return:
        '''
        self.driver.find_element_by_xpath(locator).send_keys(str(value))

    def intoiframe(self,locator=None):
        '''
        进入iframe
        :param locator:定位器，默认xpath
        :return:
        '''
        ele=self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.quit()