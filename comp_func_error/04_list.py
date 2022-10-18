'''numbers = []
for element in range(1,11):
  numbers.append(element)

print(numbers)

# ahora con menos código usando list comprehension
#sintaxis: [element for element in iterable if condicion]

numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)'''

# un ejemplo con una condición
numbers=[]
for i in range (1,11):
  if i%2==0:
    numbers.append(i*2)

print(numbers)

# ahora con menos código usando list comprehension

numbers_v2 = [i*2 for i in range (1,11) if i % 2 == 0]
print(numbers_v2)
