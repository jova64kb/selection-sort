def selection_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i] ^= numbers[j]
                numbers[j] ^= numbers[i]
                numbers[i] ^= numbers[j]

