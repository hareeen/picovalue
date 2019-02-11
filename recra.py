import ssl
import arrow
import weig
from selenium import webdriver
import os
ssl._create_default_https_context = ssl._create_unverified_context

def getU(date):
    return "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=000&date="+str(date)


def crawlW(date):
    g=list()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    chro = webdriver.Chrome(chrome_options=options)
    chro.get(getU(date))
    for i in range(1,4):
        element = chro.find_element_by_xpath("//li[@class='num"+str(i)+"']//dl//dt//a")
        g.append(element.get_attribute('href'))
    for i in range(5, 51):
        element = chro.find_element_by_xpath("//li[@class='gnum" + str(i) + "']//dl//dt//a")
        g.append(element.get_attribute('href'))
    chro.quit()
    return g

s = str()


def recT(date):
    f = open(os.getcwd() + "/news_data.csv", "a")
    g = crawlW(date)
    for i in g:
        d = i + ','
        c = weig.get_weight(i, ['mathematics', 'physicalscience', 'English', 'history', 'medicalscience', 'religion'])
        for j in c:
            d += str(c[j])
            d += ","
        f.write(d[:-1]+'\n')


if __name__ == '__main__':
    recT(20170812)
