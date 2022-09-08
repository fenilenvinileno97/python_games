#filter, map, reduce

random_numbers = [1, 3, 5, 7, 9, 13, 19, 21]
odd = list(filter(lambda x: x%2 ==0, random_numbers))
print(odd)