
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =  [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_site():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Password Check", message="Please make sure you haven't left any fields empty.")
    elif len(password) < 6:
        messagebox.showinfo(title="Password Check", message="Password is not secure, \n please generate a password longer than 6 characters or update.")
    elif not any(c in symbols for c in password):
        messagebox.showinfo(title="Password Check", message="Password is not secure, \n please add symbols to your password or select generate a password.")
    elif not any(c in numbers for c in password):
        messagebox.showinfo(title="Password Check", message="Password is not secure, \n please add numbers to your password or select generate a password.")

    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- 
# ---------------------------- SEARCH ------------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= website, message=f"Email: {username} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="There is no details for this website.")
 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady=20)

canvas = Canvas(height= 200, width= 200)
logo_img = PhotoImage(file ="pass2.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan= 3)

website_label = Label(text="Website: " )
website_label.grid(row=1, column=0)

website_entry = Entry(width = 22)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width= 12, command= search_password)
search_button.grid(row=1, column= 2)

username_label = Label(text="Username/Email: " )
username_label.grid(row=2, column=0)

username_entry = Entry(width = 38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "hire-me@live.co.uk")

password_label = Label(text="Password: " )
password_label.grid(row=3, column=0)

password_entry = Entry(width = 22)
password_entry.grid(row=3, column=1)

generate_button = Button(text= "Generate Password", width= 12, command= generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command = add_site)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
