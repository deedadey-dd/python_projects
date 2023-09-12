import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
screen.bgpic("blank_states_img.gif")

# answer_text = screen.textinput("Guess a State", "What's Another State Name?").title()
# print(answer_text)

raw_data = pandas.read_csv("50_states.csv")
states = raw_data.to_dict()
# print(states)
# print(states["x"][0])

guess_count = 0
guesses = []
all_states = raw_data.state.to_list()
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

while guess_count < 50:

    answer_text = screen.textinput(f"{guess_count}/50 States Correct", "What's Another State Name?").title()
    if answer_text == "Exit":
        remaining_states = [state for state in all_states if state not in guesses]
        # for state in all_states:
        #     if state not in guesses:
        #         remaining_states.append(state)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("remaining_states.csv")
        break

    for state_number in range(0, 50):
        if answer_text == states["state"][state_number] and answer_text not in guesses:
            guesses.append(answer_text)
            new_state = states["state"][state_number]
            new_x = states["x"][state_number]
            new_y = states["y"][state_number]
            timmy.goto(new_x, new_y)
            timmy.write(f"{new_state}",move=False, align="center", font=("cambria", 12, "normal"))
            guess_count += 1

# create a csv of the states that are not guessed.


for state in all_states:
    if state not in guesses:
        with open("remaining_states.csv", mode="a") as file:
            file.write(f"{state}\n")


# screen.exitonclick()
    # if answer_text is in the list of states,
    # Write name of the state at the assigned coordinate position
    # increment guess_count by 1 and repeat the process.
    # if guess_count reaches 50 show Congratulations.





# turtle.mainloop()
