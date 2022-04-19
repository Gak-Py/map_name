import pandas
import turtle

screen = turtle.Screen()
screen.title("日本地図都道府県当てゲーム")
screen.setup(883, 800)
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("47ken.csv")

all_states = data.state.to_list()
states_num = []

# テキストを書く位置を見つける
# def get_mouse_click_point(x,y):
#     print(x,y)
# turtle.onclick(get_mouse_click_point)

while len(states_num) < 48:
    answer = screen.textinput(f"{len(states_num)}/47県 正解!", "都道府県名を答えてください")
    # print(answer)

    if answer in all_states:
        ken = turtle.Turtle()
        ken.ht()
        ken.penup()
        state_data = data[data.state == answer]
        ken.goto(int(state_data.x), int(state_data.y))
        ken.write(answer)
        states_num.append(answer)

    elif answer == "save":
        remain_states = []
        for state in all_states:
            if state not in states_num:
                remain_states.append(state)
        remain_data = pandas.DataFrame(remain_states)
        remain_data.to_csv("remain_states.csv", header=False, index=False)
        break

screen.exitonclick()
