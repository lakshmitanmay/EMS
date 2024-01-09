import mysql.connector as my
import random

f = 0
if f == 0:
    mycon0 = my.connect(host='localhost', user='root', password='admin*6798')
    cursor = mycon0.cursor()
    sql_query = "Create database if not exists ems;"
    cursor.execute(sql_query)
    mycon0.commit()
    f = 1
mycon = my.connect(host='localhost', user='root', password='admin*6798', database='ems')
if not mycon.is_connected():
    print("Error connecting to MySQL database.")
cursor = mycon.cursor()
sql_query = "create table users (username varchar(255), password varchar(255))"
cursor.execute(sql_query)
mycon.commit()


def register_user():
    print("╔═════════════════════════╗")
    print("║        REGISTER         ║")
    print("╚═════════════════════════╝")
    print("Please enter your credentials for registration or enter 0 to exit")
    username = input("Enter New Username: ")
    if username == '0':
        print("\ngoing back to previous screen \n")
        return
    password = input("Enter New Password: ")
    if password == '0' or username == '0':
        print("\ngoing back to previous screen \n")
        return
    else:
        user_pass = (username, password)
        cursor.execute("Select * from users;")
        result = cursor.fetchall()
        for i in result:
            if i == user_pass:
                print("\nUser Already Registered, please try again\n")
                register_user()
        sql_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql_query, user_pass)
        mycon.commit()
        print("User Registered Successfully! \nLogin with the credentials you created to start using this EMS! "
              "\ngoing back to previous screen \n")
        event_table_name = 'event_' + username
        inventory_table_name = 'inventory_' + username
        staff_table_name = 'staff_' + username
        transport_table_name = 'transport_' + username
        venue_table_name = 'venue_' + username
        attendees_table_name = 'attendees_' + username
        sql_query2 = "create table {} (`Event ID` INT NOT NULL PRIMARY KEY, `Event Name` VARCHAR(255), `Event Date` Date,  `Event Start Time` Time, `Event End Time` Time, `Event Location` VARCHAR(255), `Event Description` VARCHAR(255), `Event Type` VARCHAR(255), `Event Status` VARCHAR(255), `Event Max Capacity` INT, `Event Ticket Price` INT)".format(
            event_table_name)
        cursor.execute(sql_query2)
        sql_query3 = "create table {} (`Event ID` INT References {}, `Item Name` VARCHAR(255), Quantity INT, Availability Varchar(255))".format(
            inventory_table_name, event_table_name)
        cursor.execute(sql_query3)
        sql_query4 = "create table {} (`Event ID` INT References {}, `Staff Name` VARCHAR(255), `Staff Role` varchar(255), `Staff Contact` VARCHAR(255))".format(
            staff_table_name, event_table_name)
        cursor.execute(sql_query4)
        sql_query5 = "create table {} (`Event ID` INT References {}, `Vehicle Name` VARCHAR(255), Route VARCHAR(255), Schedule VARCHAR(255), `Driver Name` VARCHAR(255))".format(
            transport_table_name, event_table_name)
        cursor.execute(sql_query5)
        sql_query6 = "create table {} (`Event ID` INT References {}, `Venue Name` VARCHAR(255), `Venue Address` VARCHAR(1000), Capacity INT, Availability Varchar(255))".format(
            venue_table_name, event_table_name)
        cursor.execute(sql_query6)
        sql_query7 = "create table {} (`Event ID` INT References {}, `Attendee Name` VARCHAR(255), `Attendee Email` VARCHAR(255), `Attendee Phone Number` BIGINT)".format(
            attendees_table_name, event_table_name)
        cursor.execute(sql_query7)
        mycon.commit()


def login_user():
    print("╔════════════════════════╗")
    print("║         LOGIN          ║")
    print("╚════════════════════════╝")
    print("Please enter your credentials for Login or enter 0 to exit")
    username = input("Enter Username: ")
    if username == '0':
        print("\ngoing back to previous screen \n")
        return None, None
    password = input("Enter Password: ")
    if password == '0' or username == '0':
        print("\ngoing back to previous screen \n")
        return None, None
    user_pass = (username, password)
    sql_query = "SELECT * FROM users WHERE username = %s and password = %s"
    cursor.execute(sql_query, user_pass)
    result = cursor.fetchone()
    if result:
        if result == user_pass:
            print("Login successful!")
            print("Welcome User", username, '\n')
            return True, username
    else:
        print("Invalid credentials. Please try again.\n")
        login_user()


