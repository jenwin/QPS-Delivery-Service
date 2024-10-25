import csv

from complete_distance_table import filled_distance

# Allows access to the package_data.csv, assign to package_data
package_data = list(csv.reader(open('data/package_data.csv')))


# Function to convert filled_distance (matrix) data to a dictionary for extraction
# Uses the filled_distance variable from complete_distance_table function
def convert_to_distance_dictionary(completed_distance_table):
    # Initialize the addresses_distances with an empty dictionary
    addresses_distances = {}

    # Skips index 0 (contains header information) in the complete_distance_table csv file
    # Begins at index 1 in the complete_distance_table csv file
    header = completed_distance_table[0][1:]

    # Outer for loop: Loops over the rest of the distance filled csv file
    # Begins at index 1 and retrieves data after it
    for distance_row in completed_distance_table[1:]:

        # Extracts the first row of the distance filled csv file (index 0)
        # Removes whitespace from the extracted data with .strip()
        # Assigns the extracted data into the cell variable
        cell = distance_row[0].strip()

        # Create an empty dictionary to store key-value pairs (addresses and distances)
        # cell is used as the key for the addresses_distances dictionary
        addresses_distances[cell] = {}

        # Inner for loop: Loops through the distance_rows starting at index 1 using enumerate
        for index, distance in enumerate(distance_row[1:]):
            # If the distance in the cell exists (true) assign the addresses_distances with the distance (float)
            # The cell is used as a key to access the addresses_distances dictionary
            # The header is used as a key to access an inner dictionary within the addresses_distances dictionary
            # The index is the current index and is used to access the distance float value in the distance table
            if distance:
                addresses_distances[cell][header[index]] = float(distance)
            # If false, addresses_distances dictionary is assigned None (null)
            else:
                addresses_distances[cell][header[index]] = None

    # Returns the addresses_distances dictionary
    return addresses_distances


# Call the convert_to_distance_dictionary with filled_distance, assign to distance_dict
distance_dict = convert_to_distance_dictionary(filled_distance)


# get_the_distance function retrieves the distance between two addresses from the distance csv file
# The function takes two parameters: current_address and delivery_address
# The current address is the current location and the delivery address is the destination location
def get_the_distance(current_address, delivery_address):
    # If the current address exists (true) in distance_dict (the dictionary created when converting the distance
    # table matrix to a dictionary)
    # And if the delivery_address of the package is accessible in the distance_dict with the key current_address
    if current_address in distance_dict and delivery_address in distance_dict[current_address]:
        # If both conditions are true, return the distance_dict with current_address (x) and delivery_address (y)
        # from the cell in the distance csv file
        # get_the_distance function returns a float number (distance)
        return distance_dict[current_address][delivery_address]
    # If false, return None (null)
    else:
        return None
