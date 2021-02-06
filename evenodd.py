array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print(array_nums)
odd = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nEven numbers: ", even)
print("\nOdd numbers: ", odd)