# 전화번호 목록
# Little Help
# in : 중간에 매치되는 것도 셈,
# len으로 정렬 후 값 정

def solution(phone_book):
    phone_book = sorted(sorted(phone_book, key=lambda x: len(x)))
    '''
    for a in range(len(phone_book)-1):
        for b in range(a+1, len(phone_book)):            
            tmp = phone_book[b][:len(phone_boo렬k[a])]
            if phone_book[a] == tmp:
                return False
    '''
    for a in range(len(phone_book) - 1):
        if phone_book[a] == phone_book[a + 1][:len(phone_book[a])]:
            return False

    return True

# phonenumber 리스트를 값과 길이 두 가지 기준으로 정렬 하면, 반복문을 돌며 phonenumber[index] 가 phone_number[index+1]의 접두어 인지만 확인해주면 효율성 통과가 가능합니다.