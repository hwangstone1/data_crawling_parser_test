from django.test import TestCase


result = []
for i in range(1,11):
    item_obj = {
        'one': i,
        'two': i,
        'three': i,
    }
    result.append(item_obj)
    print(type(item_obj))
print(type(result))
for item in result:
    print(item,end='\n')

# Create your tests here.
