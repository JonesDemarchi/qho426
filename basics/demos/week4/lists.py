red = []

#Declare a non-empty list
amber = ["Poland", "Portugal", "Romania", "Fiji", "Amber"]

#print full list
print(amber)

#print a single element
print(amber[3])

#Add elements to a list
red.append("Brazil")
red.append("Somalia")
red.append("Malta")

#for i in range(3):
  #red.append(input("Enter new red list country: "))

print(red)
#Insert data onto a list not at the end
red.insert(1, "Gana")
print(red)
red.insert(3, "Switzerland")
print(red)

#remove an item from the list
red.remove(input("Which country to delete: "))
print(red)

#Remove an item from list by Index
red.pop(0)
print(red)

#slicing
print("---slicing---")