import sys

# Comparing tuple and list. The main difference is tuple uses less memory to store information, however we should use it only if we are sure we won't add any additional key and it's a fixed structure that should remain constant and list when you need a flexible collection of items that will change over time

def main():
    coordinate_tuple = (42.376, -71.155)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

"""
def main():
    coordinates = (42.376, -71.111)
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

            # OR
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

    # latitude = 42.376
    # longitude = -71.111

"""


main()

