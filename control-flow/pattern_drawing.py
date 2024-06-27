user = int(input("Enter the size of the pattern: "))
row = 0

while row < user:
  for j in range(user):
    print("*", end="")
  
  print()
  row += 1