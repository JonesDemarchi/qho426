if status == 1:
  print("The status was 1")

print("This always prints!")

age = int (input("What is your age "))

if age < 18:
  print("you are a child")
elif age > 65:
  print("you are old")
elif age <= 30 and age >= 20:
  print("you are a grown up child")
else:
  print("you are an adult")