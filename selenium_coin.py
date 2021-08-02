from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


coin_name = 'ethereum'
# bitcoin
# ethereum

driver = webdriver.Chrome()
driver.get(f"https://kr.investing.com/crypto/{coin_name}")
print('----')

# 팝업창 닫기
driver.find_element_by_css_selector('.popupCloseIcon.largeBannerCloser').click()
# 과거 데이터 들어가기
elem = driver.find_element_by_xpath(f'//a[@href="/crypto/{coin_name}/historical-data"]')
elem.click()
time.sleep(3)
# 달력열기
driver.find_element_by_css_selector('.float_lang_base_2.historicDate').click()
print('----')
time.sleep(1)
# 시작데이터 입력
date_start = driver.find_element_by_id('startDate')
date_start.clear()
date_start.send_keys('2015/01/01')
time.sleep(1)
# 검색버튼 클릭
driver.find_element_by_id('applyBtn').click()
time.sleep(5)
# 저장할 csv 오픈
# f = open(f'{coin_name}/{coin_name}_test.csv','w', encoding='utf-8')
# 표에서 데이터 긁어오기
table = driver.find_element_by_css_selector('.genTbl.closedTbl.historicalTbl')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
rows.reverse()
print('start')
f = open(f'coin/{coin_name}.csv','w', newline='')
wr = csv.writer(f)
for index, value in enumerate(rows):
    data = value.find_elements_by_tag_name("td")[0:5]
    data_list = []
    for i in range(5):
    #     print(data[i].text, end = '  ')
        data_list.append(data[i].text)
    wr.writerow(data_list)
    # print('')
print('finish')
f.close()
driver.close()





    # csv로 저장하기



# data = driver.find_elements_by_css_selector('.genTbl.closedTbl.historicalTbl')
# print(data)
# elem = driver.find_element_by_name("q")
# elem.send_keys('다나와')
# elem.send_keys(Keys.RETURN)
# driver.find_element_by_css_selector('.Zu0yb.LWAWHf.OSrXXb.qzEoUe').click()
# driver.find_element_by_css_selector('.btn_layer1_close1').click()


# elem = driver.find_element_by_name('k1')
# elem.send_keys('그래픽카드')
# elem.send_keys(Keys.RETURN)

# time.sleep(3)

# driver.find_element_by_css_selector('.ico.i_chkbox').click()


# elems = driver.find_elements_by_css_selector(".sc-eYdvao.kvdWiq [href]")
# links = [elem.get_attribute('href') for elem in elems]

# elem = driver.find_element_by_name('k1')
# elem.send_keys('그래픽카드')
# elem.send_keys(Keys.RETURN)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()