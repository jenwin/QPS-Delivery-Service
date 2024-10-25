import csv

# Initialize an empty dictionary for the address_book
address_book = {}


# get_address_book function
# Gets the addresses in the addressesCSV.csv file
def get_address_book():
    # Opens the addressesCSV.csv file and provides it with an alias called address_csv_file
    with open('data/addressesCSV.csv') as address_csv_file:
        # Use csv reader to read the addressesCSV.csv file
        address_csv_reader = csv.reader(address_csv_file)

        # For loop, iterates over the addressesCSV.csv file
        # Get the package_ids (as integers), assign to package_id variable
        # Get the addresses, assign to address variable
        for address_row in address_csv_reader:
            package_id = int(address_row[0])
            address = address_row[1]
            # Place the address in the address_book with the package ID as the key
            address_book[package_id] = address


# Call the get_address_book function to run the function
# The address_book contains the package ID as the key and the address as the value
get_address_book()
