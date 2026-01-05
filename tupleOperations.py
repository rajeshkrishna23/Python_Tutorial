# Operations on tuple which can be performed are
# 1. Concatenation
# 2. Repetition
# 3. membership
# 4. count ,index
# 5. min , max

tuplePerson = ("John","Mendoza")
print(id(tuplePerson))
tuple2 = (54 , "Agriculturist",4.5)
tuplePersonDetails = tuplePerson + tuple2
tuplePerson = tuplePersonDetails
print(tuplePerson)

print(id(tuplePersonDetails))
print(id(tuplePerson))

testTuple =("Python","Java","C++")
repetitionTuple = testTuple * 3

print(repetitionTuple)

