#sort tuples by second element in each tuple
data = [(1,5),(3,2),(2,8),(4,1)]
sortedData = sorted(data, key=lambda x: x[1])
print("Ordered by second element: ",sortedData)

#filter into even numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers: ", evens)

#filter by odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers: ", odds)

#Doubled numbers
doubles = list(map(lambda x: x * 2, numbers))
print("doubles: ", doubles)

#squaring numbers
squares = [(lambda x: x**2)(x) for x in range(1,20)]
print(squares)
