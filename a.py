#SETS
myset = {"hello", " there", "is", "this", "mutable",False,0}
print(myset)

myset[0] = "bye" #'set' object does not support item assignment
del myset[0] # set' object doesn't support item deletion
#main


#INDEXING
list1 = ["Hello","World","This","is","a","non-homogeneous","list",True,50,100]
print(list1)
print()

#Positive indexing
print("****Positive indexing****")
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])
print(list1[9])

print()
#Negative indexing
print("****Negative indexing****")
print(list1[-10])
print(list1[-9])
print(list1[-8])
print(list1[-7])
print(list1[-6])
print(list1[-5])
print(list1[-4])
print(list1[-3])
print(list1[-2])
print(list1[-1])
