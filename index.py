class Convert:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    print("You can convert the value to other types")
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    value = input("Enter the type you want to convert to: ")
    
value = int(input("Enter a value: "))
convert = Convert(value)
print(convert)