import time
from selenium import webdriver

def login(name, passwd):
    try:
        browser = webdriver.Chrome()
        browser.get('https://shimo.im/')
        browser.maximize_window()

        btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
        time.sleep(3)
        name_field = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')
        name_field.send_keys(name)
        passwd_field = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')
        passwd_field.send_keys(passwd)       
        login_button = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
        login_button.click()

        cookies = browser.get_cookies()
        print(cookies)
        time.sleep(7)
    
    except Exception as e:
        print(e)
    finally:    
        browser.quit()
     
if __name__ == '__main__':
    login_name = input('请输入你的登录账号:\n')
    login_passwd = input('请输入你的登录密码:\n')
    cookies = login(login_name, login_passwd)    
