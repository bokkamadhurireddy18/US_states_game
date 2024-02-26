import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def check_answer(answer):
    if answer in states:
        tim = turtle.Turtle()
        state_data = data[data.state == answer]
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_data["x"]), int(state_data["y"]))
        tim.write(answer, font= 20)
        return True

Guessed_states = []
while len(Guessed_states) < 50: #0 to 49
    answer = screen.textinput(title=f"Correct Guesses: {len(Guessed_states)}/50",
                             prompt="Enter the state name:").title()
    if check_answer(answer):
        Guessed_states.append(answer)

screen.exitonclick()
