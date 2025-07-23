from datetime import datetime
from csvreader import hash_table
from nearest_distance import find_the_nearest_distances_for_routes
from package_addresses import address_book
from truck import truck_one, truck_two, truck_three, trucks

# Truck 1, 2, 3 data
truck_objects = [find_the_nearest_distances_for_routes(address_book, truck_one),
                 find_the_nearest_distances_for_routes(address_book, truck_two),
                 find_the_nearest_distances_for_routes(address_book, truck_three)]

# Get the data from truck objects: package_ids, delivery_times
for truck_items in truck_objects:
    package_ids, delivery_times = truck_items
    # Iterate over package_ids, contains all package ids from each truck
    for package_id in package_ids:
        # Use the hash table lookup function to get the packages
        packages = hash_table.lookup_package(package_id)
        if packages is not None:
            # Checks if the package_id exists in the delivery_times
            if package_id in delivery_times:
                # Assign the delivery times based on the package_id to delivery_times_data
                delivery_times_data = delivery_times[package_id]
                # Get the truck_id and delivery times information
                for truck_id, data in delivery_times_data.items():
                    # Check if the data is a dictionary first
                    if isinstance(data, dict):
                        # If it is a dictionary, get the delivery_time and departure time data
                        delivery_time = data.get('delivery_time')
                        departure_time = data.get('departure_time')
                        # Add delivery_time, truck_id, and departure_time to the packages
                        packages.add_delivery_timestamps(delivery_time)
                        packages.add_truck_id(truck_id)
                        packages.add_departure_time(departure_time)
            # Error message when package is not found
            else:
                print(f"The package cannot be found.")
        # Error message when package is not found
        else:
            print(f"The package cannot be found")


# Function display_a_package_with_time
# Display a package with a specific time (HH:MM:SS)
# Example package ID: 1
# Example specific time: 08:00:00
# Use 24-hour clock
def display_a_package_with_time():
    # Begin while loop, while true...
    while True:
        # Package ID entered by user must be an integer from 1-40
        # Assign to user_package_id_input
        user_package_id_input = int(input("Enter package ID (1-40): "))

        # Check if the user inputs a valid package ID from 1-40
        # Prints an error message to the user if the integer is incorrect
        if user_package_id_input not in range(1, 41):
            print("Package ID entered invalid. Enter a package ID from 1-40.")
            # Exits the program
            exit()

        # User time input (HH:MM:SS), assigned to user_time_input variable
        # Example time input: 08:00:00
        # Datetime formatted and assigned to user_time_input_formatted
        user_time_input = input("Enter time (HH:MM:SS): ")
        user_time_input_formatted = datetime.strptime(user_time_input, "%H:%M:%S")

        # Checks if the time input is in a valid format (HH:MM:SS)
        # Prints an error message if input is incorrect
        if len(user_time_input.split(':')) != 3:
            print("Invalid time format. Please enter the time in HH:MM:SS format.")
            # Exits the program
            exit()

        # Print the header for the interface
        # The header contains the truck ID, package ID, address, city, state, zip code, weight, deadline, status,
        # and delivery time
        print(f"{'Truck ID':<10} {'Package ID':<15} {'Address':<40} {'City':<20} {'State':<10} {'Zip Code':<10} "
              f"{'Weight (kg)':<15} {'Deadline':<15} {'Status / Delivery Time':<25}")

        # Package lookup function: Use the package lookup function to access the hash table to print package details
        # The lookup package function takes the user_package_id_input (package ID integer entered by the user) and
        # retrieves the package ID data
        package_lookup = hash_table.lookup_package(int(user_package_id_input))

        # Change the package statuses with change_package_status function
        package_lookup.change_package_status(user_time_input_formatted)

        # Datetime format of delivery_timestamps
        delivery_timestamps_formatted = package_lookup.delivery_timestamps.strftime("%H:%M:%S")
        # Print the package ID, weight, deadline, status, delivery timestamps, truck number, notes
        p_id = f"{package_lookup.package_id}"
        weight = f"{package_lookup.weight}"
        deadline = f"{package_lookup.deadline}"
        status = f"{package_lookup.status}"
        delivery_timestamps = f"{delivery_timestamps_formatted}"
        truck_number = f"{package_lookup.truck_id}"
        notes = f"{package_lookup.notes:}"

        # Call the change_package_nine_address function with user_time_input_formatted
        # Assign to address, city, state, zip_code
        address, city, state, zip_code = package_lookup.change_package_nine_address(user_time_input_formatted)

        # Print the values to the interface
        print(f"{truck_number:<10} {p_id:<15} {address:<40} {city:<20} {state:<10} {zip_code:<10} "
              f"{weight:<15} {deadline:<15} {status:<15} {delivery_timestamps} by Truck {truck_number:<10}")
        print(f"{'Notes:':<10} {notes}")

        # Allows user to search for another package
        # Enter lowercase y to search for another package
        # Enter any other key (e.g. n) to exit the package search
        keep_searching = input("Find another package? Enter lowercase y. Enter any other key to exit. (e.g. "
                               "lowercase n)")
        # User enters lowercase y to search for another package
        # If the user enters any other key besides lowercase y, it exists the while loop
        if keep_searching.lower() != 'y':
            # breaks out of the loop, prints an exiting message to the user
            print("Goodbye.")
            break
        else:
            # Continues the loop
            pass


