# Package
import datetime


# PackageData class with package information
# Contains package ID, address, city, state, zip code, deadline, weight, notes, status, delivery time stamps,
# truck ID, departure time
class PackageData:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, delivery_timestamps,
                 truck_id, departure):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_timestamps = delivery_timestamps
        self.truck_id = truck_id
        self.departure = departure

    # change_package_nine_address function
    # Update package ID 9 to the correct address at 10:20 AM
    # Current address: 300 State St, Salt Lake City, UT 84103
    # Correct address: 410 S. State St., Salt Lake City, UT 84111
    def change_package_nine_address(self, user_time_input_formatted):
        # Get the datetime for package ID 9, 10:20:00 is the time that the address for package ID 9 will change to
        # the correct address: 410 S. State St., Salt Lake City, UT 84111
        # Assign to the_new_time_for_nine variable
        the_new_time_for_nine = datetime.datetime.strptime("10:20:00", "%H:%M:%S")

        # Checks to see if the package_id is equal to 9
        if self.package_id == 9:
            # If user's time input is >= to 10:20:00 (the_new_time_for_nine)
            # Set package 9's address to 410 S. State St., Salt Lake City, UT 84111
            if user_time_input_formatted >= the_new_time_for_nine:
                self.address = "410 S State St."
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zip_code = "84111"
            # Keep the address 300 State St, Salt Lake City, UT 84103
            else:
                self.address = "300 State St"
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zip_code = "84103"

        # Return the new address, city, state, zip code
        return self.address, self.city, self.state, self.zip_code

    # Add delivery timestamps
    def add_delivery_timestamps(self, timestamps):
        self.delivery_timestamps = timestamps

    # Add truck IDs
    def add_truck_id(self, truck_id):
        self.truck_id = truck_id

    # Add departure times
    def add_departure_time(self, time):
        self.departure = time

    # Change the package status: At the HUB, En route, Delivered
    def change_package_status(self, user_time_input_formatted):
        # Delivered if user's input is >= than the delivery time
        if user_time_input_formatted >= self.delivery_timestamps:
            self.status = "Delivered"
        # En route departure time is <= than the user's input
        # Also if the user's input is < the delivery time
        elif self.departure <= user_time_input_formatted < self.delivery_timestamps:
            self.status = "En route"
        # At the HUB if user's input is < the departure time
        elif user_time_input_formatted < self.departure:
            self.status = "At the HUB"
        else:
            self.status = "Delivered"

    # Returns the PackageData's attributes in a string
    # It includes the package_id, address, city, state, zip code, deadline, weight, status, notes, delivery
    # timestamps, truck_id, and departure times
    def __str__(self):
        return (
            f"package_id={self.package_id}, address={self.address}, city={self.city}, state={self.state}, "
            f"zip_code={self.zip_code}, deadline={self.deadline}, weight={self.weight}, "
            f"status={self.status} notes={self.notes} delivery_timestamps={self.delivery_timestamps}"
            f"truck_id={self.truck_id} departure={self.departure}"
        )
