# Dictionary are set of key value pair enclosed within {}
# In an existing dictionary if the key is already present then while updating the values.. mentioned key's value will be updated.If key is not present then new item will be appended to the dictionary
#Keys in dictionary cannot be duplicated.. it should be unique

dict1 = {'key1': 'value1', 'key2': 'value2'}
print(dict1['key1'])

for key, value in dict1.items():
    print(key, value)

for key,value in dict1.items():
    print(value)