# Function to display all packages from all three trucks (truck 1, truck 2, truck 3)
# Use 24-hour clock
def display_all_packages_with_time():
    # User time input (HH:MM:SS), assigned to user_time_input variable
    # Datetime formatted, assigned to user_time_input_formatted
    user_time_input = input("Enter time (HH:MM:SS): ")
    user_time_input_formatted = datetime.strptime(user_time_input, "%H:%M:%S")

    # Checks if the time input is in a valid format (HH:MM:SS)
    if len(user_time_input.split(':')) != 3:
        # Prints error message to the user
        print("Invalid time format. Please enter the time in HH:MM:SS format.")
        # Exits the program
        exit()

    # Header to structure the interface
    print("-" * 250)

    # For loop iterates over trucks with variable t to get the miles for each truck
    # lowercase t is for truck
    # Sum of all trucks, assigned to total_miles_sum
    total_miles_sum = sum(t.total_miles for t in trucks)

    # Print the header labels: Package ID, Address, City, State, Zip Code, Weight, Deadline, Delivery Time,
    # Status, and Notes
    print(f"{'Package ID':<10} {'Address':<40} {'City':<20} {'State':<10} {'Zip Code':<10} "
          f"{'Weight (kg)':<12} {'Deadline':<15} {'Delivery Time':<20} {'Status':<30} {'Notes'}")

    # Package lookup function: Use the lookup function to access the hash table to print package details
    for package_details in range(1, 41):
        # The package lookup function takes the package ID and retrieves package data
        package_lookup = hash_table.lookup_package(package_details)

        # Change the package statuses with change_package_status function
        package_lookup.change_package_status(user_time_input_formatted)

        # Datetime format of delivery_timestamps
        delivery_timestamps_formatted = package_lookup.delivery_timestamps.strftime("%H:%M:%S")
        # Print the package ID, weight, deadline, status, delivery timestamps, truck number, notes
        truck_number = f"{package_lookup.truck_id:<10}"
        p_id = f"{package_lookup.package_id:<10}"
        weight = f"{package_lookup.weight:<10}"
        deadline = f"{package_lookup.deadline:<15}"
        status = f"{package_lookup.status:<15}"
        delivery_timestamps = f"{delivery_timestamps_formatted}"
        notes = f"{package_lookup.notes:}"

        # Call the change_package_nine_address function with user_time_input_formatted
        # Assign to address, city, state, zip_code
        address, city, state, zip_code = package_lookup.change_package_nine_address(user_time_input_formatted)

        # Print the values to the interface
        print(f"{p_id:<10} {address:<40} {city:<20} {state:<10} {zip_code:<10} {weight:<12} "
              f"{deadline:<15} {delivery_timestamps:<20} {status:<15} by Truck {truck_number:<15} "
              f"{notes}")

    # Sections out the package information in the interface
    print("-" * 250)
    # Print the total miles for all trucks (truck 1, truck 2, truck 3 total)
    print(f"{'Total Miles for All Trucks:':<20} {total_miles_sum:.2f} miles")
    # Sections out the package information in the interface
    print("-" * 250)


def display_total_truck_miles():
    # Initialize a total_sum_miles variable to 0, used to add the miles up
    total_sum_miles = 0
    # For loop iterates over trucks with variable t to get the miles for each truck
    # lowercase t is for truck
    for t in trucks:
        # Get the total miles and truck IDs
        miles = t.total_miles
        t_id = t.truck_id
        print(f"Truck {t_id}: {miles:.2f} miles")
        # Add the miles of each truck to total_sum_miles
        total_sum_miles += miles
        # Sum of all trucks, stored in total_miles_sum
    print(f"Total miles for all trucks: {total_sum_miles:.2f} miles")


# Uses 24-hour clock
# Display truck and package progress with an interactive interface
# 1. Consists of a menu selection to display a package at a specific time (Type 1)
# 2. Consists of a menu selection to display all packages at a specific time (Type 2), includes total truck mileage
# 3. A menu selection to see total miles of all trucks only
# 4. A menu selection to quit the interactive interface (Type 4)
print("Welcome to the QPS Package Delivery System!")
print("\nDelivery Status Menu:")
print("1. Check a package with time. Enter package ID. Enter specific time (e.g. 08:00:00)")
print("2. Check ALL packages with time. Enter specific time (e.g. 08:00:00)")
print("3. Check the total miles of all trucks")
print("4. Exit")
# actions include typing 1, 2, 3, 4
action = input("Menu: Choose 1, 2, 3, or 4: ")
# Exits the program if user enters other values instead of 1, 2, 3, 4
if action not in ["1", "2", "3", "4"]:
    # Error message to the user
    print("Sorry, invalid input.")
    # Exits the program
    exit()

# Action 1: Calls the display_a_package_with_time function to run and display a package's details
# Action 2: Calls the display display_all_packages_with_time function to run and display all package's details
# Action 3: Calls the display_total_truck_miles function to run and display the total miles of all trucks
# Action 4: Exits the program. Prints Goodbye to the user.
if action == '1':
    display_a_package_with_time()
elif action == '2':
    display_all_packages_with_time()
elif action == '3':
    display_total_truck_miles()
elif action == '4':
    print("Goodbye.")
else:
    # If the input is not valid, shows an error message to the user.
    print("Sorry, invalid input.")
