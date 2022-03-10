def solution(phone_book):
    #오름 차순
    phone_book.sort()
    #선택 전화번호
    for i in range(len(phone_book)):
        if phone_book[i+1].startswith(phone_book[i]):
           return False
    return True