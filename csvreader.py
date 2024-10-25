import csv

from hashtable import hash_table
from package import PackageData

# Use csv reader to open and access the package_data.csv file
# Give the package_data.csv file an alias called csv_package_data
with open('data/package_data.csv') as csv_package_data:
    # CSV reader reads csv_package_data
    # Assigns the data to the csv_package_data_files variable
    csv_package_data_files = csv.reader(csv_package_data)

    # The next() function skips the header row in the csv file
    # It moves on to the data in the csv file after the header row
    next(csv_package_data_files)

    # For loop is used to iterate over each row in the csv_package_data_files
    # Data includes: package_id, address, city, state, zip_code, deadline, weight, notes, status, delivery_timestamps,
    # truck_id, and departure times
    # The status is given a default string "At HUB and loaded"
    for package_row in csv_package_data_files:
        package_id = int(package_row[0])
        address = package_row[1]
        city = package_row[2]
        state = package_row[3]
        zip_code = package_row[4]
        deadline = package_row[5]
        weight = float(package_row[6])
        notes = package_row[7]
        status = "At HUB and loaded"
        delivery_timestamps = ""
        truck_id = ""
        departure = ""

        # The PackageData contains parameters: package_id, address, city, state, zip_code, deadline,
        # weight, notes, status, delivery_timestamps, truck_id, and departure times
        # The parameters are loaded with data from extracting the package_data.csv file
        # The data is assigned to package_items variable
        package_items = PackageData(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                                    delivery_timestamps, truck_id, departure)

        # Hash table insertion function
        # Use the insert_package function to add package_id and package_items into the hash_table
        hash_table.insert_package(package_id, package_items)
