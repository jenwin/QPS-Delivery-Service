# nearest neighbor function
import datetime
from distance import get_the_distance


# Function find_the_nearest_distances_for_routes
# Parameters include: address_book, truck
# address_book contains the package IDs and delivery addresses
# truck allows access to the truck object
def find_the_nearest_distances_for_routes(address_book, truck):
    # the current address is the starting point of the route
    current_address = truck.starting_point
    # Initialize an empty routes list for addresses, holds routes data
    routes = []
    # Initialize an empty dictionary for delivery_times, holds delivery times data
    delivery_times = {}
    # remaining_addresses holds the package ids, which has access to delivery addresses
    remaining_addresses = truck.packages_loaded_into_truck
    # Append the current address to the routes list
    # When the current route (address) is visited, add to the routes list
    routes.append(current_address)
    # Initialize an empty list for package_ids
    package_ids = []
    # Initialize an empty list for nearest_package_id
    # Holds the data for package IDs that are the nearest during travel
    nearest_package_id = []

    # Begin while loop
    # Check if the remaining addresses contain package IDs
    # The length must be greater than or equal to 1
    # The while loop won't run if it is empty
    # If empty, it means there are no package IDs left in the list
    while len(remaining_addresses) >= 1:
        # Keep track of the nearest distance and nearest address
        # Nearest distance is set to a large number, set to 999.99
        nearest_distance = 999.99
        # Nearest address is assigned to None (null)
        nearest_address = None

        # For loop: Iterate over the remaining addresses
        for package_id in remaining_addresses:
            # Access the address book with the package_id variable
            # Assign to delivery address list (contains a list of delivery addresses)
            delivery_address_list = address_book[package_id]

            # Call the get_the_distance function with the current address and the delivery address list
            # The delivery address list allows access to all delivery addresses of the package IDs
            # Assign the obtained distance from the get_the_distance function to distance variable
            distance = get_the_distance(current_address, delivery_address_list)

            # If the current distance value is less than the nearest distance value
            if distance < nearest_distance:
                # If true, assign the current distance (distance variable) to the new distance (nearest_distance
                # variable)
                nearest_distance = distance
                # If true, assign the current delivery address (from the delivery_address_list) as the new address
                # into the nearest address variable
                nearest_address = delivery_address_list
                # If true, assign the current package ID (package_id) to the new package ID (nearest package id)
                # nearest_package_id contains the nearest package ids based on distance from one point to the next
                nearest_package_id = package_id

        # If the nearest address is not None (not null), meaning it contains a value
        if nearest_address is not None:
            # Append the nearest address and nearest package id to the routes list
            # Routes was empty, now contains nearest_address and nearest_package_id
            routes.append((nearest_address, nearest_package_id))

            # If the nearest_package_id is in the remaining_addresses
            if nearest_package_id in remaining_addresses:
                # If true, find the nearest_package_id in the remaining_addresses with .index() method
                # The .index() method gets the index of the nearest_package_id in the remaining_addresses
                # The index retrieved is stored in the removed_package_id variable
                removed_package_id = remaining_addresses.index(nearest_package_id)
                # Remove the index using .pop() method
                remaining_addresses.pop(removed_package_id)
                # Store the popped nearest_package_id into the package_ids (visited package IDs)
                # package_ids holds package IDs in nearest order
                package_ids.append(nearest_package_id)

            # Calculate total truck miles
            truck.total_miles += nearest_distance
            # Calculate the delivery time for each package based on total miles
            # The average truck speed is 18 MPH (miles per hour), assign to delivery_time
            delivery_time = truck.departure_time + datetime.timedelta(hours=(truck.total_miles / 18))

            # If the nearest_package_id is not in delivery_times
            if nearest_package_id not in delivery_times:
                # delivery_times object with nearest package ID, truck ID, delivery time, departure time
                delivery_times[nearest_package_id] = {
                    truck.truck_id: {
                        'delivery_time': delivery_time,
                        'departure_time': truck.departure_time
                    }
                }
        # Assigns the nearest address to the current address, gets updated with the new nearest address
        current_address = nearest_address

    # Returns package_ids and delivery_times
    return package_ids, delivery_times
