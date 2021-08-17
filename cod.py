from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class CODHelper:

    def __init__(self,coin_name):
        self.coin_name = coin_name
        
    
    def get_data(self, start_date):
        driver = webdriver.Chrome()
        driver.get(f"https://kr.investing.com/crypto/{self.coin_name}")

        # 팝업창 닫기
        driver.find_element_by_css_selector('.popupCloseIcon.largeBannerCloser').click()

        # 과거 데이터 들어가기
        elem = driver.find_element_by_xpath(f'//a[@href="/crypto/{self.coin_name}/historical-data"]')
        elem.click()
        time.sleep(3)

        # 달력열기
        driver.find_element_by_css_selector('.float_lang_base_2.historicDate').click()
        time.sleep(1)

        # 시작 날짜 입력
        date_start = driver.find_element_by_id('startDate')
        date_start.clear()
        date_start.send_keys(f'{start_date}')
        time.sleep(1)

        # 검색버튼 클릭
        driver.find_element_by_id('applyBtn').click()
        time.sleep(5)

        # 표에서 데이터 긁어오기
        table = driver.find_element_by_css_selector('.genTbl.closedTbl.historicalTbl')
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        rows.reverse()

        # 긁어온 데이터 2차원 리스트로 전처리 후 반환
        data_list = []
        for index, value in enumerate(rows[:-1]):
            data = value.find_elements_by_tag_name("td")[0:5]
            sample_list = []
            for i in range(5):
                sample_list.append(data[i].text)
            data_list.append(sample_list)
        driver.close()
        return data_list

    def get_data_yesterday(self):
        driver = webdriver.Chrome()
        driver.get(f"https://kr.investing.com/crypto/{self.coin_name}")

        # 팝업창 닫기
        driver.find_element_by_css_selector('.popupCloseIcon.largeBannerCloser').click()

        # 과거 데이터 들어가기
        elem = driver.find_element_by_xpath(f'//a[@href="/crypto/{self.coin_name}/historical-data"]')
        elem.click()
        time.sleep(3)

        table = driver.find_element_by_css_selector('.genTbl.closedTbl.historicalTbl')
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        data_list = []
        for index, value in enumerate(rows):
            data = value.find_elements_by_tag_name("td")[0:5]
            sample_list = []
            for i in range(5):
                sample_list.append(data[i].text)
            data_list.append(sample_list)
        driver.close()
        return data_list[1]

    
    def create_data_csv(self, data):
        f = open(f'coin/{self.coin_name}.csv','w', newline='')
        wr = csv.writer(f)
        for d in data:
            wr.writerow(d)
        f.close()

    def add_data_yesterday(self, data):
        f = open(f'coin/{self.coin_name}.csv','a', newline='')
        wr = csv.writer(f)
        wr.writerow(data)
        f.close

    def __del__(self):
        print(f'{self.coin_name} finish!')
