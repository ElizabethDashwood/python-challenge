import os
file = './Resources/results.txt'
with open(file, 'r') as text:
    print(text)
    lines=text.read()
    print(lines)