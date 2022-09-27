from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            messagebox.showinfo(title="Details", message=f"Email: {data[website.get()]['email']}\nPassword: {data[website.get()]['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title="", message="No passwords stored yet.")
    except KeyError:
        messagebox.showwarning(title="", message=f"No details for {website.get()} exists.")







# ---------------------------- PASSWORD GENERATOR ------------------------------- #

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!', '#', '$', '%', '&', '(', ')', '*', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def create_password():
    password.delete(0, END)
    password_list = [random.choice(characters) for _ in range(random.randint(14, 18))]
    new_password = "".join(password_list)
    password.insert(0, f"{new_password}")
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website.get(): {
            "email": email_entry.get(),
            "password": password.get(),
        }
    }
    if len(website.get()) == 0:
        messagebox.showwarning(title="", message="Please, insert the website.")
    elif len(email_entry.get()) == 0:
        messagebox.showwarning(title="", message="Please, insert the email.")
    elif len(password.get()) == 0:
        messagebox.showwarning(title="", message="Please, generate the password.")
    else:
        is_ok = messagebox.askokcancel(title="", message=f"These are the details entered: \nWebsite: {website.get()}\nEmail: {email_entry.get()} \nPassword: {password.get()} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)


            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website.delete(0, END)
                password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website = Entry(width=21)
website.grid(column=1, row=1)



email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@example.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password = Entry(width=21)
password.grid(column=1, row=3)


generate_button = Button(text="Generate Password", command=create_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save)
add_button.grid_configure(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()
