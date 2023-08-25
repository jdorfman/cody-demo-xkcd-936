import random
import pyperclip

with open('words.csv') as f:
    words = f.read().splitlines()

password = []
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
for i in range(4):
    password.append(random.choice(words))
    print(colors[i] + password[i] + '\033[0m', end='')

print()
password = ''.join(password)
pyperclip.copy(password)
print('Password copied to clipboard!')
