from email import message
from tkinter import *
from tkinter import messagebox
import password_generator
from requests import delete
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    pwd = password_generator.generate_pwd()
    pwd_ip.delete(0, END)
    pwd_ip.insert(0, pwd)
    pyperclip.copy(pwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_info():
    web_data = web_ip.get()
    email_data = email_ip.get()
    pwd_data = pwd_ip.get()
    if web_data and email_data and pwd_data:
        messagebox.askokcancel(title = "Confirmation", message = f"These are the details entered:\nWebsite: {web_data}\nEmail: {email_data}\nPassword: {pwd_data}\nPermission to procceed and save?")
        with open("passwords.txt", "a+") as pwds:
            pwds.write(f"{web_data}|{email_data}|{pwd_data}\n")
        web_ip.delete(0, END)
        pwd_ip.delete(0, END)
    else:
        messagebox.showerror(title = "Error", message = "Please fill in all the details")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50,)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

website = Label(text = "Website:", font = ("Tw cen MT", 11), padx = 0)
email = Label(text = "Email/Username:", font = ("Tw cen MT", 11), padx = 0)
pwd = Label(text = "Password:", font = ("Tw cen MT", 11), padx = 0)
website.grid(column = 0, row = 1)
email.grid(column = 0, row = 2)
pwd.grid(column = 0, row = 3)

web_ip = Entry(width = 45)
web_ip.focus() # focus
email_ip = Entry(width = 45)
pwd_ip = Entry(width = 27)
web_ip.grid(column = 1, row = 1, columnspan = 2)
email_ip.grid(column = 1, row = 2, columnspan = 2)
email_ip.insert(0, "common") # pre-populate
pwd_ip.grid(column = 1, row = 3, columnspan = 1)

gen_pwd_button = Button(text = "Generate Password", width = 15, pady = 0, command = gen_pwd)
gen_pwd_button.grid(column = 2, row = 3, columnspan = 2)

add_button = Button(text = "Add", width = 42, pady = 0, command = get_info)
add_button.grid(column = 1, row = 4, columnspan = 2)





window.mainloop()