import io
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
user_data = {}


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_comp = "".join(([random.choice(letters) for char in range(nr_letters)] + [random.choice(numbers) for char in range(nr_symbols)] + [random.choice(symbols) for char in range(nr_numbers)]))
    password.insert(0, password_comp)
    pyperclip.copy(password_comp)
    print(password_comp)


def store_data():
    website_get = website.get()
    username_email_get = username_email.get()
    password_get = password.get()
    new_data = {
        website_get: {
            "email": username_email_get,
            "password": password_get,
        }
    }
    if not website_get:
        print("Website can't be empty")
        messagebox.askokcancel(title="Title", message=f"website can't be empty")

    if not username_email_get:
        print("username can't be empty")
        messagebox.askokcancel(title="Title", message=f"username can't be empty")

    if not password_get:
        print("password can't be empty")
        messagebox.askokcancel(title="Title", message=f"password can't be empty")

    # user_data.update({username_email_get: [website_get, password_get]})
    is_ok = messagebox.askokcancel(title="Title", message=f"These are the details entered \n Email:{website_get} \n username:{username_email_get} \n password:{password_get}")

    if is_ok and website_get and username_email_get and password_get:

        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                print(f'1 {data}')
                data.update(new_data)
                print(f'11 {data}')
            with open('data.json', 'w') as data_file2:
                print(f'2 {data}')
                json.dump(data, data_file2, indent=4)
                print('dump')
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
                print('exception dump')

        website.delete(0, END)
        # username_email.delete(0, END)
        password.delete(0, END)
    return


def search():
    website_get = website.get()
    with open("data.json", "r") as data_file:
        to_search = json.load(data_file)
        for key, value in to_search.items():
            if website_get == key:
                tkinter.messagebox.showinfo(title=f"{key}", message=f"Email: {value['email']} \nPassword: {value['password']}")
                print(key)
                return
        tkinter.messagebox.showinfo(title=f"No Data Found", message=f"No data found")


window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)
# window.geometry('200x200')

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(80, 100, image=logo_image)
canvas.grid(column=1, row=0, sticky='w')

label1 = tkinter.Label(text='Website:')
label1.grid(column=0, row=1)

label2 = tkinter.Label(text='Email/Username:')
label2.grid(column=0, row=2)

label3 = tkinter.Label(text='Password:')
label3.grid(column=0, row=3)

button1 = tkinter.Button(text='Generate Password', command=generate_password)
button1.grid(column=1, row=3, columnspan=3, ipadx=11, sticky='e')

website = tkinter.Entry(window, width=21)
website.grid(column=1, row=1, columnspan=3, sticky='w')
website.focus()

username_email = tkinter.Entry(window, width=43)
username_email.grid(column=1, row=2, columnspan=3, sticky='w')
username_email.insert(0, "szymon@gmail.com")


password = tkinter.Entry(window, width=21)
password.grid(column=1, row=3, sticky='w')


button2 = tkinter.Button(text='Add', width=36, command=store_data)
button2.grid(column=1, row=4, columnspan=2, sticky='w')


search1 = tkinter.Button(text='Search', command=search)
search1.grid(column=1, row=1, columnspan=3, ipadx=42, sticky='e')
window.mainloop()
