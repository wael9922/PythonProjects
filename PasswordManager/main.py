from tkinter import *
from tkinter import messagebox
import random
import string
import json

def password_generator(nr_letters=8, nr_digits=4, nr_symbols=1):
    """generate a password if user want a suggested password"""
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+']
    password = []
    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_digits):
        password.append(random.choice(numbers))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    password_entry.delete(0, END)
    password_entry.insert(0, ''.join(password))

def add():
    """Add the details to a data text file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "Email": email,
            "Password": password
        }
    }
    message_details = f"Email: {email}\nPassword: {password}\nProceed?"
    if len(website) == 0 or len(email) == 0 or len(password)==0:
        messagebox.showwarning("Fields Required",message="You can't leave an empty field!")
    else:
        if messagebox.askyesno(title=website,message=message_details):
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            except json.JSONDecodeError:
                data = {}
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def find_password():
    """Search the email and password associated with a given website."""
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # You need to add one password at least to create data file
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists.")

# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew", pady=5)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, sticky="ew", padx=5,pady=5)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew", padx=5)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, sticky="ew", pady=5)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

window.mainloop()