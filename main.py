from tkinter import *
from tkinter import messagebox
from random import *
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_password():
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data File found')
    else:
        if website_input.get() in data:
            email = data[website_input.get()]['Email']
            password = data[website_input.get()]['Password']
            messagebox.showinfo(title=f'{website_input.get()}', message=f'Email: {email} \n'
                                                                        f'Password: {password}')
        else:
            messagebox.showerror(title='Error', message=f'No details for {website_input.get()} exists.')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    messagebox.askquestion(title=website_input.get(), message=f'These are the details entered: '
                                                              f'\nEmail: {email_input.get()} '
                                                              f'\nPassword: {password_input.get()} '
                                                              f'\nIs it OK to save ?')

    new_data = {
        website_input.get(): {
            'Email': email_input.get(),
            'Password': password_input.get()
        }
    }

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open('data.json', 'w') as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open('data.json', 'r') as data_file:
            json.dump(new_data, data_file, indent=4)
    finally:
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# window config
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# image config
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# form config
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

search_button = Button(bg='#ffffff', text='Search', width=14, command=search_password)
search_button.grid(column=2, row=1)
generate_button = Button(bg='#ffffff', text='Generate Password', width=14, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(bg='#ffffff', text='Add', width=35, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
