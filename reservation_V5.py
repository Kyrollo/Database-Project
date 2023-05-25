from logging import root
from tkinter import *

def register():
    # Get user input values
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    address = entry_address.get()
    email = entry_email.get()
    role = var_role.get()
    user_id = entry_id_register.get()

    # Validate input values
    if not first_name:
        lbl_message_register_first_name.config(text="Please enter first name", fg="red")
    else:
        lbl_message_register_first_name.config(text="")

    if not last_name:
        lbl_message_register_last_name.config(text="Please enter last name", fg="red")
    else:
        lbl_message_register_last_name.config(text="")

    if not phone:
        lbl_message_register_phone.config(text="Please enter phone number", fg="red")
    elif not phone.startswith(('010', '011', '012', '015')) or len(phone) != 11 or not phone.isdigit():
        lbl_message_register_phone.config(text="Invalid phone number", fg="red")
    else:
        lbl_message_register_phone.config(text="")

    if not address:
        lbl_message_register_address.config(text="Please enter address", fg="red")
    else:
        lbl_message_register_address.config(text="")

    if not email:
        lbl_message_register_email.config(text="Please enter email", fg="red")
    elif '@' not in email or '.com' not in email:
        lbl_message_register_email.config(text="Invalid email address", fg="red")
    else:
        lbl_message_register_email.config(text="")

    if not role:
        lbl_message_register_role.config(text="Please select role", fg="red")
    else:
        lbl_message_register_role.config(text="")

    if not user_id:
        lbl_message_register_id.config(text="Please enter ID", fg="red")
    elif not user_id.isdigit():
        lbl_message_register_id.config(text="Invalid ID", fg="red")
    elif int(user_id) <= 0:
        lbl_message_register_id.config(text="ID must be a positive integer", fg="red")
    else:
        lbl_message_register_id.config(text="")

    # Check if all fields are valid
    if all([
        first_name,
        last_name,
        phone and phone.startswith(('010', '011', '012', '015')) and len(phone) == 11 and phone.isdigit(),
        address,
        email and '@' in email and '.com' in email,
        role,
        user_id and user_id.isdigit() and int(user_id) > 0
    ]):
        # Registration successful
        lbl_message_register.config(text="Registration successful!", fg="green")

        # Hide login and register buttons
        navigation_frame.pack_forget()

        
        
        # Clear registration input fields
        entry_first_name.delete(0, END)
        entry_last_name.delete(0, END)
        entry_phone.delete(0, END)
        entry_address.delete(0, END)
        entry_email.delete(0, END)
        entry_id_register.delete(0, END)
        
        # Show appropriate page based on role
        if role == "admin":
            navigation_frame_Admin.pack(side=TOP, anchor=NE)
            show_admin_page()
        else:
            navigation_frame_Customer.pack(side=TOP, anchor=NE)
            show_flights_page()

def login():
    # Get user input values
    user_id = entry_id_login.get()
    role = var_role_login.get()  

    # Validate input values
    if not user_id:
        lbl_message_login.config(text="Please enter ID", fg="red", bg='#0B2447', foreground='#FEFAE0', font=('Arial', 10))
    elif not user_id.isdigit():
        lbl_message_login.config(text="Invalid ID", fg="red", bg='#0B2447', foreground='#FEFAE0', font=('Arial', 10))
    else:
        lbl_message_login.config(text="Login successful!", fg="green", bg='#0B2447', foreground='#FEFAE0',font=('Arial', 10))

        # Clear login input fields
        entry_id_login.delete(0, END)

        # Hide login and register buttons
        navigation_frame.pack_forget()


        # Show appropriate page based on role
        if role == "admin":
            navigation_frame_Admin.pack(side=TOP, anchor=NE)
            show_admin_page()
        else:
            navigation_frame_Customer.pack(side=TOP, anchor=NE)
            show_flights_page()

