name = input("Enter name please :")
age = input("Enter age please :")
address = input("Enter address please :")


if (name == '' or age == '' or address == ''):
      print('is empty input')


if isinstance(name, str) and age.isdigit():
      print(f"Mr/Ms {name} age {age} located in {address}. ",'\n'
      f"thanks for beening one of our community ,      Enjoy")
else:
      print("problem !!")

