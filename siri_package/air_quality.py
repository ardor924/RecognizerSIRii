#===================================================================================================================
#                                              미세먼지농도 확인 API
#===================================================================================================================

import requests
import json

class AirQualityAPI:
    
    # 초기화
    def __init__(self):
        self.service_key = 'v6PZedo0OjiH84tKhGwXk8GpKTqVAbkYOrvk0crJjrGW7mJALzmAw0YQKf4csjvmkJcYhdAo0RtTLPrIBF66qQ=='
        self.base_url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

    # 미세먼지정보 리스트 반환
    def get_air_info(self, search_city, search_district):
        
        # API 요청 파라미터 설정
        params = {
            'serviceKey': self.service_key,
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'sidoName': search_city,
            'ver': '1.0',
        }
        try:
            # API 호출 및 데이터 파싱
            response = requests.get(self.base_url, params=params)
            data = json.loads(response.text)
            airinfo_list = data['response']['body']['items']

            data_result = []
            for airinfo in airinfo_list:
                data_result.append([airinfo['stationName'], airinfo['sidoName'], airinfo['pm25Value']])

            # 검색 조건에 맞는 리스트 필터링
            matching_list = [
                                data
                                for data in data_result
                                if search_district in data
                            ]

            if matching_list:
                result_air_info_list = matching_list[0]
                comment = f'현재 {result_air_info_list[1]} {result_air_info_list[0]}의 미세먼지 농도는 {result_air_info_list[2]}'
                air_quality_comment_char = comment + ' ㎍/m³ 입니다.'
                air_quality_comment_kor = comment + ' 마이크로그램 퍼 세제곱 미터 입니다.'
                return air_quality_comment_char, air_quality_comment_kor
            else:
                return [], []


        except Exception as e:
            print('에러 발생:', str(e))
            return []

# 결과 출력함수
def print_air_info(air_info_list):
    for item in air_info_list:
        print(item)
        


#===================================================================================================================
#                                                     사용예제
#===================================================================================================================

# 사용 예시
if __name__ == '__main__':
    service_key = 'v6PZedo0OjiH84tKhGwXk8GpKTqVAbkYOrvk0crJjrGW7mJALzmAw0YQKf4csjvmkJcYhdAo0RtTLPrIBF66qQ=='
    air_quality_info = AirQualityAPI()

    search_city = "서울"
    search_district = '송파구'

    air_info_list = air_quality_info.get_air_info(search_city, search_district)

    # 결과 출력
    print_air_info(air_info_list)
    
#===================================================================================================================