def add_craft():
    craft_id = id_entry.get()
    craft_name = name_entry.get()
    craft_capacity = capacity_entry.get()
    
    # Perform necessary actions with the craft details (e.g., store in a database)
    # print("Craft ID:", craft_id)
    # print("Craft Name:", craft_name)
    # print("Craft Capacity:", craft_capacity)
    
    # Clear the entry fields after adding the craft
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    capacity_entry.delete(0, END)

def update_aircraft():
    # Get the user input from the entry fields
    aircraft_id = entry_aircraft_id.get()
    new_aircraft_name = entry_new_aircraft_name.get()
    new_aircraft_capacity = entry_new_aircraft_capacity.get()

    # Perform the update operation based on the input data
    # Replace the following lines with your actual update logic
    # For demonstration purposes, we'll simply print the updated data
    print("Aircraft ID:", aircraft_id)
    print("New Aircraft Name:", new_aircraft_name)
    print("New Capacity:", new_aircraft_capacity)

    # Clear the entry fields after updating
    entry_aircraft_id.delete(0, 'end')
    entry_new_aircraft_name.delete(0, 'end')
    entry_new_aircraft_capacity.delete(0, 'end')

def add_flight():
    flight_id = int(entry_id.get())
    ac_id = int(entry_ac_id.get())
    airport = entry_airport.get()
    date = entry_date.get()
    source = entry_source.get()
    destination = entry_dest.get()
    seats = int(entry_seats.get())
    price = int(entry_price.get())
    
    # print("Flight ID:", flight_id)
    # print("Aircraft ID:", ac_id)
    # print("Airport:", airport)
    # print("Date:", date)
    # print("Source:", source)
    # print("Destination:", destination)
    # print("Number of Seats:", seats)
    # print("Price:", price)
    
    # Clear the entry fields after adding the flight
    entry_id.delete(0, END)
    entry_ac_id.delete(0, END)
    entry_airport.delete(0, END)
    entry_date.delete(0, END)
    entry_source.delete(0, END)
    entry_dest.delete(0, END)
    entry_seats.delete(0, END)
    entry_price.delete(0, END)

def update_flight():
    flight_id = entry_flight_id.get()
    ac_id = entry_ac_id.get()
    airport = entry_airport.get()
    date = entry_date.get()
    source = entry_source.get()
    dest = entry_dest.get()
    seats = entry_seats.get()
    price = entry_price.get()
    
    # Clear the entry fields
    entry_flight_id.delete(0, 'end')
    entry_ac_id.delete(0, 'end')
    entry_airport.delete(0, 'end')
    entry_date.delete(0, 'end')
    entry_source.delete(0, 'end')
    entry_dest.delete(0, 'end')
    entry_seats.delete(0, 'end')
    entry_price.delete(0, 'end')

def show_register_page():
    login_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    register_page.pack()
    register_page.config(bg='#0B2447')

def show_login_page():
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    login_page.pack()
    login_page.config(bg='#0B2447')

def show_flights_page():
    login_page.pack_forget()
    register_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    flights_page.pack()
    flights_page.config(bg='#0B2447')

def show_book_flights_page(flight_id):
    login_page.pack_forget()
    register_page.pack_forget()
    admin_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()
    

    book_flights_page.pack()
    book_flights_page.config(bg='#0B2447')
    # Create a label for number of seats
    seats_label = Label(book_flights_page, text="Number of Seats:")
    seats_label.pack()

    # Create an entry field for number of seats
    seats_entry = Entry(book_flights_page)
    seats_entry.pack()

    # Create a label for flight class
    class_label = Label(book_flights_page, text="Flight Class:")
    class_label.pack()

    # Create a variable to store the selected class
    class_var = StringVar(window)
    class_var.set("Economy")  

    # Create a dropdown menu for flight class
    class_dropdown = OptionMenu(book_flights_page, class_var, "Economy", "Business", "First Class")


    # Create a button to book the flight
    book_button = Button(book_flights_page, text="Book", command=lambda:show_my_flight_page(flight_id)) 
    book_button.pack()



