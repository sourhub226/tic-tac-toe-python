from tkinter import Button, Label, Tk, ttk
from tkinter.constants import ACTIVE, DISABLED, E, W

app = Tk()
app.geometry("326x373")
app.title("Tic Tac Toe")
app.configure(background="white")


class Global:
    def __init__(self):
        self.turn1 = True


Global = Global()


def reset(restart):
    # global turn1
    Global.turn1 = True
    turn_label["text"] = "Player 1's turn (X)"
    turn_label.config(bg="white")
    app.config(bg="white")
    restart.destroy()
    button_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for btn in button_list:
        btn["text"] = ""
        btn["state"] = ACTIVE


def disp_win():
    # global turn1
    if not Global.turn1:
        set_win("#50d890", "Player 1 (X) wins!")
    else:
        set_win("#ed8240", "Player 2 (O) wins!")
    button_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for btn in button_list:
        btn["state"] = DISABLED
    restart_btn()


def set_win(bg, text):
    turn_label.config(bg=bg)
    app.config(bg=bg)
    turn_label["text"] = text


def restart_btn():
    restart = ttk.Button(app, text="Restart", command=lambda: reset(restart))
    restart.grid(row=3, column=2, sticky=E, padx=5)


def check_win():
    # rows
    if b1["text"] == b2["text"] == b3["text"] and b1["text"] in ["X", "O"]:
        disp_win()
    elif b4["text"] == b5["text"] == b6["text"] and b4["text"] in ["X", "O"]:
        disp_win()
    elif b7["text"] == b8["text"] == b9["text"] and b7["text"] in ["X", "O"]:
        disp_win()
    elif b1["text"] == b4["text"] == b7["text"] and b1["text"] in ["X", "O"]:
        disp_win()
    elif b2["text"] == b5["text"] == b8["text"] and b2["text"] in ["X", "O"]:
        disp_win()
    elif b3["text"] == b6["text"] == b9["text"] and b3["text"] in ["X", "O"]:
        disp_win()
    elif b1["text"] == b5["text"] == b9["text"] and b1["text"] in ["X", "O"]:
        disp_win()
    elif b3["text"] == b5["text"] == b7["text"] and b3["text"] in ["X", "O"]:
        disp_win()
    elif (
        b1["state"]
        == b2["state"]
        == b3["state"]
        == b4["state"]
        == b5["state"]
        == b6["state"]
        == b7["state"]
        == b8["state"]
        == b9["state"]
        == DISABLED
    ):
        restart_btn()
        turn_label["bg"] = "yellow"
        turn_label["text"] = "Draw!"
        app.config(bg="yellow")


def toggle_turn(btn):
    # global turn1
    if Global.turn1:
        set_player(btn, "X", "Player 2's turn (O)", False)
    else:
        set_player(btn, "O", "Player 1's turn (X)", True)
    btn["disabledforeground"] = "black"
    btn["state"] = DISABLED
    check_win()


def set_player(btn, player, text, turn):
    btn["text"] = player
    turn_label["text"] = text
    Global.turn1 = turn


b1 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b1),
)
b1.grid(row=0, column=0, sticky=W)
b2 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b2),
)
b2.grid(row=0, column=1, sticky=W)
b3 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b3),
)
b3.grid(row=0, column=2, sticky=W)
b4 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b4),
)
b4.grid(row=1, column=0, sticky=W)
b5 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b5),
)
b5.grid(row=1, column=1, sticky=W)
b6 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b6),
)
b6.grid(row=1, column=2, sticky=W)
b7 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b7),
)
b7.grid(row=2, column=0, sticky=W)
b8 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b8),
)
b8.grid(row=2, column=1, sticky=W)
b9 = Button(
    app,
    text="",
    height=1,
    width=3,
    font=("verdana", "40"),
    command=lambda: toggle_turn(b9),
)
b9.grid(row=2, column=2, sticky=W)

turn_label = Label(
    app, text="Player 1's turn (X)", font=("verdana", "15"), bg="white", fg="#202125"
)
turn_label.grid(row=3, column=0, columnspan=3, sticky=W, padx=5)

app.mainloop()
