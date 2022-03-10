def solution(phone_book):
    #선택 전화번호
    for i in range(len(phone_book)):
        # 선택 된 전화 번호의 다음 꺼
        for j in range(i+1,len(phone_book)):
            # 접두어인지 확인 하기 위해 파이썬 함수인 stringA.startswith(stringB) 함수 사용
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True