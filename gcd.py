from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


class GCDHelper:
    """셀레니움 크롤링에 필요한 기능들을 제공합니다.
    
    """
    
    def get_data_today(self, gcname):
        """그래픽 카드의 가격정보를 추출합니다.
        셀레니움을 이용하여 '다나와 닷컴'에서 그래픽 카드 검색을 통해
        인기 상품의 5순위까지의 가격데이터를 리스트로 반환합니다.

        Args:
            gcname : 요청한 그래픽 카드 이름 크롤링시 검색에 사용
        
        Returns:
            가격 데이터 리스트를 반환합니다.
        """

        driver = webdriver.Chrome()
        driver.get('http://www.danawa.com/')

        elem = driver.find_element_by_name('k1')
        elem.send_keys(f'{gcname}')
        elem.send_keys(Keys.RETURN)

        time.sleep(3)

        result = []
        total = 0
        search_list = driver.find_elements_by_css_selector('.click_log_product_standard_price_')
        for i in range(5):
            search = search_list[i].text[:-1]
            search = int(search.replace(',',''))
            result.append(search)
        driver.close()
        return result

    def update_data_csv(self, data, gcname = 'graphicscard'):
        """불러온 데이터를 맞는 csv 파일에 추가하여줍니다.

        Args:
            data : 리스트 형태로 .csv 파일에 추가됩니다.
            gcname : 요청한 그래픽 카드 이름 .csv 파일이름을 찾을 때 사용
                    기본값에 종합데이터 파일이름 넣어줌
        
        Returns:
            None
            gcname.csv 파일에 날짜와 함께 데이터를 입력
        """
        now = time.localtime()
        result = []
        result.append(f'{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일')
        result.extend(data)
        f = open(f'graphicscard/{gcname}.csv','a',newline='')
        wr = csv.writer(f)
        wr.writerow(result)
        f.close()