def show_my_flight_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    my_flight_page.pack()
    my_flight_page.config(bg='#0B2447')


def show_customer_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    admin_page.pack()
    admin_page.config(bg='#0B2447')

def show_add_flights_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()
    

    add_flights_page.pack()
    add_flights_page.config(bg='#0B2447')

def show_update_flights_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    update_flights_page.pack()
    update_flights_page.config(bg='#0B2447')

def show_admin_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()
    update_aircraft_page.pack_forget()

    admin_page.pack()
    admin_page.config(bg='#0B2447')

def show_add_aircraft_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    update_aircraft_page.pack_forget()

    add_aircraft_page.pack()
    add_aircraft_page.config(bg='#0B2447')
   
def show_update_aircraft_page():
    login_page.pack_forget()
    register_page.pack_forget()
    flights_page.pack_forget()
    book_flights_page.pack_forget()
    admin_page.pack_forget()
    admin_page.pack_forget()
    add_flights_page.pack_forget()
    update_flights_page.pack_forget()
    add_aircraft_page.pack_forget()

    update_aircraft_page.pack()
    update_aircraft_page.config(bg='#0B2447')

flights = [
    {"id": "FL123","airport":"Cairo", "date": "2023-05-22", "source": "Cairo", "dest": "Alex", "n_seats": 150, "price": 1500},
    {"id": "FL456","airport":"Luxor", "date": "2023-05-23", "source": "Luxor", "dest": "Dahb", "n_seats": 100, "price": 1000},
    {"id": "FL789","airport":"Aswan", "date": "2023-05-24", "source": "Aswan", "dest": "Sumabay", "n_seats": 200, "price": 2000},
]

def get_flight_details_by_id(flight_id):
    
    # Filter flight details based on the provided date
    filtered_flights = [flight for flight in flights if flight['id'] == flight_id]

    if filtered_flights:
        return filtered_flights[0]  # Return the first matching flight details
    else:
        return None  # No flight details found for the provided date

def book_flight(flight_id):

    lbl_message_book = Label(window, text="", fg="")

    

    # Get the flight details based on the flight ID
    flight_details = get_flight_details_by_id(flight_id)

    if flight_details:
        # Perform the booking operation (e.g., store the booking details in a database)
        # You can access the flight details using the flight_details variable

        # Display a confirmation message to the user
        lbl_message_book.config(text="Flight booked successfully!", fg="green")

        # Clear the entry field for flight ID
        entry_flight_id.delete(0, END)
        lbl_message_book.pack()
    else:
        # If no flight details found, display an error message
        lbl_message_book.config(text="Invalid flight ID", fg="red")
        lbl_message_book.pack()

def display_flights():
    # Clear existing flights
    for widget in flights_page.winfo_children():
        widget.destroy()

    # Retrieve flights from the database or any other data source
    # flights = get_flights()  # Replace with your own logic to fetch flights data

    if flights:
        for i, flight in enumerate(flights):
            flight_details = f"Flight {i + 1}\t" \
                             f"Flight ID: {flight['id']}\t" \
                             f"Airport: {flight['airport']}\t" \
                             f"Date: {flight['date']}\t" \
                             f"Source: {flight['source']}\t" \
                             f"Destination: {flight['dest']}\t" \
                             f"Number of Seats: {flight['n_seats']}\t" \
                             f"Price: {flight['price']}"

            lbl_flight = Label(flights_page, text=flight_details)
            lbl_flight.pack()

            if var_role_login.get() != "admin":
                btn_book_now = Button(flights_page, text="Book Now",command=lambda flight_id=flight['id']: show_book_flights_page(flight_id))
                btn_book_now.pack()

            lbl_spacing = Label(flights_page, text="")
            lbl_spacing.pack()
    else:
        lbl_no_flights = Label(flights_page, text="No flights available.")
        lbl_no_flights.pack()

