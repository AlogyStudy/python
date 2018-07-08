#coding-utf=8

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs

class Douyu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    # unittest测试方法必须有`test`字样开头
    def testDouyu(self):
        self.driver.get('https://www.douyu.com/directory/all')
        while True:
            soup = bs(self.driver.page_source, 'lxml')
            names = soup.find_all('h3', {'class': 'ellipsis'})
            viewNums = soup.find_all('span', {'class': 'dy-num fr'})
            
            for name, viewNum in zip(names, viewNums):
                print('房间名' + name.get_text() + '; ' + '观众人数' + viewNum.get_text())

            # 在页面源码中找到"下一页"未隐藏的标签，就退出循环
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            # 一直点击下一页
            self.driver.find_element_by_class_name('shark-pager-next').click()    

    # 测试结束执行的方法
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
