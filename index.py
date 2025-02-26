class Convert:
    def __init__(self, value, choice):
        self.value = value
        self.choice = choice

    def logic(self):
        print("You can convert the value to other types")
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        self.choice = int(input("Enter the type you want to convert to: "))
        if self.choice == 1:
            return self.convert_to_binary()
        elif self.choice == 2:
            return self.convert_to_octal()
        elif self.choice == 3:
            return self.convert_to_hexadecimal()
        else:
            return "Invalid"

    def convert_to_binary(self):
        return bin(self.value)

value = int(input("Enter the value you want to convert: "))
convert = Convert(value, 1)
print(convert.logic())
