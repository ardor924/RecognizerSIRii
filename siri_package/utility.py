#===================================================================================================================
#                                                  유틸기능 모듈
#===================================================================================================================


# 예약어 리스트를 반환하는 함수
def get_reserved_list():
    reserved_list = ["시리","검색","날씨","먼지","게임",'숫자','끝말잇기']
    return reserved_list


# 데스크탑 바탕화면 경로
def get_local_url(folder_name):
  '''
  데스크탑 바탕화면 경로(기본) 입니다.
  폴더 이름을 지정하면 바탕화면에 있는 폴더경로로 지정됩니다.
  '''
  URL = f'C:\\Users\\TETRA\\Desktop\\{folder_name}'
  return URL



    
# 문자열을 받아온뒤 쪼개서 리스트로 반환하는 함수
        # notice : 문자열을 입력받아 
        # 공백으로 쪼갠뒤, 리스트로 리턴한다.
def get_splited_string_list(string) :
    splited_string_list = string.split()
    return splited_string_list



           


# 특정단어 확인 함수
        # notice : 특정단어와 사용자입력 리스트를 인자로 받고
        # 사용자입력 리스트에 해당 해당 단어가 포함되어 있을때 True값을 리턴한다.     
def is_specific_word_in_list(specific_word,user_input_list):
    for user_input_word in user_input_list:
        if specific_word in user_input_word:
            return True
    return False





# 두 개의 리스트를 비교하여 
# 중복되지 않는 문자열을 반환하는 함수
def get_non_duplicate_string_from_two_list(source_list, filter_list):
    unique_list = [
                    source_item 
                    for source_item in source_list
                    if all(filter_item not in source_item for filter_item in filter_list)
                  ]
    # non_duplicate_string = " ".join(unique_list) # 단어 띄어쓰기 처리
    non_duplicate_string = " ".join(unique_list)
    return non_duplicate_string

    
