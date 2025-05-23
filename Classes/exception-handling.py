#Lambda function
# lst1 = [("name1",1),("name2",4),("name3",5)]
# lst1.sort(key = lambda x: x[1])
# print(lst1)

#Recursive Function

# def counter(x):
#     print(x)
#     if x <=0:
#         return True
#     counter(x-1)


# counter(10)

#exception handling

dc = {"name":"John", "age":30, "city":"New York"}   
try:
    print(dc["role"])
except Exception as e:
    print(f"can't find the {e} key")

finally:
    print("the key's are : name, age, city")