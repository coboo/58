#-*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def onlynum(s,oth=''):
    s2 = s.lower()
    fomart = '0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'')
    return s
 
def wife() :
    phantomjs_path = r'D:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    driver = webdriver.PhantomJS(phantomjs_path)
    driver.get("http://gz.58.com/tianhe/waimai/")
    dataList = driver.find_elements_by_xpath('//*[@id="infolist"]/table/tbody/tr/td/div/span/a') #获取点击显示联系电话的按钮
    with open('csvfile.csv', 'wb') as csvfile:
        rows = csv.writer(csvfile)
        try :
            for index,each in enumerate(dataList) :
                each.click()
                time.sleep(2) #每个按钮点一下，然后等前端渲染完毕
                tel = driver.find_elements_by_class_name('jumpDiv_tel')
                codeTel = onlynum(tel[index].text.encode('UTF-8'))
                print(codeTel)
                rows.writerow(str(codeTel))

    #        tel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jumpDiv_tel")))
        finally :
                driver.close()
def main():
    pass

if __name__ == '__main__':
    wife()
    #print(onlynum('341234...'))