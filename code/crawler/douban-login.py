#conding=utf-8

# 导入webdriver对象，可以调用浏览器和操作界面
from selenium import webdriver
# 导入Key，可以通过该对象操作鼠标，键盘，标签
from selenium.webdriver.common.keys import Keys

# 创建PhantomJs浏览器对象
driver = webdriver.PhantomJS(executable_path='/Users/linxingzhang/Library/Python/3.6/lib/python/site-packages/selenium/webdriver/phantomjs')

driver.get('https://www.douban.com')

# 输入账号密码
driver.find_element_by_name('form_email').send_keys('xingzhanglin@gami.com')
driver.find_element_by_name('from_passworld').send_keys('01050310ling')

# 模拟点击
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

saveFlag = driver.save_screenshot('douban.png')
print(saveFlag)

driver.quit()
