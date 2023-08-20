#===================================================================================================================
#                                              음성송출 API
#===================================================================================================================

import sys 
sys.path.append("C:\\Users\\TETRA\\Desktop\\HelloSiri\\siri_package")
import utility as util 
from gtts import gTTS
from playsound import playsound


# 음성송출 함수
def get_text_to_speech(text_source) :
    folder_name = "HelloSiri" # 폴더명 설정
    local_url = util.get_local_url(folder_name) # 기본경로 : 데스크탑 바탕화면 경로(기본). 여기에 저장할 폴더를 매개변수로 입력.
    audio_file = save_audio_file(text_source,local_url)
    playsound(audio_file)


#  음성저장 함수(text to mp3)
def save_audio_file(text_source,local_url) :
    audio_path = f"{local_url}\\audio_data\\siri_comment.mp3"
    text_to_voice = gTTS(text=text_source, lang="ko")
    text_to_voice.save(audio_path)
    return audio_path

#===================================================================================================================
#                                                     사용예제
#===================================================================================================================

# 콘솔 확인용
if __name__ == "__main__":
    get_text_to_speech('사용예제입니다')

#===================================================================================================================