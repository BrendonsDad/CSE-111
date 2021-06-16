import math

def main():
        can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]
        n = 'NAME'
        r = 'RADIUS'
        h = 'HEIGHT'
        c = 'COST'
        ce = 'COST EFNCY'
        print()
        print(f'{n:11} {r:10} {h:10} {c:10} {ce:10}')
        for name, radius, height, cost, in can_sizes:
            volume = cylinder_volume(radius, height)
            surface_area = cylinder_surface_area(radius, height)
            storage_effective = storage_efficiency(volume, surface_area)

            new_cost = str(cost)
            nnew_cost = '$' + new_cost
            
            print()
            print(f'{name:11} {radius:<10} {height:<7} {nnew_cost:>7}    SE: {storage_effective:>.1f}')

def cylinder_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def storage_efficiency(volume, surface_area):
    storage_effec = volume / surface_area
    return storage_effec


main()