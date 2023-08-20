#===================================================================================================================
#                                              날씨정보 확인 API
#===================================================================================================================
import requests


# 날씨 클래스
class WeatherAPI:
    
    # 초기화 함수
    def __init__(self):
        self.base_url = 'https://api.open-meteo.com/v1/forecast'
     
    # 날씨정보 리턴 함수   
    def get_weather(self, city):
        city_info = cities.get(city)
        
        # 도시정보 확인
        if city_info:
            latitude = city_info['latitude']
            longitude = city_info['longitude']
            url = f'{self.base_url}?latitude={latitude}&longitude={longitude}&current_weather=true'
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                temperature = data['current_weather']['temperature']
                return f"현재 {city}의 기온은 {temperature}도 입니다."
            
            except requests.exceptions.RequestException as e:
                return f"날씨 정보를 가져오는 중에 문제가 발생했습니다: {e}"
            
            except KeyError:
                return f"날씨 정보를 처리하는 중에 문제가 발생했습니다."
        else:
            return f"아직 지원되지 않는 않는 도시입니다: {city}"



#===================================================================================================================
#                                                도시 목록 예제
#===================================================================================================================

# 도시목록
cities = {
            '서울': {'latitude': 37.57, 'longitude': 126.98},
            '대전': {'latitude': 36.3491, 'longitude': 127.3849},
            '런던': {'latitude': 51.5074, 'longitude': -0.1278},
            '도쿄': {'latitude': 35.6895, 'longitude': 139.6917},
            '오사카': {'latitude': 34.6937, 'longitude': 135.5022},
            '후쿠오카': {'latitude': 33.5904, 'longitude': 130.4017}
         }


#===================================================================================================================
#                                                     사용예제
#===================================================================================================================

# 콘솔 확인용
if __name__ == "__main__":
    city_name = '서울'  # 도시 이름 설정
    weather_api = WeatherAPI()
    weather_info = weather_api.get_weather(city_name)
    print(weather_info)

#===================================================================================================================