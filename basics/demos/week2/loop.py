          # Loop
n = int(input("Enter the number: "))
counter = 1
#print(f"{n}x1 = {n*1}")
#print(f"{n}x2 = {n*2}")
#print(f"{n}x3 = {n*3}")
n2 = int(input("Enter the limit of the table: "))

#while counter <= 10:
  #print(f"{n}x{counter} = {counter*n} ")
  #counter +=1

while counter <= n2:
  print(f"{n}x{counter} = {counter*n} ")
  counter +=1

print("The end")