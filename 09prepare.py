text_list = []

with open('provinces.txt') as text_file:
    for line in text_file:
        clean_line = line.strip()
        text_list.append(clean_line)

print(text_list)

text_list.pop(0)
text_list.pop()


for i in range(len(text_list)):
    if text_list[i] == 'AB':
        text_list[i] = 'Alberta'
    else:
        bob = 'bob'

counter = text_list.count('Alberta')

print(f'Aberta occurs {counter} times in the modified list')




