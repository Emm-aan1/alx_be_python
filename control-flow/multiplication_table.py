number = int(input("Enter a number to see its multiplication table: "))

for num in range(1,11):
  prod = num * number
  print(f"{number} * {num} = {prod}")