# Python program to volume of a shape

from math import *
shapes = dict()
shapes['cone'] = ''
shapes['cube'] = ''
shapes['cylinder'] = ''
shapes['rectangular prism'] = ''
shapes['pyramid'] = ''
shapes['sphere'] = ''

while True:
    try:
        shape = input(
            "Insert the name of a 3D figure to find its surface area and volume: ").replace(' ', '')
    except ValueError:
        print("Invalid input")
        continue
    if shape == '?':
        print("Insert one of the following figures:")
        for key, value in shapes.items():
            print(key)
    elif shape.lower() not in shapes:
        print("Unregistered Figure. Enter one of the following shapes:")
        for key, value in shapes.items():
            print(key)
        continue
    if shape == 'whats a 3D figure':
        print("a 3D figure is a shape for example a cube or a cylinder it's a 3D shape")
    else:
        break
if shape.lower() == 'cone':
    h = float(input("What is the height of the cone? "))
    r = float(input("What is the radius of the cone? "))
    volume = (1/3 * pi * r**2 * h)
    surface_area = (pi * r * (r + sqrt(h**2 + r**2)))
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2),
          'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'cube':
    s = float(input("What is the length of one side of the cube? "))
    volume = (s**3)
    surface_area = (6 * s**2)
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))

if shape.lower() == 'cylinder':
    h = float(input("What is the height of the cylinder? "))
    r = float(input("What is the radius of the cylinder? "))
    volume = (pi * r**2 * h)
    surface_area = (2 * pi * r * h + 2 * pi * r**2)
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2),
          'or', round((surface_area/pi), 2), 'pi')

if shape.lower() == 'rectangular prism':
    l = float(input("What is the length of the prism? "))
    w = float(input("What is the width of the prism? "))
    h = float(input("What is the height of the prism? "))
    volume = (l * w * h)
    surface_area = (2 * l * w + 2 * (l + w) * h)
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))

if shape.lower() == 'pyramid':
    l = float(input("What is the length of the pyramid's base? "))
    w = float(input("What is the width of the pyramid's base? "))
    h = float(input("What is the height of the pyramid? "))
    volume = (l * w * h / 3)
    surface_area = ((l * w) + l * sqrt((w/2)**2 + h**2) +
                    w * sqrt((l/2)**2 + h**2))
    print("Volume:", round(volume, 2))
    print("Surface Area:", round(surface_area, 2))

if shape.lower() == 'sphere':
    r = float(input("What is the radius of the sphere? "))
    volume = (4 * pi * r**3 / 3)
    surface_area = (4 * pi * r**2)
    print("Volume:", round(volume, 2), 'or', round((volume/pi), 2), 'pi')
    print("Surface Area:", round(surface_area, 2),
          'or', round((surface_area/pi), 2), 'pi')

# https://github.com/Cloudy934/volume-and-surface-area-calculator/blob/master/volume%20and%20surface%20area.py
