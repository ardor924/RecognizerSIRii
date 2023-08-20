#===================================================================================================================
#                                              네이버 검색 모듈
#===================================================================================================================
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class NaverSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search_naver(self, search_keyword):
        try:
            # Chrome WebDriver 초기화
            driver = self.driver
            driver.get('https://naver.com')
            
            # 검색 입력 필드를 기다림
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
            search_input = driver.find_element(By.CSS_SELECTOR, '#query')
            
            # 검색어 입력 및 검색 버튼 클릭
            search_input.send_keys(search_keyword)
            search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
            search_button.click()
            
            time.sleep(5)  # 5초 대기

        except Exception as error:
            # 예외 처리
            print(f'Error: {error}')
            print(f'Error Type: {type(error)}')


#===================================================================================================================
#                                                     사용예제
#===================================================================================================================
            
# 사용 예시
if __name__ == "__main__":
    naver_search = NaverSearch()
    search_keyword = "검색어"  # 원하는 검색어 입력
    naver_search.search_naver(search_keyword)

#===================================================================================================================