
def miles_per_gallon(start_miles, end_miles, amount_gallons):

    mpg = abs(end_miles - start_miles) / amount_gallons

    return mpg
    

def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg

    return lp100k



def main():
    print('Hello, please enter the following info: ')
    start_odometer = float(input('Starting odometer in miles: '))
    end_odometer = float(input('Ending odometer in miles: '))
    fuel = float(input('Amount of fuel in gallons: '))

    mpg = miles_per_gallon(start_odometer, end_odometer, fuel)

    lp100k = lp100k_from_mpg(mpg)

    print(f'{mpg:.1f} is the miles per gallon and the liters per 100km is {lp100k:.2f}')
    pass



main()