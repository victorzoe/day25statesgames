import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guess_state = []
state_data = pandas.read_csv('50_states.csv')
all_states = state_data['state'].to_list()
while len(guess_state) < 50:   
    ans_states = screen.textinput(title = f"{len(guess_state)}/50 correct States Correct", prompt = 'Whats another states games?')
    if ans_states == 'Exit':
        missing_state = []
        for state in guess_state:
            if state not in all_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('missing_state.csv')
        break
    
    
    if ans_states in all_states:
        guess_state.appen(ans_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        ans_states = ans_states.title()
        ans_data = state_data[state_data['state'] == ans_states]
        t.goto(ans_data['x'].item(), ans_data['y'].item())
        t.write(ans_data['state'].item())
    
    











screen.exitonclick()