def close_connection():
    mycon.close()
    if not mycon.is_connected():
        print("Successfully disconnected from database backend")
    else:
        print("Unable to disconnect from database backend.")


def display_all_events(table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Event', count)
        print('Event ID:', row[0])
        print('Event Name:', row[1])
        print('Event Date:', row[2])
        print('Event Start Time:', row[3])
        print("Event End Time:", row[4])
        print('Event Location:', row[5])
        print('Event Description:', row[6])
        print('Event Type:', row[7])
        print('Event Status:', row[8])
        print('Event Max Capacity:', row[9])
        print('Event Ticket Price:', row[10])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def add_event(table_name):
    print()
    print('The event id for this event will be auto-generated')
    print("Enter 0 at any time to go back")
    event_name = input("Enter event name: ")
    if event_name == "0":
        print("\ngoing back to previous screen \n")
        return
    event_date = input("Enter event date: ")
    if event_date == "0":
        print("\ngoing back to previous screen \n")
        return
    event_start_time = input("Enter event start time: ")
    if event_start_time == "0":
        print("\ngoing back to previous screen \n")
        return
    event_end_time = input("Enter event end time: ")
    if event_end_time == "0":
        print("\ngoing back to previous screen \n")
        return
    event_location = input("Enter event location: ")
    if event_location == "0":
        print("\ngoing back to previous screen \n")
        return
    event_description = input("Enter event description: ")
    if event_description == "0":
        print("\ngoing back to previous screen \n")
        return
    event_type = input("Enter event type: ")
    if event_type == "0":
        print("\ngoing back to previous screen \n")
        return
    event_status = input("Enter event status (scheduled on time, canceled, completed): ")
    if event_status == "0":
        print("\ngoing back to previous screen \n")
        return
    event_max_capacity = int(input("Enter event max capacity of attendees: "))
    if event_max_capacity == 0:
        print("\ngoing back to previous screen \n")
        return
    event_ticket_price = int(input("Enter event ticket price: "))
    if event_ticket_price == 0:
        print("\ngoing back to the previous screen \n")
        return

    while True:
        event_id = random.randint(100000, 999999)
        sql_query1 = f"SELECT * FROM `{table_name}` WHERE `Event ID` = '{event_id}'"
        cursor.execute(sql_query1)
        result = cursor.fetchall()
        if result:
            print('Event already exists, please try again!')
            add_event(table_name)
        else:
            break

    sql_query = f"INSERT INTO `{table_name}` (`Event ID`, `Event Name`, `Event Date`, `Event Start Time`, `Event End Time`, `Event Location`, `Event Description`, `Event Type`, `Event Status`, `Event Max Capacity`, `Event Ticket Price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql_query, (
        event_id, event_name, event_date, event_start_time, event_end_time, event_location, event_description,
        event_type,
        event_status, event_max_capacity, event_ticket_price))
    mycon.commit()
    print("Successfully added event details to the database.")
    print("\ngoing back to previous screen \n")


