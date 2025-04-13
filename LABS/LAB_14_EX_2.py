'''
2. Napisz funkcję zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)
'''

# 1 sposób

list_1=[1,2,2,20,5]
list_2=[1,5,6,5]
list_3=[4,7,9,5]

print (list_1)
print (list_2)
print (list_3)

def unique_list():
    numbers = list_1 + list_2 + list_3
    unique_numbers = list(set(numbers))
    unique_numbers=tuple(unique_numbers)
    print(tuple(unique_numbers))  # Output: [1, 2, 3, 4, 5]

unique_list()

# 2 sposób

def marge_list_without_duplicates(source,target):
    for element in source:
        if element not in target:
            target.append(element)


def transform_data (list1,list2,list3):
    result=[]
    marge_list_without_duplicates(list1, result)
    marge_list_without_duplicates(list2, result)
    marge_list_without_duplicates(list_3, result)
    result.sort()
    return tuple(result)

print(transform_data(list_1,list_2,list_3))