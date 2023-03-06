input = 20


def find_prime_list_under_number(number):
    prime_list = []
    a = 2

    for num in range(number):
        if not num == 0 or 1:
            if num % a != 0:
                a += 1
                if

        prime_list = num

    return prime_list


result = find_prime_list_under_number(input)
print(result)