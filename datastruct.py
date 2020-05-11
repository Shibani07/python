#Assigning elements to different lists
colours=['red','blue','yellow']
print("colours:",colours)
numbers=[50,60,70,80]
print("numbers:",numbers)

#accesing elements from a tuple
tup1=(1,2,3,4,5)
print(tup1[0])
print(tup1[2])
print(tup1[4])

#deleting different dictionary elements
d={
    "zack":22,
    "debby":27,
    "john":25,
}
print("the full list is:",d)
del d["debby"]
print("the list after deleting an element:",d)
