abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Welcome Caesar Cipher")
print("e = encode a message")
print("d = decode a message")
print("q = quit")

choice = input("Please enter your choice: ")
if(choice == 'e'):
  encode = input("Enter the string to encode: ")
  shift = int(input("Enter the amount to shift: "))

elif(choice == 'd'):
  decode = input("Enter the string to encode: ")
  shift = int(input("Enter the amount to shift: "))
    
elif(choice == 'q'):
  print("Caesar thanks you!")


while(choice != 'q'):

  print("")
  print("")

  abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  print("Welcome Caesar Cipher")
  print("e = encode a message")
  print("d = decode a message")
  print("q = quit")

  choice = input("Please enter your choice: ")
  if(choice == 'e'):
    encode = input("Enter the string to encode: ")
    shift = int(input("Enter the amount to shift: "))

  elif(choice == 'd'):
    decode = input("Enter the string to encode: ")
    shift = int(input("Enter the amount to shift: "))
    
  elif(choice == 'q'):
    print("Caesar thanks you!")