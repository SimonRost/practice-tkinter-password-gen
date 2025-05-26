from re import search
from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pw():
    website = input_website.get()
    try:
        with open("data.json", "r") as pw_vault:
            data = json.load(pw_vault)
    except FileNotFoundError:
        messagebox.showinfo(title="Not found.",
                            message=f"Entry for {website} not found.")
    else:
        if website in data.keys():
            messagebox.showinfo(title=website,
                            message=f"Email: {data[website]["email"]}"
                                    f"\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Not found.",
                                message=f"Entry for {website} not found.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    from random import choice, randint, shuffle
    import pyperclip

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    input_password.delete(0, "end")

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    website = input_website.get()
    email = input_mail_user.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please enter a website and password.")
    else:
        website = input_website.get()
        try:
            with open("data.json", "r") as pw_vault:
                data = json.load(pw_vault)
        except FileNotFoundError:
            with open("data.json", "w") as pw_vault:
                json.dump(new_data, pw_vault, indent=4)
        else:
            if website in data.keys():
                messagebox.showinfo(title=f"Entry {website} already exists!",
                                    message=f"Email: {data[website]["email"]}"
                                            f"\nPassword: {data[website]["password"]}")
            else:
                data.update(new_data)
                with open("data.json", "w") as pw_vault:
                    json.dump(data, pw_vault, indent=4)
        finally:
            input_website.delete(0, "end")
            input_password.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_mail_user = Label(text="Email/Username:")
label_mail_user.grid(column=0, row=2, columnspan=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

input_website = Entry(width=25)
input_website.grid(column=1, row=1, sticky="EW")
input_website.focus()
input_mail_user = Entry(width=25)
input_mail_user.grid(column=1, row=2, sticky="EW")
input_mail_user.insert(0, "simon@gmail.com")
input_password = Entry(width=25)
input_password.grid(column=1, row=3, sticky="EW")

button_search = Button(text="Search", command=search_pw)
button_search.grid(column=2, row=1, sticky="EW")
button_genpw = Button(text="Generate Password", command=generate_pw)
button_genpw.grid(column=2, row=3, sticky="EW")
button_add = Button(text="Add", command=add_pw, width=35)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
