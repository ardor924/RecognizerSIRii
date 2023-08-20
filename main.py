#===================================================================================================================
#                                                메인 실행 파일
#===================================================================================================================

import time
from siri_package import utility as util
from siri_package import siri_system as siri
from siri_package import tts_api as tts
from siri_package.naver_search import NaverSearch as naver
from siri_package.weather import WeatherAPI as wea
from siri_package.air_quality import AirQualityAPI as air
from siri_package.number_game import NumberGame as numGame
from siri_package.word_chain_game import WordChainGame as wordGame


# 상수 정의
CITY_NAME = '대전'  # 도시 이름 세팅
DISTRICT_NAME = '월평동'  # 도시 내 행정구역 이름 세팅



# 메인함수
def main():
    
    # 시작화면 출력
    siri.invoke_siri_system() 
    
    while True:
        # 음성 입력 받기
        user_input = siri.get_text_from_voice()
        # 입력된 문자열을 리스트로 분할
        user_input_list = util.get_splited_string_list(user_input)
        # 예약어 리스트 가져오기
        reserved_list = util.get_reserved_list()


        # 특정 단어 포함 여부 확인
        siri_on = util.is_specific_word_in_list('시리', user_input_list)  
        search_on = util.is_specific_word_in_list('검색', user_input_list)  
        weather_on = util.is_specific_word_in_list('날씨', user_input_list) 
        dust_on = util.is_specific_word_in_list('미세먼지', user_input_list) 
        number_game_on = util.is_specific_word_in_list('게임', user_input_list)  
        word_chain_game_on = util.is_specific_word_in_list('끝말잇기 게임', user_input_list)  


        # '시리' 음성 인식 활성화
        if siri_on:            
            # 네이버 검색 실행
            if search_on:
                run_naver_search(user_input_list, reserved_list)
                  
            # 날씨 정보 출력    
            elif weather_on:
                display_weather_info()  
                
            # 미세먼지 정보 출력    
            elif dust_on:
                display_air_quality_info() 
                
            # 숫자 게임 시작(미구현)     
            elif number_game_on:
                start_number_game()  
                
            # 끝말잇기 게임 시작(미구현)    
            elif word_chain_game_on:
                start_word_chain_game()  
                
#===================================================================================================================
#                                                   함수정의
#===================================================================================================================


# 네이버 검색 실행 함수
def run_naver_search(user_input_list, reserved_list):
    search_keyword = util.get_non_duplicate_string_from_two_list(user_input_list, reserved_list) # 중복 제거된 검색 키워드 얻기
    naver_module = naver()
    naver_module.search_naver(search_keyword)

# 날씨 정보 출력 함수
def display_weather_info():
    weather_api = wea()
    weather_info = weather_api.get_weather(CITY_NAME)
    print(weather_info)
    tts.get_text_to_speech(weather_info)
    
# 미세먼지 정보 출력 함수
def display_air_quality_info():
    air_info_api = air()
    air_quality_comment_char,air_quality_comment_kor = air_info_api.get_air_info(CITY_NAME, DISTRICT_NAME)
    print(air_quality_comment_char)
    tts.get_text_to_speech(air_quality_comment_kor)

# 숫자 게임 로직 (미구현..)
def start_number_game():
    print("숫자게임을 시작합니다...")
    numGame().play()
    
# 끝말잇기게임 (미구현..)
def start_word_chain_game():
    print("끝말잇기게임 시작을 합니다...")
    time.sleep(1)


#===================================================================================================================
#                                                     코드실행
#===================================================================================================================

# 코드실행
if __name__ == "__main__":
    main()

#===================================================================================================================