# Clear existing content
    my_flight_page.destroy()

    # Create new My Flight page
    my_flight_page = Frame(window)
    my_flight_page.pack()
    my_flight_page.config(bg='#0B2447')

    # # Get the user's flights
    # user_id = entry_id_login.get()  # Assuming the user ID is obtained from the login page
    # user_flights = get_flight_details_by_id(user_id)

    # if user_flights:
    #     for i, flight in enumerate(user_flights):
    #         flight_details = f"Flight {i+1}\t" \
    #                          f"Flight ID: {flight['id']}\t" \
    #                          f"Airport: {flight['airport']}\t" \
    #                          f"Date: {flight['date']}\t" \
    #                          f"Source: {flight['source']}\t" \
    #                          f"Destination: {flight['dest']}\t" \
    #                          f"Number of Seats: {flight['n_seats']}\t" \
    #                          f"Price: {flight['price']}"

    #         lbl_flight = Label(my_flight_page, text=flight_details)
    #         lbl_flight.pack()

    #         lbl_spacing = Label(my_flight_page, text="")
    #         lbl_spacing.pack()
    # else:
    #     lbl_no_flights = Label(my_flight_page, text="No flights available.")
    #     lbl_no_flights.pack()

# Create the main window
window = Tk()
window.geometry("1250x700")
window.title("Flight reservation system")

# Create register page
register_page = Frame(window)

lbl_first_name = Label(register_page, text="First Name:", background='#0B2447',foreground='#FEFAE0')
lbl_first_name.grid(row=0, column=0, sticky="w")
entry_first_name = Entry(register_page)
entry_first_name.grid(row=0, column=1)
lbl_message_register_first_name = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_first_name.grid(row=1, column=0, columnspan=2, sticky="w")

lbl_last_name = Label(register_page, text="Last Name:", background='#0B2447',foreground='#FEFAE0')
lbl_last_name.grid(row=2, column=0, sticky="w")
entry_last_name = Entry(register_page)
entry_last_name.grid(row=2, column=1)
lbl_message_register_last_name = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_last_name.grid(row=3, column=0, columnspan=2, sticky="w")

lbl_phone = Label(register_page, text="Phone:", background='#0B2447',foreground='#FEFAE0')
lbl_phone.grid(row=4, column=0, sticky="w")
entry_phone = Entry(register_page)
entry_phone.grid(row=4, column=1)
lbl_message_register_phone = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_phone.grid(row=5, column=0, columnspan=2, sticky="w")

lbl_address = Label(register_page, text="Address:", background='#0B2447',foreground='#FEFAE0')
lbl_address.grid(row=6, column=0, sticky="w")
entry_address = Entry(register_page)
entry_address.grid(row=6, column=1)
lbl_message_register_address = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_address.grid(row=7, column=0, columnspan=2, sticky="w")

lbl_email = Label(register_page, text="Email:", background='#0B2447',foreground='#FEFAE0')
lbl_email.grid(row=0, column=3, sticky="w")
entry_email = Entry(register_page)
entry_email.grid(row=0, column=4)
lbl_message_register_email = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_email.grid(row=1, column=3, columnspan=2, sticky="w")

lbl_id = Label(register_page, text="ID:", background='#0B2447',foreground='#FEFAE0')
lbl_id.grid(row=2, column=3, sticky="w")
entry_id_register = Entry(register_page)  
entry_id_register.grid(row=2, column=4)
lbl_message_register_id = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_id.grid(row=3, column=3, columnspan=2, sticky="w")

lbl_role = Label(register_page, text="Role:", background='#0B2447',foreground='#FEFAE0')
lbl_role.grid(row=4, column=3, sticky="w")
var_role = StringVar(value="customer")  