def update_event(table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the event you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    event_name = input("Enter New event name: ")
    if event_name == '0':
        print("\ngoing back to previous screen \n")
        return
    event_date = input("Enter New event date: ")
    if event_date == '0':
        print("\ngoing back to previous screen \n")
        return
    event_start_time = input("Enter New event start time: ")
    if event_start_time == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_end_time = input("Enter New event end time: ")
    if event_end_time == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_location = input("Enter New event location: ")
    if event_location == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_description = input("Enter New event description: ")
    if event_description == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_type = input("Enter New event type: ")
    if event_type == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_status = input("Enter New event status (scheduled on time, canceled, completed): ")
    if event_status == '0':
        print("\ngoing back to the previous screen \n")
        return
    event_max_capacity = int(input("Enter New event max capacity of attendees: "))
    if event_max_capacity == 0:
        print("\ngoing back to the previous screen \n")
        return
    event_ticket_price = int(input("Enter New event ticket price: "))
    if event_ticket_price == 0:
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{table_name}` SET `Event Name` = %s, `Event Date` = %s, `Event Start Time` = %s, `Event End Time` = %s, `Event Location` = %s, `Event Description` = %s, `Event Type` = %s, `Event Status` = %s, `Event Max Capacity` = %s, `Event Ticket Price` = %s where `Event ID` = %s"
    cursor.execute(sql_query, (
        event_name, event_date, event_start_time, event_end_time, event_location, event_description, event_type,
        event_status, event_max_capacity, event_ticket_price, event_id))
    mycon.commit()
    print("Event Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_event(table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = input("Enter Event ID: ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Event and its details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_event(table_name):
    print()
    table_name = table_name
    event_id = input("Enter Event ID of the event (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchone()
        if row:
            print("Event Found\n")
            what_to_show = input("What would you like to see from this event? (Type all to see all details): ")
            if what_to_show == "Event Name":
                print('Event Name:', row[1])
            elif what_to_show == "Event Date":
                print('Event Date:', row[2])
            elif what_to_show == "Event Start Time":
                print('Event Start Time:', row[3])
            elif what_to_show == "Event End Time":
                print("Event End Time:", row[4])
            elif what_to_show == "Event Location":
                print('Event Location:', row[5])
            elif what_to_show == "Event Description":
                print('Event Description:', row[6])
            elif what_to_show == "Event Type":
                print('Event Type:', row[7])
            elif what_to_show == "Event Status":
                print('Event Status:', row[8])
            elif what_to_show == "Event Max Capacity":
                print('Event Max Capacity:', row[9])
            elif what_to_show == "Event Ticket Price":
                print('Event Ticket Price:', row[10])
            elif what_to_show == "all":
                print('Event Name:', row[1])
                print('Event Date:', row[2])
                print('Event Start Time:', row[3])
                print("Event End Time:", row[4])
                print('Event Location:', row[5])
                print('Event Description:', row[6])
                print('Event Type:', row[7])
                print('Event Status:', row[8])
                print('Event Max Capacity:', row[9])
                print('Event Ticket Price:', row[10])
                print("Here is the event and its details in tuple form:", row)
        else:
            print("Event not found, please try again")
            search_event(table_name)
    print("\ngoing back to previous screen \n")


def add_inventory(inventory_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    item_name = input("Enter inventory item name: ")
    if item_name == "0":
        print("\ngoing back to previous screen \n")
        return
    quantity = int(input("Enter item quantity: "))
    if quantity == "0":
        print("\ngoing back to previous screen \n")
        return
    availability = int(input("Enter availability status (00 for unavailable, 01 for available): "))
    if availability == 0:
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"INSERT INTO `{inventory_table_name}` (`Event ID`, `Item Name`, `Quantity`, `Availability`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_query, (event_id, item_name, quantity, availability))
    mycon.commit()
    print("Successfully added inventory details to the database.")
    print("\ngoing back to previous screen \n")


def display_inventory(inventory_table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{inventory_table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Inventory', count)
        print('Event ID:', row[0])
        print('Item Name:', row[1])
        print('Quantity:', row[2])
        print('Availability:', row[3])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def update_inventory(inventory_table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the inventory you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    item_name1 = input("Enter the old Item Name of the inventory you want to update:")
    if item_name1 == '0':
        print("\ngoing back to previous screen \n")
        return
    item_name = input("Enter New Item name: ")
    if item_name == "0":
        print("\ngoing back to previous screen \n")
        return
    quantity = input("Enter New Quantity of the Item: ")
    if quantity == "0":
        print("\ngoing back to previous screen \n")
        return
    availability = input("Enter New Availability Status of the Item: ")
    if availability == "0":
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{inventory_table_name}` SET `Item Name` = %s, `Quantity` = %s, `Availability` = %s where `Event ID` = %s and `Item Name` = %s"
    cursor.execute(sql_query, (item_name, quantity, availability, event_id, item_name1))
    mycon.commit()
    print("Inventory Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_inventory(inventory_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    item_name1 = input("Enter the Item Name:")
    if item_name1 == '0':
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{inventory_table_name}` where `Event ID` = {event_id} and `Item Name` = '{item_name1}'"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Inventory Item and its details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_inventory(inventory_table_name):
    print()
    inventory_table_name = inventory_table_name
    event_id = input("Enter Event ID (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{inventory_table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        if row:
            count = 1
            print("Result(s) Found\n")
            what_to_show = input("What would you like to see from the results? (Type all to see all details): ")
            for details in row:
                print("Result", count)
                if what_to_show == "Item Name":
                    print('Item Name:', details[1])
                elif what_to_show == "Quantity":
                    print('Quantity:', details[2])
                elif what_to_show == "Availability":
                    print('Availability:', details[3])
                elif what_to_show == "all":
                    print('Item Name:', details[1])
                    print('Quantity:', details[2])
                    print('Availability:', details[3])
                count += 1
        else:
            print("Item Details not found, please try again")
            search_inventory(inventory_table_name)
    print("\ngoing back to previous screen \n")


def add_staff(staff_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    staff_name = input("Enter staff name: ")
    if staff_name == "0":
        print("\ngoing back to previous screen \n")
        return
    staff_role = input("Enter staff role: ")
    if staff_role == "0":
        print("\ngoing back to previous screen \n")
        return
    staff_contact = int(input("Enter staff contact number: "))
    if staff_contact == 0:
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"INSERT INTO `{staff_table_name}` (`Event ID`, `Staff Name`, `Staff Role`, `Staff Contact`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_query, (event_id, staff_name, staff_role, staff_contact))
    mycon.commit()
    print("Successfully added staff details to the database.")
    print("\ngoing back to previous screen \n")


def display_staff(staff_table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{staff_table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Staff', count)
        print('Event ID:', row[0])
        print('Staff Name:', row[1])
        print('Staff Role:', row[2])
        print('Staff Contact:', row[3])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def update_staff(staff_table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the Staff details you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    staff_name1 = input("Enter old staff name: ")
    staff_name = input("Enter New Staff Name: ")
    if staff_name == "0":
        print("\ngoing back to previous screen \n")
        return
    staff_role = input("Enter New Staff Role: ")
    if staff_role == "0":
        print("\ngoing back to previous screen \n")
        return
    staff_contact = input("Enter New Staff Contact Details: ")
    if staff_contact == "0":
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{staff_table_name}` SET `Staff Name` = %s, `Staff Role` = %s, `Staff Contact` = %s where `Event ID` = %s and `Staff Name` = %s"
    cursor.execute(sql_query, (staff_name, staff_role, staff_contact, event_id, staff_name1))
    mycon.commit()
    print("Staff Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_staff(staff_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    staff_name = (input("Enter Staff Name:"))
    if staff_name == '0':
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{staff_table_name}` where `Event ID` = {event_id} and `Staff Name` = '{staff_name}'"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Staff details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_staff(staff_table_name):
    print()
    staff_table_name = staff_table_name
    event_id = input("Enter Event ID (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{staff_table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        if row:
            count = 1
            print("Result(s) Found\n")
            what_to_show = input("What would you like to see from the results? (Type all to see all details): ")
            for details in row:
                print("Result", count)
                if what_to_show == "Staff Name":
                    print('Staff Name:', details[1])
                elif what_to_show == "Staff Role":
                    print('Staff Role:', details[2])
                elif what_to_show == "Staff Contact":
                    print('Staff Contact:', details[3])
                elif what_to_show == "all":
                    print('Staff Name:', details[1])
                    print('Staff Role:', details[2])
                    print('Staff Contact:', details[3])
                count += 1
        else:
            print("Staff Details not found, please try again")
            search_staff(staff_table_name)
    print("\ngoing back to previous screen \n")


def add_transportation(transportation_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    vehicle_name = input("Enter vehicle name: ")
    if vehicle_name == "0":
        print("\ngoing back to previous screen \n")
        return
    route = input("Enter route in short: ")
    if route == "0":
        print("\ngoing back to previous screen \n")
        return
    schedule = input("Enter Schedule Details: ")
    if schedule == '0':
        print("\ngoing back to previous screen \n")
        return
    driver_name = input("Enter driver name: ")
    if driver_name == "0":
        print("\ngoing to previous screen \n")
        return
    sql_query = f"INSERT INTO `{transportation_table_name}` (`Event ID`, `Vehicle Name`, `Route`, `Schedule`, `Driver Name`) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_query, (event_id, vehicle_name, route, schedule, driver_name))
    mycon.commit()
    print("Successfully added staff details to the database.")
    print("\ngoing back to previous screen \n")


def display_transportation(transportation_table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{transportation_table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Transport', count)
        print('Event ID:', row[0])
        print('Vehicle Name:', row[1])
        print('Route:', row[2])
        print('Schedule:', row[3])
        print('Driver Name:', row[4])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def update_transportation(transportation_table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the Transportation details you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    vehicle_name1 = input("Enter old Vehicle Name: ")
    vehicle_name = input("Enter New Vehicle Name: ")
    if vehicle_name == "0":
        print("\ngoing back to previous screen \n")
        return
    route = input("Enter New Route: ")
    if route == "0":
        print("\ngoing back to previous screen \n")
        return
    schedule = input("Enter New Schedule Status: ")
    if schedule == "0":
        print("\ngoing back to previous screen \n")
        return
    driver_name = input("Enter New Driver Name: ")
    if driver_name == "0":
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{transportation_table_name}` SET `Vehicle Name` = %s, `Route` = %s, `Schedule` = %s, `Driver Name` = %s where `Event ID` = %s and `Vehicle Name` = %s"
    cursor.execute(sql_query, (vehicle_name, route, schedule, driver_name, event_id, vehicle_name1))
    mycon.commit()
    print("Transportation Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_transportation(transportation_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    vehicle_name = input("Enter Vehicle Name: ")
    if vehicle_name == '0':
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{transportation_table_name}` where `Event ID` = {event_id} and `Vehicle Name` = '{vehicle_name}'"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Transportation details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_transportation(transportation_table_name):
    print()
    transportation_table_name = transportation_table_name
    event_id = input("Enter Event ID (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{transportation_table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        if row:
            count = 1
            print("Result(s) Found\n")
            what_to_show = input("What would you like to see from the results? (Type all to see all details): ")
            for details in row:
                print("Result", count)
                if what_to_show == "Vehicle Name":
                    print('Vehicle Name:', details[1])
                elif what_to_show == "Route":
                    print('Route:', details[2])
                elif what_to_show == "Schedule":
                    print('Schedule:', details[3])
                elif what_to_show == "Driver Name":
                    print('Driver Name:', details[4])
                elif what_to_show == "all":
                    print('Vehicle Name:', details[1])
                    print('Route:', details[2])
                    print('Schedule:', details[3])
                    print('Driver Name:', details[4])
                count += 1
        else:
            print("Staff Details not found, please try again")
            search_transportation(transportation_table_name)
    print("\ngoing back to previous screen \n")


def add_venue(venue_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    venue_name = input("Enter Venue Name: ")
    if venue_name == "0":
        print("\ngoing back to previous screen \n")
        return
    venue_address = input("Enter Venue Address: ")
    if venue_address == "0":
        print("\ngoing back to previous screen \n")
        return
    capacity = int(input("Enter Capacity: "))
    if capacity == 0:
        print("\ngoing to previous screen \n")
        return
    availability = input("Enter Availability: ")
    if availability == '0':
        print("\ngoing back to previous screen \n")
        return

    sql_query = f"INSERT INTO `{venue_table_name}` (`Event ID`, `Venue Name`, `Venue Address`, `Capacity`, `Availability`) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_query, (event_id, venue_name, venue_address, capacity, availability))
    mycon.commit()
    print("Successfully added venue details to the database.")
    print("\ngoing back to previous screen \n")


def display_venue(venue_table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{venue_table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Venue', count)
        print('Event ID:', row[0])
        print('Venue Name:', row[1])
        print('Venue Address:', row[2])
        print('Capacity:', row[3])
        print('Availability:', row[4])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def update_venue(venue_table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the Venue details you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    venue_name1 = input("Enter old Venue Name: ")
    if venue_name1 == '0':
        print("\ngoing back to previous screen \n")
        return
    venue_name = input("Enter New Venue Name: ")
    if venue_name == "0":
        print("\ngoing back to previous screen \n")
        return
    venue_address = input("Enter New Venue Address: ")
    if venue_address == "0":
        print("\ngoing back to previous screen \n")
        return
    capacity = input("Enter New Capacity of the Venue: ")
    if capacity == "0":
        print("\ngoing back to previous screen \n")
        return
    availability = input("Enter New Availability: ")
    if availability == "0":
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{venue_table_name}` SET `Venue Name` = %s, `Venue Address` = %s, `Capacity` = %s, `Availability` = %s where `Event ID` = %s and `Venue Name` = %s"
    cursor.execute(sql_query, (venue_name, venue_address, capacity, availability, event_id, venue_name1))
    mycon.commit()
    print("Venue Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_venue(venue_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    venue_name = input("Enter Venue Name: ")
    if venue_name == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{venue_table_name}` where `Event ID` = {event_id} and `Venue Name` = '{venue_name}'"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Venue details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_venue(venue_table_name):
    print()
    venue_table_name = venue_table_name
    event_id = input("Enter Event ID (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{venue_table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        if row:
            count = 1
            print("Result(s) Found\n")
            what_to_show = input("What would you like to see from the results? (Type all to see all details): ")
            for details in row:
                print("Result", count)
                if what_to_show == "Venue Name":
                    print('Venue Name:', details[1])
                elif what_to_show == "Venue Address":
                    print('Venue Address:', details[2])
                elif what_to_show == "Capacity":
                    print('Capacity:', details[3])
                elif what_to_show == "Availability":
                    print('Availability:', details[4])
                elif what_to_show == "all":
                    print('Venue Name:', details[1])
                    print('Venue Address:', details[2])
                    print('Capacity:', details[3])
                    print('Availability:', details[4])
                count += 1
        else:
            print("Venue Details not found, please try again")
            search_venue(venue_table_name)
    print("\ngoing back to previous screen \n")


def add_attendee(attendees_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    attendee_name = input("Enter Attendee Name: ")
    if attendee_name == "0":
        print("\ngoing back to previous screen \n")
        return
    attendee_email_address = input("Enter Attendee Email Address: ")
    if attendee_email_address == "0":
        print("\ngoing back to previous screen \n")
        return
    attendee_phone_number = input("Enter Attendee Phone Number: ")
    if attendee_phone_number == 0:
        print("\ngoing to previous screen \n")
        return

    sql_query = f"INSERT INTO `{attendees_table_name}` (`Event ID`, `Attendee Name`, `Attendee Email`, `Attendee Phone Number`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_query, (event_id, attendee_name, attendee_email_address, attendee_phone_number))
    mycon.commit()
    print("Successfully added attendee details to the database.")
    print("\ngoing back to previous screen \n")


def display_attendee(attendees_table_name):
    print()
    count = 1
    sql_query = f"SELECT * FROM `{attendees_table_name}`"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    for row in result:
        print('Attendee', count)
        print('Event ID:', row[0])
        print('Attendee Name:', row[1])
        print('Attendee Email Address:', row[2])
        print('Attendee Phone Number:', row[3])
        print()
        count += 1
    print("\ngoing back to previous screen \n")


def update_attendee(attendees_table_name):
    print()
    print("Warning: You must update all details or enter the old details for those columns you don't want to update.")
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID of the Attendee details you want to update: "))
    if event_id == 0:
        print("\ngoing back to previous screen \n")
        return
    attendee_name1 = input("Enter Old Attendee Name")
    attendee_name = input("Enter New Attendee Name: ")
    if attendee_name == "0":
        print("\ngoing back to previous screen \n")
        return
    attendee_email_address = input("Enter New Attendee Email Address: ")
    if attendee_email_address == "0":
        print("\ngoing back to previous screen \n")
        return
    attendee_phone_number = int(input("Enter New Attendee Phone Number: "))
    if attendee_phone_number == 0:
        print("\ngoing back to previous screen \n")
        return
    sql_query = f"UPDATE `{attendees_table_name}` SET `Attendee Name` = %s, `Attendee Email` = %s, `Attendee Phone Number` = %s where `Event ID` = %s and `Attendee Name` = %s"
    cursor.execute(sql_query, (attendee_name, attendee_email_address, attendee_phone_number, event_id, attendee_name1))
    mycon.commit()
    print("Attendee Details have been updated successfully.")
    print("\ngoing back to previous screen \n")


def delete_attendee(attendees_table_name):
    print()
    print("Enter 0 at any time to go back")
    event_id = int(input("Enter Event ID: "))
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    attendee_name = input("Enter Attendee Name: ")
    if attendee_name == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"DELETE FROM `{attendees_table_name}` where `Event ID` = {event_id} and `Attendee Name` = '{attendee_name}'"
        cursor.execute(sql_query)
        mycon.commit()
        print("Requested Attendee details have been deleted successfully.")
        print("\ngoing back to previous screen \n")


def search_attendee(attendees_table_name):
    print()
    attendees_table_name = attendees_table_name
    event_id = input("Enter Event ID (or enter 0 to go back): ")
    if event_id == "0":
        print("\ngoing back to previous screen \n")
        return
    else:
        sql_query = f"SELECT * FROM `{attendees_table_name}` where `Event ID` = {event_id}"
        cursor.execute(sql_query)
        row = cursor.fetchall()
        if row:
            count = 1
            print("Result(s) Found\n")
            what_to_show = input("What would you like to see from the results? (Type all to see all details): ")
            for details in row:
                print("Result", count)
                if what_to_show == "Attendee Name":
                    print('Attendee Name:', details[1])
                elif what_to_show == "Attendee Email Address":
                    print('Attendee Email Address:', details[2])
                elif what_to_show == "Attendee Phone Number":
                    print('Attendee Phone Number:', details[3])
                elif what_to_show == "all":
                    print('Attendee Name:', details[1])
                    print('Attendee Email Address:', details[2])
                    print('Attendee Phone Number:', details[3])
                count += 1
        else:
            print("Attendee Details not found, please try again")
            search_attendee(attendees_table_name)
    print("\ngoing back to previous screen \n")


def main():
    while True:
        print("╔═════════════════════════╗")
        print("║ EVENT MANAGEMENT SYSTEM ║")
        print("╚═════════════════════════╝")
        choice = input("WELCOME! \n1. New User? Register Here! \n2. Existing User? Login Here! \n3. Exit EMS \nWhat do "
                       "you want to do? (Enter 1, 2, or 3): ")
        if choice == '1':
            print()
            register_user()
        elif choice == '2':
            print()
            x, username = login_user()
            event_table_name = 'event_' + username
            inventory_table_name = 'inventory_' + username
            staff_table_name = 'staff_' + username
            transportation_table_name = 'transport_' + username
            venue_table_name = 'venue_' + username
            attendees_table_name = 'attendees_' + username
            if x:
                while True:
                    print("╔════════════════════════╗")
                    print("║       DASHBOARD        ║")
                    print("╚════════════════════════╝")
                    choice0 = input(
                        "1. Event Management \n2. Resources and Logistics Management \n3. Attendee Management "
                        "\n4. Log Out (Enter 1, 2, 3, or 4): ")
                    print()
                    if choice0 == '1':
                        while True:
                            print("╔══════════════════════════════╗")
                            print("║       EVENT MANAGEMENT       ║")
                            print("╚══════════════════════════════╝")
                            choice1 = input("1. Display All Events \n2. Add a New Event \n3. Update Existing Event "
                                            "Details\n4. Delete a Event \n5. Search in the Event \n6. Back \nWhat do you "
                                            "want to do? (Enter 1, 2, 3, 4, 5, or 6): ")
                            if choice1 == '1':
                                display_all_events(event_table_name)
                            elif choice1 == '2':
                                add_event(event_table_name)
                            elif choice1 == '3':
                                update_event(event_table_name)
                            elif choice1 == '4':
                                delete_event(event_table_name)
                            elif choice1 == '5':
                                search_event(event_table_name)
                            elif choice1 == '6':
                                print("\ngoing back to previous screen \n")
                                break
                            else:
                                print("Invalid choice, please try again!\n")
                    elif choice0 == '2':
                        while True:
                            print("╔══════════════════════════════════╗")
                            print("║       LOGISTICS MANAGEMENT       ║")
                            print("╚══════════════════════════════════╝")
                            choice2 = input("1. Inventory \n2. Staff Details \n3. Transportation \n4. Venue \n5. Back "
                                            "\nWhat do you want to do? (Enter 1, 2, 3, 4 or 5): ")
                            print()
                            if choice2 == '1':
                                while True:
                                    print("╔════════════════════════╗")
                                    print("║        inventory       ║")
                                    print("╚════════════════════════╝")
                                    choice2_1 = input("1. Add Equipment to Inventory \n2. Display all Inventory \n3. "
                                                      "Update Inventory Details \n4. Delete Inventory Details \n5. Search "
                                                      "Inventory Details, \n6. Back \nWhat do you want to do? (Enter 1, "
                                                      "2, 3, 4, 5 or 6): ")
                                    if choice2_1 == '1':
                                        add_inventory(inventory_table_name)
                                    elif choice2_1 == '2':
                                        display_inventory(inventory_table_name)
                                    elif choice2_1 == '3':
                                        update_inventory(inventory_table_name)
                                    elif choice2_1 == '4':
                                        delete_inventory(inventory_table_name)
                                    elif choice2_1 == '5':
                                        search_inventory(inventory_table_name)
                                    elif choice2_1 == '6':
                                        print("\ngoing back to previous screen \n")
                                        break
                                    else:
                                        print("Invalid choice, please try again!\n")
                            elif choice2 == '2':
                                while True:
                                    print("╔════════════════════════════╗")
                                    print("║        staff details       ║")
                                    print("╚════════════════════════════╝")
                                    choice2_2 = input("1. Add Staff Details \n2. Display all Staff Details \n3. Update "
                                                      "Staff Details \n4. Delete Staff Details \n5. Search Staff Details, "
                                                      "\n6. Back \nWhat do you want to do? (Enter 1, 2, 3, 4, 5 or 6): ")
                                    if choice2_2 == '1':
                                        add_staff(staff_table_name)
                                    elif choice2_2 == '2':
                                        display_staff(staff_table_name)
                                    elif choice2_2 == '3':
                                        update_staff(staff_table_name)
                                    elif choice2_2 == '4':
                                        delete_staff(staff_table_name)
                                    elif choice2_2 == '5':
                                        search_staff(staff_table_name)
                                    elif choice2_2 == '6':
                                        print("\ngoing back to previous screen \n")
                                        break
                                    else:
                                        print("Invalid choice, please try again!\n")
                            elif choice2 == '3':
                                while True:
                                    print("╔═════════════════════════════╗")
                                    print("║        transportation       ║")
                                    print("╚═════════════════════════════╝")
                                    choice2_3 = input("1. Add Transportation Details \n2. Display All Transportation "
                                                      "Details \n3. Update Transportation Details \n4. Delete "
                                                      "Transportation Details \n5. Search Transportation Details \n 6. "
                                                      "Back \nWhat do you want to do? (Enter 1, 2, 3, 4, 5 or 6): ")
                                    if choice2_3 == '1':
                                        add_transportation(transportation_table_name)
                                    elif choice2_3 == '2':
                                        display_transportation(transportation_table_name)
                                    elif choice2_3 == '3':
                                        update_transportation(transportation_table_name)
                                    elif choice2_3 == '4':
                                        delete_transportation(transportation_table_name)
                                    elif choice2_3 == '5':
                                        search_transportation(transportation_table_name)
                                    elif choice2_3 == '6':
                                        print("\ngoing back to previous screen \n")
                                        break
                                    else:
                                        print("Invalid choice, please try again!\n")
                            elif choice2 == '4':
                                while True:
                                    print("╔═════════════════════════════╗")
                                    print("║        venue details        ║")
                                    print("╚═════════════════════════════╝")
                                    choice2_4 = input("1. Add Venue Details \n2. Display All Venue Details \n3. Update "
                                                      "Venue Details \n4. Delete Venue Details \n5. Search Venue Details "
                                                      "\n6. Back \nWhat do you want to do? (Enter 1, 2, 3, 4, 5 or 6): ")
                                    if choice2_4 == '1':
                                        add_venue(venue_table_name)
                                    elif choice2_4 == '2':
                                        display_venue(venue_table_name)
                                    elif choice2_4 == '3':
                                        update_venue(venue_table_name)
                                    elif choice2_4 == '4':
                                        delete_venue(venue_table_name)
                                    elif choice2_4 == '5':
                                        search_venue(venue_table_name)
                                    elif choice2_4 == '6':
                                        print("\ngoing back to previous screen \n")
                                        break
                                    else:
                                        print("Invalid choice, please try again!\n")
                            elif choice2 == '5':
                                print("\ngoing back to previous screen \n")
                                break
                            else:
                                print("Invalid choice, please try again!\n")
                    elif choice0 == '3':
                        while True:
                            print("╔═════════════════════════════════════╗")
                            print("║         ATTENDEE MANAGEMENT         ║")
                            print("╚═════════════════════════════════════╝")
                            choice3 = input("1. Add Attendee Details \n2. Display All Attendees Details \n3. Update "
                                            "Attendee Details \n4. Delete Attendee Details \n5. Search Attendee Details "
                                            "\n6. Back \nWhat do you want to do? (Enter 1, 2, 3, 4, 5, or 6): ")
                            if choice3 == '1':
                                add_attendee(attendees_table_name)
                            elif choice3 == '2':
                                display_attendee(attendees_table_name)
                            elif choice3 == '3':
                                update_attendee(attendees_table_name)
                            elif choice3 == '4':
                                delete_attendee(attendees_table_name)
                            elif choice3 == '5':
                                search_attendee(attendees_table_name)
                            elif choice3 == '6':
                                print("\ngoing back to previous screen \n")
                                break
                            else:
                                print("Invalid choice, please try again!\n")
                    elif choice0 == '4':
                        print("Logging out..\n")
                        break
                    else:
                        print("Invalid choice, please try again!\n")

        elif choice == '3':
            close_connection()
            print("Thank you for using this EMS, Hope you use it again!")
            break
        else:
            print("Invalid choice, please try again!\n")


if __name__ == "__main__":
    main()
