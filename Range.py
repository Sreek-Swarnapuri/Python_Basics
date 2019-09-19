#Range function creates sequential list of numbers
#Range method itself creates a range object, we would need to call list fucntion in order to convert it to a list
numbers = list(range(10))
print(numbers)
rng = range(5)
print(type(rng))
print(rng)

#range with two arguments will produce a numbers from first argument to second
numbers = list(range(3,8))
print(numbers)

#range can have a third argument which determines the interval of the sequence produced
numbers = list(range(2,10,2))
print(numbers)
