class Convert:
  def __init__(self, value, choise):
    self.value = value
    self.choise = choise

  def logic(self):
    print("You can convert the value to other types")
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    self.choise = input("Enter the type you want to convert to: ")
    if(self.choise == 1):
      return self.convert_to_binary()


  def convert_to_binary(self):
    return bin(self.value)
    

value = int(input("Enter the value you want to convert: "))
convert = Convert(value, 1)
print(convert.logic())