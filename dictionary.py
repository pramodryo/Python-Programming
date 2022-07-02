# 01 create a dictionary which carrys keys and values

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))







# 02 create a dictionary which store the fevourite language of student

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)
