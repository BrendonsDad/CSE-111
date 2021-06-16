from datetime import datetime
import time
current_date_and_time = datetime.now()
weekday = current_date_and_time.isoweekday()

if weekday == 2 or weekday == 4:
    print()
    print('Today is a special day!! On Tuesdays and Wednesday, you get a 50 percent \n discount if you spend over $50.00!')
    subtotal = float(input('What is the subtotal? '))
    if subtotal >= 50:
        discount = subtotal * .10
        newtotal = subtotal - discount
        tax = newtotal * .06
        total = newtotal + tax
        print()
        print(f'You saved ${discount:.2f}! Your subtotal was ${newtotal:.2f}, tax was ${tax:.2f} so your total comes to {total:.2f}')
        time.sleep(3)
        print()
        print('Thank you and have a nice day. ')

    else:
        tax = subtotal * .06
        total = subtotal + tax
        print()
        print(f'Your subtotal was ${subtotal:.2f} and tax was ${tax:.2f} which brings your total to ${total:.2f}')
        print()
        time.sleep(3)
        print('Thank you have a great day. ')

else:
    subtotal = float(input('What is the subtotal? '))
    tax = subtotal * .06
    total = subtotal + tax
    print()
    print(f'Your subtotal was ${subtotal:.2f} and tax was ${tax:.2f} which brings your total to ${total:.2f}')
    print()
    time.sleep(3)
    print('Thank you have a great day. ')