radio_admin = Radiobutton(register_page, text="Admin", variable=var_role, value="admin", background='#0B2447',foreground='#FEFAE0',selectcolor='#002B5B')
radio_admin.grid(row=4, column=4)
radio_customer = Radiobutton(register_page, text="Customer", variable=var_role, value="customer", background='#0B2447',foreground='#FEFAE0',selectcolor='#002B5B')
radio_customer.grid(row=4, column=5)

lbl_message_register_role = Label(register_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
lbl_message_register_role.grid(row=5, column=3, columnspan=2, sticky="w")


btn_register = Button(register_page, text="Register", command=register, background='#0B2447', foreground='#FEFAE0')
btn_register.grid(row=8, column=2, pady=10)

lbl_message_register = Label(register_page, text="", background='#0B2447',foreground='#FEFAE0')
lbl_message_register.grid(row=9, columnspan=5, pady=10)

# Create login page
login_page = Frame(window)

lbl_id = Label(login_page, text="ID:",font=('Arial',20),background='#0B2447',foreground='#FEFAE0')
lbl_id.grid(row=1,column=0,sticky="w",padx=10,pady=250)

entry_id_login = Entry(login_page,font=(50))  

entry_id_login.grid(row=1,column=1,padx=20,pady=250)
lbl_message_login = Label(login_page, text="", fg="red" ,background='#0B2447',foreground='#FEFAE0')
lbl_message_login.grid(row=6, columnspan=5)

lbl_role_login = Label(login_page, text="Role:",font=('Arial',20),background='#0B2447',foreground='#FEFAE0')

lbl_role_login.place(x=0,y=300)
var_role_login = StringVar(value="customer")  

radio_admin_login = Radiobutton(login_page, text="Admin", variable=var_role_login, value="admin",font=('Arial',16),background='#0B2447',foreground='#FEFAE0',selectcolor='#002B5B')

radio_admin_login.place(x=90,y=300)
radio_customer_login = Radiobutton(login_page, text="Customer", variable=var_role_login, value="customer",font=('Arial',16),background='#0B2447',foreground='#FEFAE0',selectcolor='#002B5B')
radio_customer_login.place(x=180,y=300)

btn_login = Button(login_page, text="Login", command=login,font=('Arial',16),background='#0B2447',foreground='#FEFAE0')
btn_login.place(x=140,y=400)


# Create flights page
flights_page = Frame(window)

lbl_flights = Label(flights_page, text="Welcome to the Flights Page!")
lbl_flights.pack()

btn_display_flights = Button(flights_page, text="Display Flights", command=display_flights, background='#0B2447', foreground='#FEFAE0')
btn_display_flights.pack()

# Create book flights page
book_flights_page = Frame(window)

lbl_flights_book = Label(book_flights_page, text="Welcome to the Book Flights Page!")
lbl_flights_book.pack()


# Create my flights page
my_flight_page = Frame(window)

lbl_my_flights = Label(my_flight_page, text="Welcome to the Book Flights Page!")
lbl_my_flights.pack()


# Create add flights page
add_flights_page = Frame(window)

label_id = Label(add_flights_page, text="ID:",background='#0B2447',foreground='#FEFAE0')
label_id.grid(row=0, column=0)

entry_id = Entry(add_flights_page)
entry_id.grid(row=0, column=1)

label_ac_id = Label(add_flights_page, text="AC_ID:",background='#0B2447',foreground='#FEFAE0')
label_ac_id.grid(row=1, column=0)
entry_ac_id = Entry(add_flights_page)
entry_ac_id.grid(row=1, column=1)

label_airport = Label(add_flights_page, text="Airport:",background='#0B2447',foreground='#FEFAE0')
label_airport.grid(row=2, column=0)
entry_airport = Entry(add_flights_page)
entry_airport.grid(row=2, column=1)

label_date = Label(add_flights_page, text="Date:",background='#0B2447',foreground='#FEFAE0')
label_date.grid(row=3, column=0)
entry_date = Entry(add_flights_page)
entry_date.grid(row=3, column=1)

label_source = Label(add_flights_page, text="Source:",background='#0B2447',foreground='#FEFAE0')
label_source.grid(row=4, column=0)
entry_source = Entry(add_flights_page)
entry_source.grid(row=4, column=1)

label_dest = Label(add_flights_page, text="Destination:",background='#0B2447',foreground='#FEFAE0')
label_dest.grid(row=5, column=0)
entry_dest = Entry(add_flights_page)
entry_dest.grid(row=5, column=1)

label_seats = Label(add_flights_page, text="Number of Seats:",background='#0B2447',foreground='#FEFAE0')
label_seats.grid(row=6, column=0)
entry_seats = Entry(add_flights_page)
entry_seats.grid(row=6, column=1)

label_price = Label(add_flights_page, text="Price:",background='#0B2447',foreground='#FEFAE0')
label_price.grid(row=7, column=0)
entry_price = Entry(add_flights_page)
entry_price.grid(row=7, column=1)

# Create a button to add the flight
button_add = Button(add_flights_page, text="Add Flight", command=add_flight,background='#0B2447',foreground='#FEFAE0')
button_add.grid(row=8, column=0, columnspan=2)



# Create update flights page
update_flights_page = Frame(window)

lbl_flight_id = Label(update_flights_page, text="Flight ID:", background='#0B2447',foreground='#FEFAE0')
lbl_flight_id.pack()
entry_flight_id = Entry(update_flights_page)
entry_flight_id.pack()

lbl_ac_id = Label(update_flights_page, text="AC ID:", background='#0B2447',foreground='#FEFAE0')
lbl_ac_id.pack()
entry_ac_id = Entry(update_flights_page)
entry_ac_id.pack()

lbl_airport = Label(update_flights_page, text="Airport:", background='#0B2447',foreground='#FEFAE0')
lbl_airport.pack()
entry_airport = Entry(update_flights_page)
entry_airport.pack()

lbl_date = Label(update_flights_page, text="Date:", background='#0B2447',foreground='#FEFAE0')
lbl_date.pack()
entry_date = Entry(update_flights_page)
entry_date.pack()

lbl_source = Label(update_flights_page, text="Source:", background='#0B2447',foreground='#FEFAE0')
lbl_source.pack()
entry_source = Entry(update_flights_page)
entry_source.pack()

lbl_dest = Label(update_flights_page, text="Destination:", background='#0B2447',foreground='#FEFAE0')
lbl_dest.pack()
entry_dest = Entry(update_flights_page)
entry_dest.pack()

lbl_seats = Label(update_flights_page, text="Number of Seats:", background='#0B2447',foreground='#FEFAE0')
lbl_seats.pack()
entry_seats = Entry(update_flights_page)
entry_seats.pack()

lbl_price = Label(update_flights_page, text="Price:", background='#0B2447',foreground='#FEFAE0')
lbl_price.pack()
entry_price = Entry(update_flights_page)
entry_price.pack()

# Create a button to update the flight
btn_update_flight = Button(update_flights_page, text="Update Flight", command=update_flight, background='#0B2447',foreground='#FEFAE0')
btn_update_flight.pack()


# Create cutomer page
admin_page = Frame(window)
lbl_cutomer = Label(admin_page, text="Welcome to the Cutomer Page!")


first_name = Label(admin_page, text="First Name:", background='#0B2447',foreground='#FEFAE0')
first_name.grid(row=2, column=0, sticky="w")
entry_first_name_customer = Entry(admin_page)
entry_first_name_customer.grid(row=2, column=1)
message_customer_first_name = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_first_name.grid(row=1, column=0, columnspan=2, sticky="w")

last_name = Label(admin_page, text="Last Name:", background='#0B2447',foreground='#FEFAE0')
last_name.grid(row=4, column=0, sticky="w")
entry_last_name_customer = Entry(admin_page)
entry_last_name_customer.grid(row=4, column=1)
message_customer_last_name = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_last_name.grid(row=3, column=0, columnspan=2, sticky="w")

phone = Label(admin_page, text="Phone:", background='#0B2447',foreground='#FEFAE0')
phone.grid(row=6, column=0, sticky="w")
entry_phone_customer= Entry(admin_page)
entry_phone_customer.grid(row=6, column=1)
message_customer_phone = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_phone.grid(row=5, column=0, columnspan=2, sticky="w")

address = Label(admin_page, text="Address:", background='#0B2447',foreground='#FEFAE0')
address.grid(row=8, column=0, sticky="w")
entry_address_customer = Entry(admin_page)
entry_address_customer.grid(row=8, column=1)
message_customer_address = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_address.grid(row=7, column=0, columnspan=2, sticky="w")



email = Label(admin_page, text="Email:", background='#0B2447',foreground='#FEFAE0')
email.grid(row=10, column=0, sticky="w")
entry_email_customer = Entry(admin_page)
entry_email_customer.grid(row=10, column=1)
message_customer_email = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_email.grid(row=9, column=0, columnspan=2, sticky="w")


btn_customer_data = Button(admin_page, text="Update", command=show_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_customer_data.grid(row=16, column=1)


# Create admin page
admin_page = Frame(window)

lbl_admin = Label(admin_page, text="Welcome to the Admin Page!")


first_name = Label(admin_page, text="First Name:", background='#0B2447',foreground='#FEFAE0')
first_name.grid(row=2, column=0, sticky="w")
entry_first_name_customer = Entry(admin_page)
entry_first_name_customer.grid(row=2, column=1)
message_customer_first_name = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_first_name.grid(row=1, column=0, columnspan=2, sticky="w")

last_name = Label(admin_page, text="Last Name:", background='#0B2447',foreground='#FEFAE0')
last_name.grid(row=4, column=0, sticky="w")
entry_last_name_customer = Entry(admin_page)
entry_last_name_customer.grid(row=4, column=1)
message_customer_last_name = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_last_name.grid(row=3, column=0, columnspan=2, sticky="w")

phone = Label(admin_page, text="Phone:", background='#0B2447',foreground='#FEFAE0')
phone.grid(row=6, column=0, sticky="w")
entry_phone_customer= Entry(admin_page)
entry_phone_customer.grid(row=6, column=1)
message_customer_phone = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_phone.grid(row=5, column=0, columnspan=2, sticky="w")

address = Label(admin_page, text="Address:", background='#0B2447',foreground='#FEFAE0')
address.grid(row=8, column=0, sticky="w")
entry_address_customer = Entry(admin_page)
entry_address_customer.grid(row=8, column=1)
message_customer_address = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_address.grid(row=7, column=0, columnspan=2, sticky="w")



email = Label(admin_page, text="Email:", background='#0B2447',foreground='#FEFAE0')
email.grid(row=10, column=0, sticky="w")
entry_email_customer = Entry(admin_page)
entry_email_customer.grid(row=10, column=1)
message_customer_email = Label(admin_page, text="", fg="red", background='#0B2447',foreground='#FEFAE0')
message_customer_email.grid(row=9, column=0, columnspan=2, sticky="w")


btn_customer_data = Button(admin_page, text="Update", command=show_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_customer_data.grid(row=16, column=1)


# Create add aircraft page
add_aircraft_page = Frame(window)

id_label = Label(add_aircraft_page, text="ID:", background='#0B2447',foreground='#FEFAE0')
id_label.pack()
id_entry = Entry(add_aircraft_page)
id_entry.pack()

name_label = Label(add_aircraft_page, text="Name:", background='#0B2447',foreground='#FEFAE0')
name_label.pack()
name_entry = Entry(add_aircraft_page)
name_entry.pack()

capacity_label = Label(add_aircraft_page, text="Capacity:", background='#0B2447',foreground='#FEFAE0')
capacity_label.pack()
capacity_entry = Entry(add_aircraft_page)
capacity_entry.pack()

add_button = Button(add_aircraft_page, text="Add Craft", command=add_craft, background='#0B2447',foreground='#FEFAE0')
add_button.pack()


# Create update aircraft page
update_aircraft_page = Frame(window)

lbl_aircraft_id = Label(update_aircraft_page, text="Aircraft ID:", background='#0B2447',foreground='#FEFAE0')
lbl_aircraft_id.grid(row=0, column=0, sticky="w")
entry_aircraft_id = Entry(update_aircraft_page)
entry_aircraft_id.grid(row=0, column=1)

lbl_new_aircraft_name = Label(update_aircraft_page, text="Aircraft Name:", background='#0B2447',foreground='#FEFAE0')
lbl_new_aircraft_name.grid(row=1, column=0, sticky="w")
entry_new_aircraft_name = Entry(update_aircraft_page)
entry_new_aircraft_name.grid(row=1, column=1)

lbl_new_aircraft_capacity = Label(update_aircraft_page, text="Capacity:", background='#0B2447',foreground='#FEFAE0')
lbl_new_aircraft_capacity.grid(row=2, column=0, sticky="w")
entry_new_aircraft_capacity = Entry(update_aircraft_page)
entry_new_aircraft_capacity.grid(row=2, column=1)

btn_update_aircraft = Button(update_aircraft_page, text="Update Aircraft", command=update_aircraft, background='#0B2447',foreground='#FEFAE0')
btn_update_aircraft.grid(row=3, columnspan=2)

# Create navigation buttons
navigation_frame = Frame(window)

navigation_frame_Customer = Frame(window)

navigation_frame_Admin = Frame(window)

btn_register_page = Button(navigation_frame, text="Register Page", command=show_register_page, background='#0B2447', foreground='#FEFAE0')
btn_register_page.grid(row=0, column=0)

btn_login_page = Button(navigation_frame, text="Login Page", command=show_login_page, background='#0B2447', foreground='#FEFAE0')
btn_login_page.grid(row=0, column=1)

# Buttons for customer
btn_flights_page = Button(navigation_frame_Customer, text="Flights Page", command=show_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_flights_page.grid(row=0, column=2)

btn_flights_page = Button(navigation_frame_Customer, text="Customer Page", command=show_customer_page, background='#0B2447', foreground='#FEFAE0')
btn_flights_page.grid(row=0, column=3)

btn_my_flight = Button(navigation_frame_Customer, text="My Flights", command=show_my_flight_page, background='#0B2447', foreground='#FEFAE0')
btn_my_flight.grid(row=0, column=4)


# Buttons for admin
btn_admin_page = Button(navigation_frame_Admin, text="Admin Page", command=show_admin_page, background='#0B2447', foreground='#FEFAE0')
btn_admin_page.grid(row=0, column=7)

btn_flights_page = Button(navigation_frame_Admin, text="Flights Page", command=show_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_flights_page.grid(row=0, column=2)

btn_add_flight_page = Button(navigation_frame_Admin, text="Add Flights Page", command=show_add_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_add_flight_page.grid(row=0, column=3)

btn_update_flight_page = Button(navigation_frame_Admin, text="Update Flights Page", command=show_update_flights_page, background='#0B2447', foreground='#FEFAE0')
btn_update_flight_page.grid(row=0, column=4)

btn_add_aircraft_page = Button(navigation_frame_Admin, text="Add Aircraft", command=show_add_aircraft_page, background='#0B2447', foreground='#FEFAE0')
btn_add_aircraft_page.grid(row=0, column=5)

btn_update_aircraft_page = Button(navigation_frame_Admin, text="Update Aircraft", command=show_update_aircraft_page, background='#0B2447', foreground='#FEFAE0')
btn_update_aircraft_page.grid(row=0, column=6)

navigation_frame.pack(side=TOP, anchor=NE)


window.config(bg='#0B2447')

# Show login page by default
show_login_page()

# Run the main window's event loop
window.mainloop()