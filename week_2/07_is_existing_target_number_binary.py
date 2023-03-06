finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    current_guess = 0
    for current_guess in finding_numbers:
        if current_guess == 2:
            return True
    # 이 부분을 채워보세요!
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)