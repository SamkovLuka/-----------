# myDict = dict()
# print(type(myDict))

# myDict2 = {"Developer":"Dmitro"}
# print(type(myDict2))
# myDict3 = {"Macbook":"Pro","Developer":"Oleksandr","Iphone":"15 Pro",1:"Hello world","1":"Hello to you"}
# print(myDict3)
# myDict3["Key"] = "Castle"
# # value = input("Enter value you want to add: ")
# # key = input("Enter key you want to add: ")
# # myDict3[key] = value
# myDict3.update(myDict2)
# print(myDict3)
# print(myDict3["1"])

# myDict4 = dict.fromkeys(["One","Two","Three","Four"],1)
# print(myDict4)
# print(myDict3.keys())
# print(myDict3.values())
# print(myDict3.items())
# print(myDict3.get("Developer"))
# print(myDict3.setdefault("Developer2"))
# print(myDict3)

# print(myDict3.pop("Developer"))
# print(myDict3)
# print(myDict3.popitem())

# my_dict = {"Mark":{"Phone":"097342423","Instagram":"@mark228","Tiktok":"@Mark777"},"Andrii":{"Phone":"06311214","Instagram":"@andrii228","Tiktok":"@andrii777"},"Sasha":{"Phone":"0973689295","Instagram":"@sasha228","Tiktok":"sasha777"}}
# user = my_dict[input("Enter name: ")][input("Enter data you wanna know: ")]
# print(user)







#завдання з уроку

dict = {"Alice": 30, "Bob": 25, "Charlie": 35}
items = ["Alice: 30", "Bob: 25", "Charlie: 35"]
keys = ["Alice", "Bob", "Charlie"]
values = [30, 25,35]
dict.update({"Dave":40})
print(dict)
print(dict.pop("Alice"))
print(dict.get("Bob"))
print(dict.setdefault("Charlie"))
for i in items:
    print(i)
for i in keys:
    print(i)
for i in values:
    print(i)


copy = {}
copy.update(dict)
print(copy)





#дз

#1


rd = input("Введіть рядок: ")
n = len(rd)
key = rd
rd_dict = {key:n}
print(rd_dict)

#2

dict_1 = {"one": "a","two": "b", "three":"c"}
dict_2 = {"four": "d","two": "b", "five":"e"}
dict_1.update(dict_2)
list_1 = []
print(dict_1)
if dict_1.keys == dict_2.keys:
    list_1.insert(dict_1.keys, dict_1.keys)
print(list_1)

#3

key = input("Введіть ключ: ")
value = input("введіть значення: ")
st_dict = {key: value}
if key == value:
   print("Only unique elements!")
print(st_dict)
fin_dict = {value:key}
print(fin_dict)
