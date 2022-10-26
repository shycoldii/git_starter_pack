def findValue(numbers, number_to_find, low, high):
    if high >= low:
        middle = low + (high - low) // 2

        if numbers[middle] == number_to_find:
            return middle
        elif numbers[middle] < number_to_find:
            return findValue(numbers, number_to_find, middle + 1, high)
        else:
            return findValue(numbers, number_to_find, low, middle - 1)

    else:
        return -1

numbers = [7, 9, 14, 22, 34]
number_to_find = 22

final = findValue(numbers, number_to_find, 0, len(numbers) - 1)

if final == -1:
	print("This item was not found in the list.")
else:
	print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")