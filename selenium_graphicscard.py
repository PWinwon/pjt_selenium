from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


products = ['RTX 3090', 'RTX 3080 Ti', 'RTX 3080 -Ti', 'RTX 3070 Ti',
            'RTX 3070 -Ti', 'RTX 3060 Ti', 'RTX 3060 -Ti',
            'RTX 2060 super', 'RTX 2060 -super',
        ]
now = time.localtime()
result_avg = []
result_avg.append(f'{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일')
for product in products:
    driver = webdriver.Chrome()
    driver.get('http://www.danawa.com/')

    elem = driver.find_element_by_name('k1')
    elem.send_keys(f'{product}')
    elem.send_keys(Keys.RETURN)

    time.sleep(5)
    search_list = driver.find_elements_by_css_selector('.click_log_product_standard_price_')
    f = open(f'graphicscard/{product}.csv','w',newline='')
    wr = csv.writer(f)
    result = []
    total = 0
    result.append(f'{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일')
    for i in range(5):
        search = search_list[i].text[:-1]
        search = int(search.replace(',',''))
        total += search
        result.append(search)
    result_avg.append(int(round(total/5)))
    wr.writerow(result)
    f.close()
    driver.close()
    
f = open(f'graphicscard/graphicscard.csv','w',newline='')
wr = csv.writer(f)
wr.writerow(['제품목록'] + products)
wr.writerow(result_avg)
f.close()


