# Sets -  non-sequential collection of items
# comma seperated elements closed within {}

setTest ={1,2,3,4,2,1}

print(setTest)

# sets  cannot have indexing as its non-sequential
#sets do not allow duplicate elements

#operations on sets
#membership
#concatenation ? no not possible
s1= {1,2,3,4}
s2={5,2,7,8}
print(s1 & s2)
print(s1|s2)
print(s1^s2)
#sets are mutable but how ?
# By using a couple of functions we can update the set
s1.add(12)
print(s1)
s1.pop()
s1.remove(12)
print(s1)
s1.copy()
print(s1)
s1.update({1,2,3,4})
print(s1)
s1.remove(1)
print(s1)
s1.add(3)
print(s1)
#operation on sets
# Union → Combines all unique elements from both sets.
#
# Intersection → Returns elements common to both sets.
#
# Difference → Returns elements present in one set but not in the other.
#
# Symmetric Difference → Returns elements present in either set but not in both.
#
# Subset → Checks whether all elements of one set exist in another set.
#
# Superset → Checks whether a set contains all elements of another set.
#
# Disjoint → Checks whether two sets have no elements in common.
#
# Membership → Checks whether a specific element exists in a set.
#
# Set Update → Modifies a set in place based on another set.
#
# Copy → Creates a shallow copy of a set.
student1_SubjectSet ={"English","Maths","CS","Chemistry","Physics"}
student2_SubjectSet ={"English","Biology","Chemistry","Physics"}
#Intersection : Returns elements common to both sets.
common_SubjectSet =student1_SubjectSet & student2_SubjectSet
print(common_SubjectSet)

symmetricDiff = student1_SubjectSet ^ student2_SubjectSet
print(symmetricDiff)

#frozen sets
#Frozen sets are immutable sets
frozenSet = frozenset({1,2,3,4})

print(frozenSet ,type(frozenset))


print(frozenSet)