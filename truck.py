import datetime


# Truck class with all trucks (truck 1, truck 2, truck 3) information
# Contains the truck ID, truck capacity, truck driver number, starting point, packages that are loaded into the truck,
# total miles calculated, package IDs (after calculating distances), departure time
class Truck:
    def __init__(self, truck_id, truck_capacity, truck_driver_number, starting_point,
                 packages_loaded_into_truck, total_miles, truck_package_ids, departure_time):
        self.truck_id = truck_id
        self.truck_capacity = truck_capacity
        self.truck_driver_number = truck_driver_number
        self.starting_point = starting_point
        self.packages_loaded_into_truck = packages_loaded_into_truck
        self.total_miles = total_miles
        self.truck_package_ids = truck_package_ids
        self.departure_time = departure_time

    # Returns the Truck's attributes in a string
    # Contains the truck ID, truck capacity, truck driver number, packages loaded into the truck, total miles,
    # package IDs after calculating the distances, departure time
    def __str__(self):
        return (f"(truck_id={self.truck_id}, truck_capacity={self.truck_capacity} "
                f"truck_driver_number={self.truck_driver_number}, truck_driver_number={self.starting_point}, "
                f"packages_loaded_into_truck={self.packages_loaded_into_truck} total_miles={self.total_miles}, "
                f"truck_package_ids={self.truck_package_ids})"
                f"departure_time={self.departure_time})")


# Truck 1 packages
# Holds 16 packages
# Packages 15, 19 must be delivered together
# Packages 13, 19 must be delivered together
# Packages 13, 15 must be delivered together
# Includes package 14, 16, 20
truck_one = Truck(1, 16, 1, 'HUB', [1, 7, 13, 14, 15, 16, 19, 20, 21, 26, 29, 31, 34, 39, 37, 30],
                  0, [], datetime.datetime(1900, 1, 1, 8, 0, 0))

# Truck 2 packages
# Holds 14 packages
# 3, 18, 36, 38 must be on truck 2
# Includes all delayed packages (arrives at 09:05:00) - 6, 25, 28, 32
truck_two = Truck(2, 14, 2, 'HUB', [2, 3, 4, 5, 8, 18, 33, 36, 38, 40, 32, 6, 25, 28],
                  0, [], datetime.datetime(1900, 1, 1, 9, 5, 0))

# Truck 3 packages
# Holds 10 packages
# Contains package 9 (address update)
truck_three = Truck(3, 10, 1, 'HUB', [10, 11, 12, 17, 22, 23, 24, 27, 35, 9],
                    0, [], datetime.datetime(1900, 1, 1, 10, 20, 0))

# List of truck 1, truck 2, and truck 3 in trucks list
trucks = [truck_one, truck_two, truck_three]
