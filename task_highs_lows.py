def count_low_high(num_list):
    new_list = []
    high_list = [int(num) for num in num_list if num > 50 or num % 3 == 0]
    low_list = [int(num) for num in num_list if num <= 50 and num % 3 != 0]

    new_list.append(len(low_list))
    new_list.append(len(high_list))

    if new_list:
        return new_list
    else:
        return None


list_of_nums = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(list_of_nums))
