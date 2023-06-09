#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password = ""
for random_letters in range(1, nr_letters + 1):
  selected_letters = random.choice(letters)
  password += selected_letters

for random_numbers in range(1, nr_numbers + 1):
  selected_numbers = random.choice(numbers)
  password += selected_numbers

for random_symbols in range(1, nr_symbols + 1):
  selected_symbols = random.choice(symbols)
  password += selected_symbols

password_shuffled = random.sample(password, len(password))
password_result = ''.join(password_shuffled)
print(f"Generated password is: {password_result}")