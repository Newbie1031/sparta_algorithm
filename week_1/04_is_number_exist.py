input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:   # array의 길이 만큼 아래 연산이 실행
        if num == number:   # 비교 연산 1번 실행
            return True

    return False


result = is_number_exist(3, input)
print(result)