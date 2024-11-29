from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json

EMAIL = "rumaandev@gmail.com"


# ---------------------------- PASSWORD SEARCHING ------------------------------- #
def search():
    websiteget = website_input.get()
    email2 = email_input.get()
    try:
        with open("data.json", "r") as x:
            data1 = json.load(x)
    except FileNotFoundError:
        messagebox.showerror(title="No data found", message="please add details to the manager")
    else:
        result = data1[websiteget]
        password = result["password"]
        # messagebox.OK(title=f"reuslts found for {websiteget}", text=f"password: {password}")
        messagebox.showinfo(f"{websiteget} Details",f"email:{email2} \n password:{password}")
        print(password)
    finally:
        x.close()
    pass


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    password_input.delete(0, END)
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website1 = website_input.get()
    email1 = email_input.get()
    pwd = password_input.get()
    new_data = {
        website1: {
            "email": email1,
            "password": pwd
        }
    }

    check_website1 = len(website1)
    check_pwd = len(pwd)

    if check_pwd <= 0 or check_website1 <= 0:
        messagebox.showerror(title="No Entry found", message="please enter valid website or password")
    else:

        is_ok = messagebox.askokcancel(title="Check details",
                                       message=f" do you want to save these details? \nwebsite: {website1} \nEmail: {email1} \npassword: {pwd}")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    all_data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open("data.json", "w") as f:
                    all_data.update(new_data)
                    json.dump(all_data, f, indent=4)
                f.close()
            finally:
                website_input.delete(0, END)
                # email_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password manager")
# window.minsize(height=200, width=200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
file = PhotoImage(file="logo.png")
canvas.create_image(145, 100, image=file)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:")
website.grid(column=0, row=1)
Email = Label(text="Email:")
Email.grid(column=0, row=2)
Password = Label(text="Password:")
Password.grid(column=0, row=3)

# Entries
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()
email_input = Entry(width=60)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, EMAIL)
password_input = Entry(width=40)
password_input.grid(row=3, column=1)

# buttons

search_button = Button(text="Search", command=search, width=15)
search_button.grid(row=1, column=2, )
generate = Button(text="Generate Password", command=password_generate, width=15)
generate.grid(row=3, column=2, )
add = Button(text="Add", width=50, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
