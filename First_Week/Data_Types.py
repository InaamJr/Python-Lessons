x = "Python{}"       #{}are used to pass a value for a string
y = "Lion"
z = """\nHello World... I'm a proud Sri Lankan :)"""

#check the type
#print(type(x), x)


#print(x, y, z)

#print a letter of variable x according to indexes
#print(x[-2])



#intiger
a = 0

#check the type
#print(type(a))


#print(x.format(a))   #.format is used to pass the int value of "a" for x

#another method to use the .format method
#print(f"Inaam Ahamed {y}")



#float
b = 0.0

#print(type(b))

#Github Test
#print("Configure Git")



#list
l1 = [1, 2, 3, "Jr", 0.0]

#print the 4th element in the array l1
#print(l1[3])

#print first four elements of the array l1
#print(l1[0:4])

#to fint the length of the array l1
#print(len(l1))



#tuple
tuple1 = (1, 2, 3, 4)

#print tuple1
#print(tuple1)



#boolean
is_created = False
is_failed = True

#print variable and its data type
#print(is_created, type(is_created))



#set
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])

#print(set1)



#dictionary
dict = {}
dict1 = {
    "name": "Inaam",
    "age": 16,
    "mobile": '0764935825'
}

dict2 = {
    "name": "Ahamed",
    "age": 18,
    "mobile": '0764935825'
}


#print(dict1['mobile'])

list = []
list.append(dict1)
list.append(dict2)
#print(list)



import pandas as pd

df = pd.DataFrame(list)
print(df.head())
print(type(df))

