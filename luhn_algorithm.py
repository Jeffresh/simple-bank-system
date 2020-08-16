def luhn_algorithm(number_list):
    odds_index_by2 = [number_list[i] * 2 if (i + 1) % 2 == 1 else number_list[i] for i in range(len(number_list))]
    subtract_9 = [number - 9 if number > 9 else number for number in odds_index_by2]
    print(subtract_9)
    sum_numbers = sum(subtract_9)
    return sum_numbers


if __name__ == '__main__':
    card_number = '400000921451540'
    digits_sum = luhn_algorithm(list(map(int, card_number)))
    print(digits_sum)
    for i in range(10):
        if (digits_sum + i) % 10 == 0:
            card_number = card_number + str(i)

    print(card_number)
