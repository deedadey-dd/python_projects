from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.4
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    global timer
    reps = 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.configure(text="Timer")
    label_tick.configure(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0 and reps > 0:
        label_timer.configure(text="LONG BREAK", fg=RED)
        count = long_break_sec
    elif reps % 2 == 0 and reps > 0:
        label_timer.configure(text="SHORT BREAK", fg=PINK)
        count = short_break_sec
    else:
        label_timer.configure(text="WORK", fg=GREEN)
        count = work_sec

    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global timer
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            n = int((reps+1)/2)
            label_tick.configure(text="✔" * n)
        reps += 1
        start()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.configure(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

label_timer = Label(text="Timer", fg=GREEN, font=("Courier", 24, "bold"))
label_timer.configure(bg=YELLOW)
label_timer.grid(row=0, column=1)

label_tick = Label(fg=GREEN)
label_tick.configure(bg=YELLOW)
label_tick.grid(row=3, column=1)

button_start = Button(text="Start", command=start)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
