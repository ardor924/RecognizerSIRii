import sys 
sys.path.append("C:\\Users\\TETRA\\Desktop\\HelloSiri\\siri_package")
import tts_api as tts
import siri_system as siri
import random

import random

class NumberGame:
    
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.max_attempts = 10

    def play(self):
        tts.get_text_to_speech("1부터 100 사이의 숫자를 맞추어보세요.")

        for attempt in range(1, self.max_attempts + 1):
            user_guess = int(input(f"시도 {attempt}/{self.max_attempts}: ")) 
            # user_guess = int(siri.get_text_from_voice()) # SST 한글 -> 숫자 변경 구현 준비중...
            
            if user_guess == self.secret_number:
                tts.get_text_to_speech(f"축하합니다! {attempt}번 만에 정답을 맞췄습니다.")
                break
            
            if user_guess < self.secret_number:
                tts.get_text_to_speech("업!")
            else:
                tts.get_text_to_speech("다운!")
        else:
            tts.get_text_to_speech(f"아쉽지만 정답은 {self.secret_number}였습니다. 다시 도전해보세요!")

if __name__ == "__main__":
    game = NumberGame()
    game.play()