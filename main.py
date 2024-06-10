from tkinter import *
from tkinter import font
from tkinter import messagebox
import random
import pyperclip

CHARACTERS = "abcdef_gh!ijk_lmn$op_qr^stu_vxy*z1234567890!@#$^*("


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pwd():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # password_letters = [char for char in letters[nr_letters]]
    # password_symbols = [char for char in symbols[nr_symbols]]  # my password is getting generated as k%4
    # password_numbers = [char for char in numbers[nr_numbers]]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    #  join string method using function join

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)   # save the password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    data_website_entry = website_entry.get()
    data_email_entry = email_entry.get()
    data_password_entry = password_entry.get()

    if len(data_website_entry) == 0 or len(data_password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{data_website_entry}",
                                       message=f"These are details entered:\nEmail:{data_email_entry} \nPassword: {data_password_entry}\nIs is ok?")

        with open("data.txt", "a") as file:
            file.write(f'{data_website_entry} | {data_email_entry} | {data_password_entry} \n ')
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

        messagebox.showinfo(title="Success", message=f"Added {data_website_entry} to the data store")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pwd():
    pass


# ------------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("PASSWORD MANAGER")
window.resizable(False, False)  # No scope of resizing the dimensions in either of the axes
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)  # width 200 and height 200--the dimensions of the image
canvas.grid(column=1, row=0)

list_fonts = list(font.families())

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="E-Mail/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(window, width=35)
email_entry.insert(0, "amber_m123@e-mail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# how to get the entry box towards the label defining it

generate_button = Button(text="Generate Password", bg="white", command=gen_pwd)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=29, command=save, bg="white")
add_button.grid(column=1, row=4, columnspan=2)

# search_button = Button(text='Search', bg ='white', command=search_pwd())

window.mainloop()
