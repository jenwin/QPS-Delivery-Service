import csv

# Get the distance_table.csv and assign to distance_data
# Allows access to the distance_table.csv file
distance_data = list(csv.reader(open('data/distance_table.csv')))


# The CompleteDistance constructor that contains the complete_distance_table function
class CompleteDistance:

    # Initiate a distance attribute for the CompleteDistance class
    def __init__(self, distance):
        self.distance = distance

    # The complete_distance_table takes a distance parameter
    # The function fills in the other half of the distance table (empty cells in the csv file)
    # complete_distance_table function is used to access the distance float values in the csv file
    # and return a full matrix table of the distances
    @staticmethod
    def complete_distance_table(distance):

        # Gets the length of the distance, stores length in a variable called n
        n = len(distance)
        # Initialize i with 0, to keep track of iteration in the while loops
        i = 0
        # Begins with the first while loop:
        # When variable i is less than length variable n. Variable i cannot be larger than the length n.
        while i < n:
            # 1 is added to variable i (begins at 0), increments i by 1 and stores it in x
            x = i + 1
            # Second while loop, inner loop: variable x is less than length variable n. Variable x cannot be
            # larger than the length n
            # The while loop will stop when it becomes greater than length n
            while x < n:
                # If true (x is less than length n)
                # Check if the cell value in the distance table [i][x] is empty and check if the cell value
                # in the distance table [x][i] is not empty
                if distance[i][x] == '' and distance[x][i] != '':
                    # If the condition is true, assign [x][i] cell value (contains a value in the cell)
                    # to the [i][x] cell (empty cell) in the distance table
                    distance[i][x] = distance[x][i]
                # If the [i][x] is not empty and the [x][i] is empty in the distance table
                elif distance[i][x] != '' and distance[x][i] == '':
                    # If the condition is true, assign the distance value from [i][x] (contains a value in the cell)
                    # to the empty cell [x][i] in the distance table
                    # Empty cells are filled with data to create a two-dimensional matrix
                    distance[x][i] = distance[i][x]
                # Incrementing x by 1
                x += 1
            # Incrementing x by 1
            i += 1
        # Returns the completed filled distance table
        # A full completed matrix is the result of the complete_distance_table function
        return distance


# Create an instance of CompleteDistance and assign to distance_instance
distance_instance = CompleteDistance(distance_data)
# Call the complete_distance_table function with distance_data that contains the data/distance_table.csv information
# Assign to filled_distance variable
filled_distance = distance_instance.complete_distance_table(distance_data)
