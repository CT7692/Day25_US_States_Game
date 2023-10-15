import turtle as t
import pandas as p
from random import choice

def get_text_box(my_title, my_prompt, screen_obj):
    my_guess = screen_obj.textinput(title=my_title, prompt=my_prompt)
    return my_guess

def play(score, state_data, screen_obj, g_states):
    prompt = "Can you guess any of the state names?"
    while score < 50:
        guess = get_text_box(my_title=f"Guess State Name {score}/50",
                             my_prompt=prompt, screen_obj=screen_obj)
        score = check_answer(score, state_data, guess, screen_obj, g_states)

def check_answer(score, s_data, my_guess, my_screen, g_states):
    states = s_data["state"].to_list()
    guess = my_guess.title()
    for state in states:
        if state == guess and state not in g_states:
            score += 1
            tom = get_state(state, s_data, my_screen)
            g_states.append(state)
    return score

def get_state(my_state, s_data, my_screen):
    my_screen.tracer(0)
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.hideturtle()
    text = my_state
    state_row = s_data[s_data.state == my_state]
    state_x = state_row.x.iloc[0]
    state_y = state_row.y.iloc[0]
    new_turtle.setpos(x=state_x, y=state_y)
    new_turtle.write(text)
    my_screen.update()
    return new_turtle


my_screen = t.Screen()
image = "blank_states_img.gif"
my_screen.addshape(image)
t.shape(image)
state_data = p.read_csv("50_states.csv")
my_score = 0
guessed_states = []
active = play(my_score, state_data, my_screen, guessed_states)
my_screen.exitonclick()
