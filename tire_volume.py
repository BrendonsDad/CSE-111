import math
import time
from datetime import datetime

##Logo
print()
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('                                                                                                                        ///')
print('|||||   |||   ||||||||        ||||||||||||          |||||||||||    |||   |||||||||    ||||||||     |||||||             ///')
print('||  ||  |||   ||              |||      |||              |||        |||   |||    ||    |||         |||                 ///')
print('|||||   |||   ||  |||||       |||      |||              |||        |||   |||   ||     |||||       |||||||            ///')
print('||  ||  |||   ||     ||       |||      |||              |||        |||   |||||||      |||              |||          ///')
print('||||||  |||   |||||||||       ||||||||||||              |||        |||   ||    |||    |||||||||   |||||||          ///')
print('                                                                                                                  ///')
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print()
print()
print()
time.sleep(2)

#Starting the loop
keep = ''
while keep.lower() != 'quit':
    print()
    print('Want a custum tire? Enter info below based on what you are looking for, and \nwe will build any tire you want! Type QUIT when you are finished')
    print()
    time.sleep(1)
    width = (input('Please enter the width of the tire in mm(ex 205): '))
    if  width.lower() == 'quit':
        keep = 'quit'
    else:
        width = float(width)
        print()
        aspect = float(input('Please enter the apect ratio of the tire (ex 60): '))
        print()
        diameter = float(input('Please enter the diamter of the wheel in inches (ex 15): '))
        print()

        volume1 = math.pi * (width**2) * aspect
        bignum = 2540 * diameter
        volume2 = volume1 * (width*aspect + bignum)
        volume3 = volume2 / 10000000

        ##Getting the price and displaying volume
        print(f'The approximate volume is {volume3:.1f} milliliters. ')
        time.sleep(2)
        if width >= 245 or aspect >= 80 or diameter >=19:
            price = 345.98
        
        elif width >= 235 or aspect >= 65 or diameter >=18:
            price = 162.49
        
        elif width >= 235 or aspect >= 60 or diameter >=15:
            price = 149.48

        elif width >= 215 or aspect >= 55 or diameter >=16:
            price = 114.62

        else:
            price = 99.99
        
        ## Displaying price and discount and asking if they want them
        print(f'The price of your custum tire is ${price}')
        print()
        discount2 = price * 2 * .1
        discount4 = price * 4 * .15
        print(f'If you buy a set of 2, you will get a 10 percent discount (${discount2:.2f}) \n if you puchase 4 tires, we will give you a 15 percent discount ({discount4:.2f}')
        buy = input('Would you like to buy this tire? (Y/N) ')
        
        ## Making the date look pretty
        current_day_now = datetime.now()
        day = current_day_now.day
        month = current_day_now.month
        if month < 10:
            month = f'0{month}'
        else:
            month = month
        year = current_day_now.year
        print()
        
        ## Getting phone number
        if buy.lower() == 'yes' or buy.lower() == 'y':
            phone = input('What is your phone number? ')
            with open('volume.txt', 'at') as volume_file:
                print(f'{year}-{month}-{day}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume3:.1f}, {phone}', file=volume_file)
                
            print('We will give you a call.')
            print('Thank you for your buisness. ')

            ## Give them a chance to quit
            fin = input('Are you finished? (Y/N) ')
            if fin.lower() == 'yes' or fin.lower() == 'y' or fin.lower() == 'quit':
                keep = 'quit'
            else:
                bob = 'bob'
        
        elif buy.lower() == 'quit':
            keep = 'quit'

        else:
            with open('volume.txt', 'at') as volume_file:
                print(f'{year}-{month}-{day}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume3:.1f}', file=volume_file)
            
            fin = input('Are you finished? (Y/N) ')
            if fin.lower() == 'yes' or fin.lower() == 'y' or fin.lower() == 'quit':
                keep = 'quit'
            else:
                bob = 'bob'
            
            
print()
print('Goodbye')
print()