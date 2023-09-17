from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


FONT = ("calibri", 11, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project from appbrewery

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(4, 8))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    text_password.delete(0, END)
    text_password.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = text_website.get()
    username = text_user.get()
    password = text_password.get()

    if len(password) < 1 or len(website) < 1:
        messagebox.askretrycancel(title="Empty Fields", message="Some Fields are Empty")
    else:
        is_correct = messagebox.askokcancel(title=f"{website} Credentials", message=f"Do you want to save? \nWebsite: {website} "
                                                                       f"\n Email/ Username: {username} "
                                                                       f"\nPassword: {password}")
        if is_correct:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")

            pyperclip.copy(f"{password}")

            messagebox.showinfo(title="Saved", message="Password Copied to Clipboard")

            text_website.delete(0, END)
            # text_user.delete(0, END)
            text_password.delete(0, END)
            text_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("My Pass")
window.configure(padx=50, pady=70)

# Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)
label_user = Label(text="Email/Username:", font=FONT)
label_user.grid(row=2, column=0)
label_password = Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

# Entries
text_website = Entry(font=FONT, width=45)
text_website.grid(row=1, column=1, columnspan=2)
text_website.focus()
text_user = Entry(font=FONT, width=45)
text_user.grid(row=2, column=1, columnspan=2)
text_user.insert(0, "deedadey@gmail.com")
text_password = Entry(font=FONT, width=28)
text_password.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", font=("Calibri", 10, "normal"), command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", font=FONT, width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
