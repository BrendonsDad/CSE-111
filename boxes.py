import math

items = int(input('What is the number of manufactured items? '))
box_size = int(input('How many will you pack per box? '))

rawnum = items / box_size
refnum = math.ceil(rawnum)

if refnum == 1:
    print(f'For {items} items, packing {box_size} items in each box, you will need {refnum} box. ')

else:
    print(f'For {items} items, packing {box_size} items in each box, you will need {refnum} boxes. ')