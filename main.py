import pytest,os

'''
1：执行pytest单元测试，生成Allure报告需要的数据存在/temp目录
pytest.main(['alluredir','./temp'])
2：执行命令allure generate ./temp -o ./report --clear,生成测试报告
os.system('allure generate ./temp -o ./report --clean')
'''



if __name__ == '__main__':
    pytest.main(['-s','-q','Suites/test_example5.py','--clean-alluredir','--alluredir=./temp'])
    os.system('allure generate ./temp -o ./report --clean')



