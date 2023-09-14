# import playground
# import tkinter
#
# print(playground.add(1, 2, 3, 4, 5))
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tkinter.Label(text="I am a label", font=("Cambria", 20, "bold"))
# my_label.pack()
#
#
# def button_clicked():
#     the_text = new_input.get()
#     my_label.config(text=f"{the_text}")
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
#
# # create a text entry or input field - textbox
#
# new_input = tkinter.Entry(width=12)
# new_input.pack()
#
#
# window.mainloop()
#

from tkinter import *

LABEL_FONT = ("Cambria", 16, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
# window.configure(bg="black")


miles_textbox = Entry(width=14)
miles_textbox.place(relx=0.4, rely=0.2, anchor="nw")
# miles.grid(row=1, column=1, pady=2)
# miles.pack()
label_1 = Label(text="Miles", font=LABEL_FONT)
label_1.place(relx=0.6, rely=0.2, anchor="nw")

label_2 = Label(text="is equal to", font=LABEL_FONT)
label_2.place(relx=0.1, rely=0.4, anchor="nw")


def calculate_kilometers():
    miles = miles_textbox.get()
    kilometers = round(int(miles) * 1.609)
    label_km.configure(text=f"{kilometers}")


label_km = Label(text="0", font=LABEL_FONT)
label_km.place(relx=0.4, rely=0.4, anchor="nw")

label_3 = Label(text="Km", font=LABEL_FONT)
label_3.place(relx=0.6, rely=0.4, anchor="nw")

calculate_button = Button(text="Calculate", font=LABEL_FONT, command=calculate_kilometers)
calculate_button.configure(width=10)
calculate_button.place(relx=0.4, rely=0.6, anchor="nw")



window.mainloop()
